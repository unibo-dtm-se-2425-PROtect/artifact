from getpass import getpass
from project.dbconfig import dbconfig
from rich import print as printc

from project import AES256util
import hashlib 

#function to compute the masterkey from the masterPassword (mp) and the the deviceSecret (ds)
def computeMasterKey(mp,ds): 
    combined= (mp + ds).encode()
    return hashlib.sha256(combined).digest()

def checkEntry(Site, URL, Email, Username):
    db = dbconfig()
    cursor = db.cursor()
    query = "SELECT * FROM PROtect.entries WHERE Site=%s AND URL=%s AND Email=%s AND Username=%s"
    cursor.execute(query, (Site, URL, Email, Username))
    results = cursor.fetchall()

    if len(results)!=0:
        return True
    return False

def req_fields(Site, Username, Password):
    missing=[]
    if not Site or Site.strip()=="":
        missing.append("Site")
    if not Username or Username.strip()=="":
        missing.append("Username")
    if not Password or Password.strip()=="":
        missing.append("Password")
    if missing:
        printc(f"[red][!] The following required fields are empty: {', '.join(missing)}[/red]")
        return False
    return True

def addEntry(mp, ds, Site, URL, Email, Username, Password): 
    if not Password:
        raise ValueError("Password cannot be empty")

    if not req_fields(Site, Username, Password):
        return #stop if required fields are missing 
    
    #check if the entry already exists
    try:
        if checkEntry(Site, URL, Email, Username):
            printc("[yellow][-][/yellow] This entry already exists")
            return

        mk = computeMasterKey(mp,ds) #to compute the master key
        mk_hex=mk.hex()
        enc_pass=AES256util.encrypt(mk_hex, Password, keyType="hex")

        #validate that encryption actually returned data
        #if AES256util returns None or empty, we must stop
        if not enc_pass:
            raise ValueError("Encryption failed: Returned empty result")
        
        #using imported aesutil function to encrypt the mk 
        #this should return the encrypted password in base 64 encoded format
        enc_bytes = AES256util.encrypt(key=mk, source=Password, keyType="bytes")

        #add the new password to the database
        db = dbconfig()
        if db is None:
            printc("[red][!] Cannot connect to database[/red]")
            return
        cursor = db.cursor()
        query = "INSERT INTO PROtect.entries (Site, URL, Email, Username, Password) VALUES (%s, %s, %s, %s, %s)"
        val = (Site,URL,Email,Username,enc_pass)
        cursor.execute(query, val)
        db.commit()
        printc("[green][+][/green] Added entry ")
    except Exception as e:
        printc(f"[red][!][/red] Failed to add entry: {e}")
