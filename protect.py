import tkinter as tk
from ttkbootstrap import Style
from ui.CONTROLLER.Logincontroller import Logincontroller
from ui.CONTROLLER.GUIcontroller import PasswordManagerController
import sys

def start_main_app(root, username:str, mp:str, ds:str):
    #launch PasswordManagerController for the authenticated users
    #Pass the entered master password so the controller can compute the master key
    for w in root.winfo_children():
        w.destroy() #ensures clean state
    PasswordManagerController(username=username, mp=mp, ds=ds)

if __name__ == "__main__":
    testmode = "--test" in sys.argv #optional testmode to skip login

    root = tk.Tk()
    root.title("PROtect Password Manager")
    root.geometry("1000x700")
    style = Style(theme="vapor") #applies ttk theme globally

    if testmode:
        #skips login and launches password manager directly with a test user
        PasswordManagerController(username="testuser", mp="password", ds="TEST_DEVICE_SECRET")
    else:
        Logincontroller(root, on_success=lambda r,u,p,d: start_main_app(r,u,p,d))
    root.mainloop()

