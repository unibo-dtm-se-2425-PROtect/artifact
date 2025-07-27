from getpass import getpass
from dbconfig import dbconfig
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from rich import print as printc
from rich.console import console
import base64

import AES256util

#function to comupute the masterkey from the masterPassword (mp) and the the deviceSecret (ds)
def computeMasterKey(mp,ds): 
    password = mp.encode() #encoding the mp and save it as password
    salt = ds.encode() #encoding the ds and save it as salt
    #using the PBDKF2 function from the Crypto.protocol module to derive a strong key from the two input values
    key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512) #(mp, ds, length_key, nrRoundsforAESstrengthening, hashFunctionSpecification)
    return key

def checkEntry(sitename, siteurl, email, username):
    db = dbconfig()
    cursor = db.cursor()
    query = f"SELECT * FROM PROtect.entries where sitename = '{sitename}' and siteurl = '{siteurl}' AND email = '{email}' AND username = '{username}'"
    cursor.execute(query)
    results = cursor.fetchall()

    if len(results)!=0:
        return True
    return False


def addEntry(mp, ds, sitename, siteurl, email, username): 
    #get the password
    password = getpass("Password: ")

    mk = computeMasterKey(mp,ds): #mk stands for masterKey

    #using imported aesutil function to encrypt the mk 
    #this should return the encrypted password in base 64 encoded format
    encrypted = AES256util.encrypt(key=mk, source=password, keyType="bytes")

    #add the new password to the database
    db = dbconfig()
    cursor = db.cursor()
    query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values (%s, %s, %s, %s, %s)"
    val = (sitename.siteurl,email.username.encrypted)
    cursor.execute(query, val)
    db.commit()

    printc("[green][+][/green] Added entry ")
