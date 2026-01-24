from tkinter import messagebox
from ui.VIEW.Loginview import Loginview
from ui.MODEL.Loginmodel import LoginModel
from project.add import computeMasterKey
from project.AES256util import verify_master_password
import os
import hashlib

class Logincontroller:
    #Expects the on_success callback signature: on_success(root, username, master_password)
    def __init__(self, root, on_success):
        self.root = root
        self.on_success = on_success
        #we use a LoginModel to access the secrets table for authentication
        self.model = LoginModel()
        self.view = Loginview(root, on_login=self.verify_login, on_signup=self.try_signup)
        self.view.pack(expand=True, fill="both")
    
    def verify_login(self, username: str, password: str): #the ds is fetched inside 
        #Verify username + master password against the stored derived key.
        row = self.model.get_user_secrets(username)
        if not row: #No such user
            res = messagebox.askyesno("User not found", f"User '{username}' not found. Do you want to create a new account?")
            if res:
                self.try_signup(username, password)
            else:
                self.view.clear_password()
            return

        #Compares the entered password hash with the stored hash
        mp_ds_pair=verify_master_password(username, password)
        if mp_ds_pair:
            #Success
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
            mp, ds=mp_ds_pair
            self.model.close()
            self.view.pack_forget()
            self.view.destroy()
            #pass the plain mp and ds
            self.on_success(self.root, username, mp, ds)
        else:
            #console error showed by the GUI, too
            messagebox.showerror("Authentication failed", "Invalid master password.")
            self.view.clear_password()

    def try_signup(self, username: str, password: str):
        #Check if user exists already
        if self.model.get_user_secrets(username):
            messagebox.showinfo("Exists", f"User '{username}' already exists. Please login instead.")
            self.view.clear_password()
            return

        #Generate salt (hex) and derive key
        salt = os.urandom(16).hex()
        mp_hash=hashlib.sha256(password.encode()).hexdigest()

        #Insert new user into secrets table
        try:
            self.model.create_new_user(username, mp_hash, salt)
        except Exception as e:
            messagebox.showerror("Error", f"Unable to create user: {e}")
            return

        messagebox.showinfo("Account created", f"User '{username}' created. You can now login.")
        #Immediately log in
        self.verify_login(username, password)