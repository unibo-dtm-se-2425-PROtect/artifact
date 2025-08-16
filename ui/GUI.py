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
