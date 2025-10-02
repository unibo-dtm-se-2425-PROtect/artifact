#!/usr/bin/env python

import argparse
from getpass import getpass
import hashlib
import pyperclip

from rich import print as printc

import add
import string
import retrieve
from dbconfig import dbconfig

parser = argparse.ArgumentParser(description='Password Manager CLI')

parser.add_argument('option', help='(a)dd / (e)xtract') #those are the type of operation that the user is able to perform
parser.add_argument("-s", "--name", help="Site name")
parser.add_argument("-u", "--url", help="Site URL")
parser.add_argument("-e", "--email", help="Email")
parser.add_argument("-l", "--login", help="Username")
parser.add_argument("-c", "--copy", action='store_true', help='Copy password to clipboard')


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
	query = "SELECT * FROM pm.secrets"
	cursor.execute(query)
	result = cursor.fetchall()[0]
	if hashed_mp != result[0]:
		printc("[red][!] WRONG! [/red]")
		return None

	return [mp,result[1]]


def main():
	if args.option in ["add","a"]:
		if args.name == None or args.url == None or args.login == None:
			if args.name == None:
				printc("[red][!][/red] Site Name (-s) required ")
			if args.url == None:
				printc("[red][!][/red] Site URL (-u) required ")
			if args.login == None:
				printc("[red][!][/red] Site Username (-l) required ")
			return

		if args.email == None:
			args.email = ""

		res = inputAndValidateMasterPassword()
		if res is not None:
			add.addEntry(res[0],res[1],args.name,args.url,args.email,args.login)


	if args.option in ["extract","e"]:
		# if args.name == None and args.url == None and args.email == None and args.login == None:
		# 	# retrieve all
		# 	printc("[red][!][/red] Please enter at least one search field (sitename/url/email/username)")
		# 	return
		res = inputAndValidateMasterPassword()

		search = {}
		if args.name is not None:
			search["sitename"] = args.name
		if args.url is not None:
			search["siteurl"] = args.url
		if args.email is not None:
			search["email"] = args.email
		if args.login is not None:
			search["username"] = args.login

		if res is not None:
			retrieve.retrieveEntries(res[0],res[1],search,decryptPassword = args.copy)



main()
