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
    - focus() records that the widget received focus.
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

    def focus(self):
        # Record that focus() was called
        self.focused = True    


class FakeButton(FakeWidget):
    """
    Stand-in for ttk.Button:
    - Captures the 'command' passed at construction so tests can invoke it.
    - invoke() calls the stored command if callable.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # The real ttk.Button accepts a command kwarg; store it for tests.
        self.command = kwargs.get("command")

    def invoke(self):
        if callable(self.command):
            return self.command()


class FakeStyle:
    """
    Stand-in for ttkbootstrap.Style.
    - Stores the theme argument so tests could assert it if needed.
    """
    def __init__(self, *args, **kwargs):
        # Accept either Style(theme='...') or Style('theme')
        self.theme = kwargs.get("theme", args[0] if args else None)


#fake root object creation 

class FakeRoot:
    """
    Minimal fake for tk.Tk root:
    - title(text) stores the title string in titled.
    - geometry(geom) stores the geometry string in geometry_value.
    - bind(sequence, callback) records event bindings in bindings dict.
    """
    def __init__(self):
        self.titled = None
        self.geometry_value = None
        self.bindings = {}

    def title(self, text):
        self.titled = text

    def geometry(self, geom):
        self.geometry_value = geom

    def bind(self, sequence, callback):
        # Store the callback so tests can assert the binding exists and is callable.
        self.bindings[sequence] = callback


#patching helper

def apply_widget_patches(module):
    """
    Create patch context managers that replace:
    - module.Style with FakeStyle
    - module.ttk with a simple namespace exposing FakeFrame, FakeLabel, FakeEntry, FakeButton
    """
    patches = [
        mock.patch.object(module, "Style", new=FakeStyle),
        mock.patch.object(module, "ttk", new=types.SimpleNamespace(
            Frame=FakeFrame,
            Label=FakeLabel,
            Entry=FakeEntry,
            Button=FakeButton
        )),
    ]
    return patches #returns a list of patch context managers to be used with 'with'.


# -------------------------
# Tests
# -------------------------
