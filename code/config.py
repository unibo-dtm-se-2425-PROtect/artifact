import os
from getpass import getpass
import string
import random
import hashlib

from dbconfig import dbconfig 

from rich import print as printc 
from rich.console import Console

console = Console()

def checkConfig(): 
    db = dbconfig()
    cursor = db.cursor()
    query = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA  WHERE SCHEMA_NAME = 'PROtect'"
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    if len(results)!=0:
        return True
    return False

def generateDeviceSecret(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

def config():
    #Create a Database
    db=dbconfig() 
    cursor=db.cursor()
    try: 
        cursor.execute("CREATE DATABASE PROtect")
    except Exception as e: 
        printc("[red][!] An error occurred while trying to create db")
        console.print_exception(show_locals=True)
    printc("[green][+][/green] Database 'PROtect' created")

    #create tables
    query = "CREATE TABLE PROtect.secrets (masterpassword_hash TEXT NOT NULL, device_secret TEXT NOT NULL)" 
    res = cursor.execute(query) 
    printc("[green][+][/green] Table 'secrets' created")

    query = "CREATE TABLE PROtect.entries (sitename TEXT NOT NULL, siteurl TEXT NOT NULL, email TEXT, username TEXT, password TEXT NOT NULL)" 
    res = cursor.execute(query) 
    printc("[green][+][/green] Table 'entries' created")

    mp=""
    while 1:
        mp=getpass("Choose a MASTER PASSWORD: ")
        if mp==getpass("Write the password again: ") and mp!="":
            break
        printc("[yellow][-] Please try again [/yellow]") 

    #Hash the MASTER PASSWORD
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
    printc("[green][+][/green] Generated hash of the Master Password")

    #Generation of DEVICE SECRET
    ds = generateDeviceSecret()
    printc("[green][+][/green] Device Secret generated")

    #Add values into the database in the secrets table
    query = "INSERT INTO PROtect.secrets (masterpassword_hash, device_secret) values (?, ?)"
    val = (hashed_mp, ds)
    cursor.execute(query, val) 
    PROtect.commit()
    printc("[green][+][/green] Added to the database PROtect")
    printc("[green][+] Configuration completed! [/green]")

    PROtect.close()

config()
