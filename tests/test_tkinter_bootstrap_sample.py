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

def test_init_creates_widgets_and_binds_return():
    """
    Verify that LoginApp.__init__:
    - constructs the expected widget attributes (main_frame, title_label, username_entry, etc.)
    - sets the root title and geometry
    - binds the <Return> key to a callable callback
    """
    patches = apply_widget_patches(app_module)
    # Apply both patches in a scoped context so they only affect this test
    with patches[0], patches[1]:
        root = FakeRoot()
        app = app_module.LoginApp(root)

        # Assert widget attributes exist and are instances of our fakes
        assert isinstance(app.main_frame, FakeFrame)
        assert isinstance(app.title_label, FakeLabel)
        assert isinstance(app.username_frame, FakeFrame)
        assert isinstance(app.username_label, FakeLabel)
        assert isinstance(app.username_entry, FakeEntry)
        assert isinstance(app.password_frame, FakeFrame)
        assert isinstance(app.password_label, FakeLabel)
        assert isinstance(app.password_entry, FakeEntry)
        assert isinstance(app.login_button, FakeButton)

        # Root title and geometry should have been set by the constructor
        assert root.titled == "Login Application"
        assert root.geometry_value == "450x350"

        # The <Return> binding should be present and callable
        assert "<Return>" in root.bindings
        assert callable(root.bindings["<Return>"])

def test_verify_login_success_calls_showinfo_and_clears_fields():
    """
    Verify the success branch of verify_login:
    - When username == "admin" and password == "123456", messagebox.showinfo is called
    - clear_fields is invoked to reset the form
    """
    patches = apply_widget_patches(app_module)
    with patches[0], patches[1]:
        root = FakeRoot()
        app = app_module.LoginApp(root)

        # Simulate user input of correct credentials
        app.username_entry.set_value("admin")
        app.password_entry.set_value("123456")

        # Patch messagebox.showinfo to spy on it and patch clear_fields to assert it was called
        with mock.patch.object(app_module.messagebox, "showinfo") as mock_info, \
             mock.patch.object(app_module.LoginApp, "clear_fields") as mock_clear:

            app.verify_login()

            # showinfo should be called with the success title, message, and icon
            mock_info.assert_called_once_with("Success", "Login successful!", icon='info')
            # clear_fields should have been called once
            mock_clear.assert_called_once()

def test_verify_login_failure_shows_error_and_deletes_password():
    """
    Verify the failure branch of verify_login:
    - When credentials are incorrect, messagebox.showerror is called
    - Only the password entry is cleared (password_entry.delete called with 0, tk.END)
    """
    patches = apply_widget_patches(app_module)
    with patches[0], patches[1]:
        root = FakeRoot()
        app = app_module.LoginApp(root)

        # Simulate wrong credentials
        app.username_entry.set_value("user")
        app.password_entry.set_value("wrongpass")

        # Patch messagebox.showerror to spy on it
        with mock.patch.object(app_module.messagebox, "showerror") as mock_error:
            app.verify_login()

            # showerror should be called with the expected title and message
            mock_error.assert_called_once_with("Error", "Invalid username or password")

            # The password entry's delete method should have been called to clear it
            assert app.password_entry.deleted_calls, "password_entry.delete was not called"

            # Verify the delete call used start=0 and end=tk.END as in the implementation
            start, end = app.password_entry.deleted_calls[0]
            assert start == 0
            assert end == tk.END

def test_clear_fields_deletes_both_entries_and_focuses_username():
    """
    Verify clear_fields behavior:
    - Both username and password entries are cleared
    - username_entry.focus() is called so the username field receives focus
    """
    patches = apply_widget_patches(app_module)
    with patches[0], patches[1]:
        root = FakeRoot()
        app = app_module.LoginApp(root)

        # Populate entries with sample values
        app.username_entry.set_value("someone")
        app.password_entry.set_value("secret")

        # Call clear_fields directly
        app.clear_fields()

        # Both entries should now be empty
        assert app.username_entry.get() == ""
        assert app.password_entry.get() == ""

        # username_entry.focused should be True because clear_fields calls focus()
        assert app.username_entry.focused is True
