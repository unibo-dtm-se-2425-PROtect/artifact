import tkinter as tk
from unittest import mock
import types

import project.tkinter_bootstrap_sample as app_module #import module under test

#fake widget implementations

class FakeWidget:
    """
    Base fake widget.
    - Records init kwargs in _config for possible assertions.
    - Records whether pack() was called via _packed.
    """
    def __init__(self, *args, **kwargs):
        self._config = kwargs
        self._packed = False

    def pack(self, *args, **kwargs):
        # Simulate packing the widget into a layout manager.
        self._packed = True
   
class FakeFrame(FakeWidget):
    pass

class FakeLabel(FakeWidget):
    pass

class FakeEntry(FakeWidget):
 """Stand-in for ttk.Entry with minimal stateful behavior:
 """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = ""
        self.deleted_calls = []  # records (start, end) tuples
        self.focused = False
