#Tkinter + ttkbootstrap (theme='vapor')
#Features:
  # -Login with Master Password (required on app open)
  # -Optional re-lock
  # -List entries in table (password never shown by default)
  # -Copy to clipboard (no on-screen reveal)
  # -Show Password (requires master password again) with 10s auto-hide
  # -Add, Edit, Delete entries (each requires master password confirmation)
  # -Generate password tool (length slider) + copy
  # -First-time Setup (GUI wrapper for config): create DB/tables + set master password
  # -Import/Export JSON (optional convenience)

from __future__ import allocations
import json
import os
import sys
import threading
import time
from dataclasses import asdict, dataclass
from typing import List, Optional, Tuple

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import StringVar, IntVar

import ttkbootstrap as tb
from ttkbootstrap.constants import *

#back-end imports for the project
try:
    from project.dbconfig import dbconfig
except Exception as e: 
    raise SystemExit("dbconfig.py not found or import error: " +str(e))

try: 
    from project.add import computeMasterKey
except Exception:
    #useful whether the user has not imported its own add.py which includes the PBKDF2 implementation 
    # so we use a local one directly imported from PyCryptodome
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Hash import SHA256
    def computeMasterKey(mp, ds):
        return PBKDF2(mp.encode(), ds.encode(), 32, count=1_000_000, hmac_hash_module=SHA256)
    
try:
    import project.AES256util
except Exception as e:
    raise SystemExit("AES256util.py not found or import error: " + str(e))

try: 
    import project.generate
except Exception:
    import random, string
    def generatePassword(n):
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for num in range(n))
    generate = type('G', (), {'generatePassword': staticmethod(generatePassword)})

try:
    import pyperclip
except Exception:
    pyperclip=None

#DATABASE HELPERS: bridge between GUI and underlying db so that the user does not need to manage SQL queries directly
def get_db():
    db=dbconfig()
    if db is None:
        raise RuntimeError("Unable to connect to database. Check dbconfig.py and DB server")
    return db

SCHEMA_CANDIDATES = ["PROtect", "pm"]

def detect_schema() -> Optional[str]:
    db=get_db()
    cur=db.cursor()
    for s in SCHEMA_CANDIDATES:
        cur.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s", (s,))
        if cur.fetchall():
            db.close()
            return s 
        db.close()
        return None
    
def read_secrets(schema_str) -> Tuple[str, str]:
    #Return (master_hash, device_secret)
    db=get_db()
    cur=db.cursor()
    cur.execute(f"SELECT * FROM {schema}.secrets")
    row=cur.fetchall()
    db.close()
    if not row:
        raise RuntimeError("Secrets table empty. Run configuration")
    #expect order: masterpassword_hash, device_secret
    r= row[0]
    master_hash, device_secret = r[0], r[1]
    return master_hash, device_secret

def verify_master(schema: str, mp: str) -> Tuple[bool, Optional[str]]:
    import hashlib
    try:
        master_hash, device_secret = read_secrets(schema)
    except Exception as e:
        return False, None
    hashed=hashlib.sha256(mp.encode()).hexdigest()
    return(hashed==master_hash, device_secret if hashed==master_hash else None)

def list_entries(schema:str):
    db=get_db()
    cur=db.cursor()
    cur.execute(f"SELECT sitename, siteurl, email, username, password FROM {schema}.entries")
    rows=cur.fetchall()
    db.close()
    return rows

def insert_entry(schema:str, mp:str, ds:str, sitename:str, siteurl:str, email:str, username:str, password_plain:str):
    mk=computeMasterKey(mp,ds)
    enc=project.AES256util.encrypt(key=mk, source=password_plain, keyType='bytes')
    db=get_db()
    cur=db.cursor()
    cur.execute(
        f"INSERT INTO {schema}.entries (sitename, siteurl, email, username, password) VALUES (%s,%s,%s,%s,%s)",
        (sitename, siteurl, email, username, enc),
    )
    db.commit()
    db.close()

def delete_entry(schema:str, row):
    db=get_db()
    cur=db.cursor()
    cur.execute(
        f"DELETE FROM {schema}.entries WHERE sitename=%s AND siteurl=%s AND email=%s AND username=%s AND password=%s LIMIT 1",
        row,
    )
    db.commit()
    db.close()

def update_entry(schema:str, old_row, new_values, mp:str, ds:str):
    ns, nu, ne, nl, nplain = new_values
    if nplain is None: 
        nenc=old_row[]
    else: 
        mk=computeMasterKey(mp, ds)
        nenc=project.AES256util.encrypt(key=mk, source=nplain, keyType='bytes')
    db=get_db()
    cur=db.cursor()
    cur.execute(
        f"UPDATE {schema}.entries SET sitename=%s, siteurl=%s, email=%s, username=%s, password=%s "
        f"WHERE sitename=%s AND siteurl=%s AND email=%s AND username=%s AND password=%s LIMIT 1",
        (ns, nu, ne, nl, nenc, old_row),
    )
    db.commit()
    db.close()

def export_json(schema:str, path:str):
    rows=list_entries(schema)
    data=[
        {"sitename": r[0], "siteurl": r[1], "email": r[2], "username": r[3], "password": r[4]} for r in rows
    ]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def import_json(schema:str, path:str):
    with open(path, 'r', encoding='utf-8') as f:
        data=json.load(f)
    db=get_db()
    cur=db.cursor()
    for r in data:
        cur.execute(
            f"INSERT INTO {schema}.entries (sitename, siteurl, email, username, password) VALUES (%s,%s,%s,%s,%s)",
            (r['sitename'], r['siteurl'], r.get('email', ''), r.get('username', ''), r['password'])
        )
        db.commit()
        db.close()

#GUI visual set up

class SetupDialog(tb.Toplevel):
    def __init__(self, master, on_done=None):
        super().__init__(master)
        self.on_done = on_done

class Loginframe(tb.Frame):
    def __init__(self, master, on_succes):
        super().__init__(master, padding=30)
        self.on_success=on_succes
        tb.Label(self, text="Unlock Vault", font=("Helvetica",20)).pack(pady=(0,15))

        self.schema=detect_schema()
        if not self.schema:
            tb.Label(self, text="No vault found.", bootstyle=WARNING).pack(pady=(0,5))
            tb.Button(self, text="Run First-Time SetUp", bootstyle=SUCCESS, command=self.open_setup).pack(pady=(0,20))
        else:
            tb.Label(self, text=f"Using schema: {self.schema}").pack(pady=(0,10))
    
        self.pw=tb.Entry(self, show="•", width=30)
        self.pw.pack()
        self.pw.focus_set()
        tb.Button(self, text="Unlock", bootstyle=PRIMARY, command=self.try_login).pack(pady=12)

        tb.Button(self, text="Configure...", command=self.open_setup).pack()

        self.blind_all('<Return>', lambda e: self.try_login())
    
    def open_setup(self):
        SetupDialog(self, on_done=self.after_setup)
    

