from getpass import getpass
from project.dbconfig import dbconfig
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from rich import print as printc

from project import AES256util
import hashlib 

#function to compute the masterkey from the masterPassword (mp) and the the deviceSecret (ds)
def computeMasterKey(mp,ds): 
    combined= (mp + ds).encode()
    return hashlib.sha256(combined).hexdigest()

def checkEntry(sitename, siteurl, email, username):
    db = dbconfig()
    cursor = db.cursor()
    query = "SELECT * FROM PROtect.entries WHERE sitename=%s AND siteurl=%s AND email=%s AND username=%s"
    cursor.execute(query, (sitename, siteurl, email, username))
    results = cursor.fetchall()

    if len(results)!=0:
        return True
    return False

def addEntry(mp, ds, sitename, siteurl, email, username): 
    #check if the entry already exists
    try:
        if checkEntry(sitename, siteurl, email, username):
            printc("[yellow][-][/yellow] This entry already exists")
            return
    
        #get the password
        password = getpass("Password: ")

        mk = computeMasterKey(mp,ds) #to compute the master key
        enc_pass=AES256util.encrypt(mk, password, keyType=hex)

        #using imported aesutil function to encrypt the mk 
        #this should return the encrypted password in base 64 encoded format
        encrypted = AES256util.encrypt(key=mk, source=password, keyType="bytes")

        #add the new password to the database
        db = dbconfig()
        if db is None:
            printc("[red][!] Cannot connect to database[/red]")
            return
        cursor = db.cursor()
        query = "INSERT INTO PROtect.entries (sitename, siteurl, email, username, password) VALUES (%s, %s, %s, %s, %s)"
        val = (sitename,siteurl,email,username,enc_pass)
        cursor.execute(query, val)
        db.commit()
        printc("[green][+][/green] Added entry ")
    except Exception as e:
        printc(f"[red][!][/red] Failed to add entry: {e}")