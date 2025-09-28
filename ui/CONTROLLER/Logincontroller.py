import tkinter as tk
from tkinter import messagebox
from ui.VIEW.Loginview import LoginView
from ui.MODEL.GUImodel import PasswordManagerModel
from project.add import computeMasterKey
import os

class Logincontroller:
    #Expects the on_success callback signature: on_success(root, username, master_password)
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        #we use a model instance to access the secrets table for authentication
        self.model = PasswordManagerModel()
        self.view = LoginView(root, on_login=self.verify_login, on_signup=self.try_signup)
        self.view.pack(expand=True, fill="both")
    
    def verify_login(self, username: str, password: str):
        #Verify username + master password against the stored derived key (PBKDF2 result stored as hex).
        cur = self.model.cursor
        # Query secrets for this username
        cur.execute("SELECT mp, ds FROM PROtect.secrets WHERE mp_username=%s" if self._secrets_has_username_col() else "SELECT mp, ds FROM PROtect.secrets WHERE mp=%s", (username,))
        row = cur.fetchone()
        if not row: #No such user
            res = messagebox.askyesno("User not found", f"User '{username}' not found. Do you want to create a new account?")
            if res:
                self.try_signup(username, password)
            else:
                self.view.clear_password()
            return

        #Depending on the secrets table layout, mp may store derived_key_hex and ds the salt (we'll try to be flexible)
        stored_mp, stored_ds = row  #stored_mp: derived_key_hex or username

        #If the secrets table uses columns differently, we assume stored_ds is the salt.
        salt = stored_ds if stored_ds else ""
        # Compute derived key from entered password and salt
        derived = computeMasterKey(password, salt)
        derived_hex = derived.hex() if isinstance(derived, (bytes, bytearray)) else str(derived)

        # Compare with stored_mp
        if stored_mp and derived_hex == stored_mp:
            # Success
            self.view.pack_forget()
            self.view.destroy()
            # Pass username and password to on_success so main app can compute masterkey etc.
            self.on_success(self.root, username, password)
        else:
            messagebox.showerror("Authentication failed", "Invalid master password.")
            self.view.clear_password()

    def try_signup(self, username: str, password: str):
        #Create new user in secrets table: generate random salt, 
        #compute derived key with computeMasterKey(password, salt), 
        #store derived_key_hex and salt along with username in secrets table
        cur = self.model.cursor

        # Check if user exists already
        cur.execute("SELECT mp FROM PROtect.secrets WHERE mp_username=%s" if self._secrets_has_username_col() else "SELECT mp FROM PROtect.secrets WHERE mp=%s", (username,))
        if cur.fetchone():
            messagebox.showinfo("Exists", f"User '{username}' already exists. Please login instead.")
            self.view.clear_password()
            return

        # Generate salt (hex) and derive key
        salt = os.urandom(16).hex()
        derived = computeMasterKey(password, salt)
        derived_hex = derived.hex() if isinstance(derived, (bytes, bytearray)) else str(derived)

        #Try to insert into secrets table. We'll attempt to insert columns (username, mp, ds) if available,
        #otherwise fall back to (mp, ds) and store derived_key in mp and salt in ds.
        try:
            # prefer storing username explicitly if table has that column
            if self._secrets_has_username_col():
                cur.execute("INSERT INTO PROtect.secrets (username, mp, ds) VALUES (%s,%s,%s)", (username, derived_hex, salt))
            else:
                cur.execute("INSERT INTO PROtect.secrets (mp, ds) VALUES (%s,%s)", (derived_hex, salt))
            self.model.db.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Unable to create user: {e}")
            return

        messagebox.showinfo("Account created", f"User '{username}' created. You can now login.")
        # Immediately log in
        self.verify_login(username, password)

    