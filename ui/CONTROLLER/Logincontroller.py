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
    