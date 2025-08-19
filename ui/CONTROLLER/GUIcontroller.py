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

    
