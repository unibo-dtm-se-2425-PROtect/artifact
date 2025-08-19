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

        


