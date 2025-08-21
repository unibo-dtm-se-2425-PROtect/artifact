from ui.VIEW.GUIview import PasswordManagerView
from typing import List, Tuple, Optional
from ui.MODEL.GUImodel import PasswordManagerModel
import tkinter as tk
from threading import Timer
from tkinter import simpledialog, filedialog
from project.add import computeMasterKey

class PasswordManagerController:
    def __init__(self, root, master_password=str):
        self.root=root
        self.model=PasswordManagerModel()
        self.masterkey=computeMasterKey(master_password)

        #Bind view callbacks to controller methods
        self.view=PasswordManagerView(
            root,
            on_add=self.add_entry,
            on_edit=self.edit_entry,
            on_delete=self.delete_entry,
            on_copy=self.copy,
            on_generate=self.generate_password,
            on_show=self.show_message,
            on_export=self.export_to_file,
            on_import=self.import_from_file,
            on_lock=self.lock,
        )
        self.view.pack(fill=tk.BOTH, expand=True)
        self.refresh_entries()

    def refresh_entries(self):
        entries=self.model.get_entries()
        self.view.set_entries(entries)

    #CRUD METHODS
    def add_entry(self):
        from tkinter.simpledialog import askstring
        site=askstring("Site", "Enter site name: ")
        url = askstring("URL", "Enter URL: ")
        email = askstring("Email", "Enter Email: ")
        username = askstring("Username", "Enter Username: ")
        password = askstring("Password", "Enter Password: ")
        if all([site, url, email, username, password]):
            self.model.add_entry(site, url, email, username, password, self.masterkey)
            self.refresh_entries()

    def edit_entry(self):
        selected=self.view.get_selected_entry()
        if not selected:
            return
        ID, Site, url, email, username, password = selected
        from tkinter.simpledialog import askstring
        new_site=askstring("Edit Site", "Site: ", initialvalue=Site)
        new_url=askstring("Edit URL", "URL: ", initialvalue=url)
        new_email=askstring("Edit Email", "Email: ", initialvalue=email)
        new_username=askstring("Edit Username", "Username: ", initialvalue=username)
        new_password=askstring("Edit Password", "Password (keep it empty to keep the current one): ")
        if not new_password:
            new_password=self.model.get_password(ID, self.masterkey)
        self.model.edit_entry(ID, new_site, new_url, new_email, new_username, new_password, self.masterkey)
        self.refresh_entries()

    


        #Mock Data for Demonstration
        self.data:List[Tuple[str,str,str,str]] = [
            "ExSite", "https://ExURL.com", "Ex@mail.com", "ExUser"
        ]
        self.view.set_entries(self.data)

    #Controller Methods
    def add(self):
        print("Add clicked")
        # Example: add a dummy entry
        new_entry = ("NewSite", "https://new.com", "new@mail.com", "newuser")
        self.data.append(new_entry)
        self.view.set_entries(self.data)

    def edit(self):
        selected=self.view.get_selected_entry()
        if selected:
            print(f"Edit clicked on {selected}")
            #Mocking: change username
            idx=self.data.index(tuple(selected))
            self.data[idx]=(selected[0], selected[1], selected[2], "editedUser")
            self.view.set_entries(self.data)
    
    def delete(self):
        selected=self.view.get_selected_entry()
        if selected:
            print(f"Delete clicked on {selected}")
            self.data.remove(tuple(selected))
            self.view.set_entries(self.data)

    def copy(self):
        selected=self.view.get_selected_entry()
        if selected:
            print(f"Copy clicked on {selected}")
            
    def show(self):
        selected=self.view.get_selected_entry()
        if selected:
            print(f"Show clicked on {selected}")
            #Temporarily show password [MOCK]

    def generate(self):
        import random, string
        #Gen random password
        password=''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        print(f"[MOCK] Generated password: {password}")
        #optional
        selected=self.view.get_selected_entry()
        if selected:
            #Modify existing row with new generated password, so edit last column
            update_row=(selected[0], selected[1], selected[2], selected[3], password)
            self.view.clear_entries()
            self.view.set_entries([update_row])
            #Add a row of entries with the new generated password
            new_row=("New Site", "https://newURL.com", "new@mail.com", "newuser", password)
            self.view.set_entries([new_row])
    
    def export(self):
        print("Export clicked")
        #Mock

    def import_(self):
        print("Import clicked")
        # Example: load data from file (mock)
        self.data.append(("ImportedSite", "https://import.com", "import@mail.com", "importUser"))
        self.view.set_entries(self.data)

    def lock(self):
        print("Lock clicked")
        #Mock
    

    

