#!/usr/bin/env python

import argparse
from getpass import getpass
import hashlib
import string
import sys

from rich import print as printc

from project import add
from project.config import config, delete, reconfig
from project import retrieve
from project.dbconfig import dbconfig
from project.delete import delete_entry
from project.modify import modify_entry
from project.export import export_entries
from project.importf import import_entries


def get_args():
    parser = argparse.ArgumentParser(description='Password Manager CLI')
    
    parser.add_argument('option', help='(a)dd / (e)xtract / (con)figure / (del)ete configuration / (recon)figure / (imp)ort / (exp)ort / (mod)ify / (rem)ove an entry by ID') 
    parser.add_argument("-s", "--name", help="Site Name")
    parser.add_argument("-u", "--url", help="Site URL")
    parser.add_argument("-e", "--email", help="Email")
    parser.add_argument("-l", "--login", help="Username")
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("--length", help="Length of the password to generate", type=int)
    parser.add_argument("-c", "--copy", action='store_true', help='Copy password to clipboard')
    parser.add_argument("--all", action="store_true", help="Retrieve all stored entries (not the default, it must be specified for conscious choice)" )
    parser.add_argument("--id", help="ID of the entry to modify/delete (for 'modify' and 'delete' options)")
    parser.add_argument("-f", "--file", help="path to file to 'import' or 'export' operations")
    
    return parser.parse_args()

def inputAndValidateMasterPassword():
    mp = getpass("MASTER PASSWORD: ")
    #Password policy checks
    if len(mp) < 8:
        printc("[red][!] Password must be at least 8 characters long.[/red]")
        return None
    if not any(c.isupper() for c in mp):
        printc("[red][!] Password must contain at least one uppercase letter.[/red]")
        return None
    if not any(c.isdigit() for c in mp):
        printc("[red][!] Password must contain at least one number.[/red]")
        return None
    if not any(c in string.punctuation for c in mp):
        printc("[red][!] Password must contain at least one special character.[/red]")
        return None
    
    # If all policies are observed
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()

    db = dbconfig()
    cursor = db.cursor()
    query = "SELECT * FROM PROtect.secrets"
    cursor.execute(query)
    results = cursor.fetchall()
    
    if not results:
        printc("[red][!] Database not configured! Run 'pm.py con' first.[/red]")
        db.close()
        return None

    result = results[0]
    db.close()

    #remember the schema being: 0=ID, 1=username, 2=masterpassword_hash, 3=device_secret
    if hashed_mp != result[2]:
        printc("[red][!] WRONG! [/red]")
        return None

    #retrieve the deviceSecret, at index 3, which is needed for AES encryption/decryption
    return [mp, result[3]]


def main():
    args = get_args()
    if args.option in ["add", "a"]:
        missing = []
        if args.name is None:
            missing.append("Site Name (-s)")
        if args.login is None:
            missing.append("Username (-l)")
        if args.password is None:
            missing.append("Password (-p)")
        if missing:
            for m in missing:
                printc(f"[red][!][/red] {m} is required!")
            return

        #optional field
        if args.email is None:
            args.email = ""
        if args.url is None:
            args.url = ""
        
        res = inputAndValidateMasterPassword()
        if res is not None:
            add.addEntry(res[0], res[1], args.name, args.url, args.email, args.login, args.password)


    elif args.option in ["extract", "e"]:
        res = inputAndValidateMasterPassword()
        if res is None: 
            return
        
        search = {}
        if not args.all:
            if args.name is not None:
                search["Site"] = args.name
            if args.url is not None:
                search["URL"] = args.url
            if args.email is not None:
                search["Email"] = args.email
            if args.login is not None:
                search["Username"] = args.login
        
        #if no fields provided and --all not used, show warning
        if len(search) == 0 and not args.all:
            printc("[red][!][/red] Please enter at least one search field (Site/URL/Email/Username) or use --all")
            return
        
        #if --all is used, search[] stays empty to retrieve all entries 
        retrieve.retrieveEntries(res[0], res[1], search, decryptPassword=args.copy)

    elif args.option in ["remove", "rem"]:
        res = inputAndValidateMasterPassword()
        if res is not None:
            if args.id is None:
                printc("[red][!][/red] Entry ID (--id) is required for deletion!")
                return
            delete_entry(args.id) #delete_entry is fixed to take only ID
    
    elif args.option in ["modify", "mod"]:
        res = inputAndValidateMasterPassword()
        if res is not None:
            if args.id is None: 
                printc("[red][!][/red] Entry ID (--id) is required for modification!")
                return
            modify_entry(args.id, res[0], res[1]) 

    elif args.option in ["import", "imp"]:
        res = inputAndValidateMasterPassword()
        if res is not None:
            if args.file is None:
                printc("[red][!][/red] File path (-f/--file) is required for import!")
                return
            import_entries(args.file, res[0], res[1])
    
    elif args.option in ["export", "exp"]:
        res = inputAndValidateMasterPassword()
        if res is not None:
            if args.file is None:
                printc("[red][!][/red] File path (-f/--file) is required for export!")
                return
            export_entries(args.file, res[0], res[1])
    
    elif args.option in ["configure", "con"]:
        config()
    elif args.option in ["delete configuration", "del"]:
        delete()
    elif args.option in ["reconfigure", "recon"]:
        reconfig()

if __name__ == "__main__":
    main()
