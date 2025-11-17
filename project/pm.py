#!/usr/bin/env python

import argparse
from getpass import getpass
import hashlib

from rich import print as printc

import add
from config import config, delete, reconfig
import string
import retrieve
from dbconfig import dbconfig
from delete import delete_entry
from modify import modify_entry
from export import export_entries
from importf import import_entries


parser = argparse.ArgumentParser(description='Password Manager CLI')

parser.add_argument('option', help='(a)dd / (e)xtract / (con)figure / (del)ete / (recon)figure / (imp)ort / (exp)ort / (mod)ify') #these are the type of operation that the user is able to perform
parser.add_argument("-s", "--name", help="Site name")
parser.add_argument("-u", "--url", help="Site URL")
parser.add_argument("-e", "--email", help="Email")
parser.add_argument("-l", "--login", help="Username")
parser.add_argument("--length", help="Length of the password to generate",type=int)
parser.add_argument("-c", "--copy", action='store_true', help='Copy password to clipboard')
parser.add_argument("--all", action="store_true", help="Retrieve all stored entries (not the default, it must be specified for conscious choice)" )
parser.add_argument("--id", help="ID of the entry to modify/delete (for 'modify' and 'delete' options)")
parser.add_argument("--f", "--file", help="path to file to 'import' or 'export' operations")
args = parser.parse_args()


def inputAndValidateMasterPassword():
	mp = getpass("MASTER PASSWORD: ")
	#Password policy checks
	if len(mp)<8:
		print("[!] Password must be at least 8 characters long.")
		return None
	if not any(c.isupper() for c in mp):
		print("[!] Password must contain at least one uppercase letter.")
		return None
	if not any(c.isdigit() for c in mp):
		print("[!] Password must contain at least one number.")
		return None
	if not any(c in string.punctuation for c in mp):
		print("[!] Password must contain at least one special character.")
		return None
	
	#If all policies are observed
	hashed_mp = hashlib.sha256(mp.encode()).hexdigest()

	db = dbconfig()
	cursor = db.cursor()
	query = "SELECT * FROM PROtect.secrets"
	cursor.execute(query)
	result = cursor.fetchall()[0]
	if hashed_mp != result[0]:
		printc("[red][!] WRONG! [/red]")
		return None

	return [mp,result[1]]


def main():
	if args.option in ["add","a"]:
		missing=[]
		if args.name == None:
			missing.append("Site Name (-s)")
		if args.url == None:
			missing.append("Site URL (-u)")
		if args.login == None:
			missing.append("Site Username (-l)")
		if missing:
			for m in missing:
				printc(f"[red][!][/red] {m} is required!")
        #optional field
		if args.email == None:
			args.email = ""

		res = inputAndValidateMasterPassword()
		if res is not None:
			add.addEntry(res[0],res[1],args.name,args.url,args.email,args.login)


	elif args.option in ["extract","e"]:
		res = inputAndValidateMasterPassword()
		if res is None: 
			return
        
		search={}
		if not args.all:
			if args.name is not None:
				search["Site"] = args.name
			if args.url is not None:
				search["URL"] = args.url
			if args.email is not None:
				search["Email"] = args.email
			if args.login is not None:
				search ["Username"] = args.login
		
		#if no fields provided and --all not used, show warning
		if len(search) == 0:
			printc("[red][!][/red] Please enter at least one search field (Site/URL/Email/Username) or use --all")
			return
		
		#if --all is used, search[] stays empty to retrieve all entries 
		retrieve.retrieveEntries(res[0], res[1], search, decryptPassword=args.copy)

	elif args.option in ["delete", "del"]:
		res=inputAndValidateMasterPassword()
		if res is not None:
			if args.id is None:
				printc("[red][!][/red] Entry ID (--id) is required for deletion!")
				return
			delete_entry(args.id, res[0], res[1]) #mp and ds
	
	elif args.option in ["modify", "mod"]:
		pass

	elif args.option in ["import", "imp"]:
		res=inputAndValidateMasterPassword()
		if res is not None:
			if args.file is None:
				printc("[red][!][/red] File path (-f/--file) is required for import!")
				return
			import_entries(args.file, res[0], res[1])
	
	elif args.option in ["export", "exp"]:
		res=inputAndValidateMasterPassword()
		if res is not None:
			if args.file is None:
				printc("[red][!][/red] File path (-f/--file) is required for export!")
				return
			export_entries(args.file, res[0], res[1])
    
	elif args.option in ["configure", "con"]:
		config()
	elif args.option in ["delete", "del"]:
		delete()
	elif args.option in ["reconfigure", "recon"]:
		reconfig()

main()
