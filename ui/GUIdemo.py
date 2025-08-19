#demo for GUI to create an interactive exploration for visual/manual verification 
#It's not the TEST for GUI!
#demo does not need to be tested, we directly test the MVC in the tests package 

import ttkbootstrap as tb

class DemoController:
    def __init__(self, view):
        self.view=view
        self.entries=[
            ("GitHub", "https://github.com", "git@mail.com", "myuser"),
            ("Gmail", "https://gmail.com", "me@mail.com", "me"),
        ]
        self.refresh()
    
    def refresh(self):
        self.view.set_entries(self.entries)
    
    def add(self): 
        self.entries.append(("NewSite", "https://new.com", "newuser@mail.com", "newuser"))
        self.refresh()
    
    def edit(self):
        sel=self.view.get_selected_entry()
        if sel:
            self.view.show_message("Edit", f"Would you edit {sel[0]}")
    
    def delete(self):
        sel=self.view.get_selected_entry()
        if sel:
            self.entries=[r for r in self.entries if r[0]!=sel[0]]
            self.refresh()
    
    def copy(self): 
        self.view.show_message("Copy", "Password copied (mock)")
    