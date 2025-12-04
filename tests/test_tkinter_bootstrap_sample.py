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
    """
    Stand-in for ttk.Entry with minimal stateful behavior:
    - _value stores the text content.
    - get() returns the current value.
    - set_value(v) is a test helper to simulate user typing.
    - delete(start, end) records calls and clears the stored value.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._value = ""
        self.deleted_calls = []  # records (start, end) tuples
        self.focused = False
    
    def get(self):
        return self._value
    
    def set_value(self, v):
        # Helper used by tests to simulate user input
        self._value = v
    
    def delete(self, start, end=None):
        # Record the delete call and clear the stored value
        self.deleted_calls.append((start, end))
        self._value = ""
