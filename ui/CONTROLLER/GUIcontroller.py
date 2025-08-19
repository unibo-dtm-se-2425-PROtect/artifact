from ui.VIEW.GUIview import PasswordManagerView
from typing import List, Tuple

class PasswordManagerController:
    def __init__(self, view:PasswordManagerView):
        self.view=view

        #Bind view callbacks to controller methods
        self.view.on_add=self.add
        self.view.on_edit=self.edit
        self.view.on_delete=self.delete
        self.view.on_copy=self.copy
        self.view.on_generate=self.generate
        self.view.on_show=self.show
        self.view.on_export=self.export
        self.view.on_import=self.import_
        self.view.lock=self.lock

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

    

