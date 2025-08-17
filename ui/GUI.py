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

class PromptPassword(tb.Toplevel):
    def __init__(self, master, prompt="Master password"):
        super().__init__(master)
        self.title("Confirm")
        self.value = None
        frm = tb.Frame(self, padding=15)
        frm.pack(fill=BOTH, expand=True)
        tb.Label(frm, text=prompt).pack(anchor=W)
        self.ent = tb.Entry(frm, show='•', width=32)
        self.ent.pack(pady=6)
        self.ent.focus_set()
        btns = tb.Frame(frm)
        btns.pack(anchor=E)
        tb.Button(btns, text="OK", bootstyle=PRIMARY, command=self.ok).pack(side=LEFT, padx=4)
        tb.Button(btns, text="Cancel", command=self.destroy).pack(side=LEFT)
        self.bind('<Return>', lambda e: self.ok())

    def ok(self):
        self.value = self.ent.get()
        self.destroy()

    def on_ok(self):
        self.value = self.entry.get()
        self.destroy()

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
    
    def after_setup(self, ok:bool):
        if ok:
            self.schema=detect_schema()
            messagebox.showinfo("SetUp", "Configuration completed.")
    
    def try_login(self):
        if not self.schema:
            messagebox.showerror("Error", "Please run setup first")
            return
        mp=self.pw.get()
        ok, ds=verify_master(self.schema, mp)
        if ok:
            self.on_success(self.schema, mp, ds)
        else:
            messagebox.showerror("Error", "Wrong master password.")

class EditDialog(tb.Toplevel):
    def __init__(self, master, title="Edit Entry", initial:Optional[Tuple]=None):
        super().__init__(master)
        self.title(title)
        self.result=None
        frm=tb.Frame(self, padding=15)
        frm.pack(fill=BOTH, expand=True)

        self.sitename=tb.Entry(frm, width=40)
        self.siteurl=tb.Entry(frm, width=40)
        self.email=tb.Entry(frm, width=40)
        self.username=tb.Entry(frm, width=40)
        self.password=tb.Entry(frm, width=40)

        def row(lbl, widget):
            r=tb.Frame(frm)
            r.pack(fill=X, pady=4)
            tb.Label(r, text=lbl, width=14, anchor=E).pack(side=LEFT)
            widget.pack(side=LEFT, fill=X, expand=True)
        
        row("Site Name", self.sitename)
        row("Site URL", self.siteurl)
        row("Email", self.email)
        row("Username", self.username)
        row("Password", self.password)
        tb.Label(frm, text="(leave password blank to keep the existing one)", bootstyle=INFO).pack(anchor=W, pady=(0,8))

        btns=tb.Frame(frm)
        btns.pack(anchor=E)
        tb.Button(btns, text="Save", bootstyle=SUCCESS, command=self.ok).pack(side=LEFT, padx=4)
        tb.Button(btns, text="Cancel", command=self.destroy).pack(side=LEFT)

        if initial:
            self.sitename.insert(0, initial[0])
            self.siteurl.insert(0, initial[1])
            self.email.insert(0, initial[2])
            self.username.insert(0, initial[3])
            #don't prefill password

        self.sitename.focus_set()
        self.bind('<Return>', lambda e: self.ok())

    def ok(self):
        site=self.sitename.get().strip()
        url=self.siteurl.get().strip()
        email=self.email.get().strip()
        user=self.username.get().strip()
        password=self.password.get()
        if not site or not url or not user:
            messagebox.showerror("Validation Error", "Site, URL and Username are required.")
            return
        self.result=(site, url, email, user, password)
        self.destroy() 



class MainFrame(tb.Frame):
    def __init__(self, master, schema:str, mp:str, ds:str, on_lock):
        super().__init__(master, padding=15)
        self.schema, self.mp, self.ds = schema, mp, ds
        self.on_lock=on_lock

        header=tb.Frame(self)
        header.pack(fill=X)
        tb.Label(header, text="Password Manager", font=("Helvetica", 18)).pack(side=LEFT)
        tb.Button(header, text="Lock", bootstyle=DANGER, command=self.lock).pack(side=RIGHT, padx=5)
        tb.Button(header, text="Export", command=self.do_export).pack(side=RIGHT, padx=5)
        tb.Button(header, text="Import", command=self.do_import).pack(side=RIGHT, padx=5)
        
        #Toolbar
        bar=tb.Frame(self)
        bar.pack(fill=X, pady=8)
        tb.Button(bar, text="Add", bootstyle=SUCCESS, command=self.add_entry).pack(side=LEFT, padx=4)
        tb.Button(bar, text="Edit", command=self.edit_entry).pack(side=LEFT, padx=4)
        tb.Button(bar, text="Delete", bootstyle=DANGER, command=self.delete_entry).pack(side=LEFT, padx=4)
        tb.Separator(bar, orient=VERTICAL).pack(side=LEFT, fill=Y, padx=8)
        tb.Button(bar, text="Copy", command=self.copy_password).pack(side=LEFT, padx=4)
        tb.Button(bar, text="Show (10s)", bootstyle=WARNING, command=self.show_password).pack(side=LEFT, padx=4)
        tb.Separator(bar, orient=VERTICAL).pack(side=LEFT, fill=Y, padx=8)
        tb.Button(bar, text="Generate", command=self.generate_password).pack(side=LEFT, padx=4)

        #Table
        cols=("site", "URL", "Email", "Username")
        self.tree=tb.Treeview(self, columns=cols, show="headings", height=14, bootstyle=INFO)
        for c in cols:
            self.tree.heading(c, text=c)
            self.tree.column(c, width=180 if c=="URL" else 140)
        self.tree.pack(fill=BOTH, expand=True)
        self.tree.bind('<Double-1>', lambda e: self.copy_password())

        self._rows_cache=[]     # parallels tree items; holds full tuples including encrypted password
        self.refresh()

    def lock(self):
        if messagebox.askyesno("Lock", "Do you want to lock the vault?"):
            self.on_lock()
    
    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self._rows_cache=list_entries(self.schema)
        for r in self._rows_cache:
            self.tree.insert('', 'end', values=r[:4])
    
    def selected_row(self) -> Optional[Tuple]:
        sel=self.tree.selection()
        if not sel:
            messagebox.showinfo("Select", "Please select a row.")
            return None
        idx=self.tree.index(sel[0])
        return self._rows_cache[idx]
    
    def require_master(self, prompt="Confirm master password") -> bool:
        d=PromptPassword(self, prompt)
        self.wait_window(d)
        if not d.value:
            return False
        ok, _=verify_master(self.schema, d.value)
        if not ok:
            messagebox.showerror("Error", "Wrong Master Password.")
            return False
        return True
    
    def add_entry(self):
        if not self.require_master("Enter master password to add"):
            return
        d=EditDialog(self, title="Add Entry")
        self.wait_window(d)
        if d.result:
            site,url,email,user,password=d.result
            try:
                insert_entry(self.schema, self.mp, self.ds, site,url,email,user,password)
                self.refresh()
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))
    
    def edit_entry(self):
        row=self.selected_row()
        if not row:
            return
        if not self.require_master("Master Password to edit"):
            return
        d=EditDialog(self, title="Edit Entry", initial=row)
        self.wait_window(d)
        if d.result:
            site,url,email,user,password=d.result
            nplain=None if (p=='' or p is None) else p
            try:
                update_entry(self.schema, row, (site,url,email,user,nplain), self.mp, self.ds)
                self.refresh()
            except Exception as ex:
                messagebox.showerror("DB Error", str(ex))
    
    def delete_entry(self):
        row=self.selected_row()
        if not row:
            return
        if not self.require_master("Master Password to delete"):
            return
        if not messagebox.askyesno("Delete", f"Delete entry for {row[0]}?"):
            return
        try:
            delete_entry(self.schema, row)
            self.refresh()
        except Exception as ex:
            messagebox.showerror("DB Error", str(ex))
    
    def copy_password(self):
        if pyperclip is None: 
            messagebox.showwarning("clipboard", "pyperclip not installed.")
            return
        row=self.selected_row()
        if not row:
            return
        if not self.require_master("Master Password to correctly copy."):
            return
        try:
            mk=computeMasterKey(self.mp, self.ds)
            dec=project.AES256util.decrypt(key=mk, source=row[4], keyType='bytes')
            pyperclip.copy(dec.decode())
            messagebox.showinfo("copied", "Password copied to clipboard.")
        except Exception as ex: 
            messagebox.showerror("Decrypt Error", str(ex))
    
    def show_password(self):
        row=self.selected_row()
        if not row:
            return
        if not self.require_master("Master Password to show user's password."):
            return
        try:
            mk=computeMasterKey(self.mp, self.ds)
            dec=project.AES256util.decrypt(key=mk, source=row[4], keyType='bytes').decode()
        except Exception as ex:
            messagebox.showerror("Decrypt Error", str(ex))
            return
        RevealDialog(self, dec)
    
    def generate_password(self): 
        GenDialog(self)

    def do_export(self):
        path=filedialog.asksaveasfilename(defaultextension='.json', filetypes=[("Json","*.json")])
        if not path:
            return
        try:
            export_json(self.schema, path)
            messagebox.showinfo("Export", f"Exported to {path}")
        except Exception as ex:
            messagebox.showerror("Export Error", str(ex))
        
    def do_import(self):
        path=filedialog.askopenfilename(filetypes=[('JSON', '*.json')])
        if not path:
            return
        if not messagebox.askyesno("Import", "Importing will add entries to your vault. Continue?"):
            return
        try:
            import_json(self.schema, path)
            self.refresh()
        except Exception as ex:
            messagebox.showerror("Import Error", str(ex))
    