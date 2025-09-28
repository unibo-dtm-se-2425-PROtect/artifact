import tkinter as tk
from ttkbootstrap import Style
from ui.CONTROLLER.Logincontroller import LoginController
from ui.CONTROLLER.GUIcontroller import PasswordManagerController
import sys

def start_main_app(root, username:str, master_password:str):
    #launch PasswordManagerController for the authenticated users
    #Pass the entered master password so the controller can compute the master key
    for w in root.winfo_children():
        w.destroy() #ensures clean state
    PasswordManagerController(master_password=master_password)

if __name__ == "__main__":
    testmode = "--test" in sys.argv #optional testmode to skip login

    root = tk.Tk()
    root.title("PROtect Password Manager")
    root.geometry("1000x700")
    style = Style(theme="vapor") #applies ttk theme globally

    if testmode:
        #skips login and launches password manager directly with a test user
        PasswordManagerController(master_password="password")
    else:
        LoginController(root, on_success=lambda r,u,p: start_main_app(r,u,p))
    root.mainloop()

