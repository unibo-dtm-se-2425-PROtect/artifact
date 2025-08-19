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
