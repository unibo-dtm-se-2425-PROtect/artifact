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
    
    def show(self):
        self.view.show_message("Show", "Password123", kind="warning")
    
    def generate(self):
        self.view.show_message("Generate", "GenPassword!#")
    
    def export(self):
        self.view.show_message("Export", "Exported to demo.json")
    
    def import_(self):
        self.view.show_message("import", "Imported from demo.json")
    
    def lock(self):
        self.view.show_message("Lock", "Vault locked")
    
    if __name__=="__main__":
        app=tb.Window(themename="vapor")
        #view=view.GUIview.PasswordManagerView(app)
        def dummy():pass
        #ctrl = view.DemoController(view) We jave to define a controller yet
        #view.set_callbacks(
        #    on_add=lambda:ctrl.add,
        #   on_edit=lambda:ctrl.edit,
        #   on_delete=lambda:ctrl.delete(),
        #   on_copy=lambda:ctrl.copy(),
        #   on_show=lambda:ctrl.show(),
        #   on_generate=lambda:ctrl.generate(),
        #   on_export=lambda:ctrl.export(),
        #   on_import=lambda:ctrl.import_(),
        #   on_lock=lambda:ctrl.lock()
        #)
        view = view.PasswordManagerView(
            on_add=dummy,
            on_edit=dummy,
            on_delete=dummy,
            on_copy=dummy,
            on_show=dummy,
            on_generate=dummy,
            on_export=dummy,
            on_import=dummy,
            on_lock=dummy,
            on_search=dummy,
            on_clear=dummy
        )
        view.pack(fill="both", expand=True)

        app.mainloop