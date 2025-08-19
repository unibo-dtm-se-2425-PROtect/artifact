import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import BOTH, X, Y, LEFT, RIGHT, END, messagebox, filedialog
from typing import Callable, Optional, List, Tuple

class PasswordManagerView (tb.Frame):
    #It only defines the GUI, doesn't consider db, crypto etc. The controller must be passed in to handle actions
    def __init__(
            self,
            master,
            on_add: callable[[], None],
            on_edit: callable[[], None],
            on_delete: callable[[], None],
            on_copy: callable[[], None],
            on_show: callable[[], None],
            on_generate: callable[[], None],
            on_export: callable[[], None],
            on_import: callable[[], None],
            on_lock: callable[[], None],
            **kwargs
    ):
        super().__init__(master, padding=15, **kwargs)
    
        #HEADER
        header=tb.Frame(self)
        header.pack(fill=X)
        tb.Label(header, text="Password Manager", font=('Helvetica', 18)).pack(side=LEFT)
        tb.Button(header, text="Lock", bootstyle=DANGER, command=on_lock).pack(side=RIGHT, padx=5)
        tb.Button(header, text="Export", command=on_export).pack(side=RIGHT, padx=5)
        tb.Button(header, text="Import", command=on_import).pack(side=RIGHT, padx=5)

        #TOOLBAR
        bar=tb.Frame(self)
        bar.pack(fill=X, pady=8)
        tb.Button(bar, text="Add", bootstyle=SUCCESS, command=on_add).pack(side=LEFT, padx=4)
        tb.Button(bar, text="Edit", command=on_edit).pack(side=LEFT, padx=4)
        tb.Button(bar, text="Delete", bootstyle=DANGER, command=on_delete).pack(side=LEFT, padx=4)
        tb.Separator(bar, orient=VERTICAL).pack(side=LEFT, fill=Y, padx=8)
        tb.Button(bar, text="Copy", command=on_copy).pack(side=LEFT, padx=4)
        tb.Button(bar, text="Show (10s)", bootstyle=WARNING, command=on_show).pack(side=LEFT, padx=4)
        tb.Separator(bar, orient=VERTICAL).pack(side=LEFT, fill=Y, padx=8)
        tb.Button(bar, text="Generate", command=on_generate).pack(side=LEFT, padx=4)

        

