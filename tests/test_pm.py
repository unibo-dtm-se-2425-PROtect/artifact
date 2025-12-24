import sys 
import importlib
import hashlib
from unittest.mock import patch, MagicMock
import project.pm as pm
import pytest

# --- Fake DB and cursor helpers ---

#emulate a minimal DB cursor and connection so as to test password hash retrieval
class FakeCursor:
    def __init__(self, rows):
        self._rows = rows
        self.queries = []

    def execute(self, q):
        self.queries.append(q)

    def fetchall(self):
        return self._rows


class FakeDB:
    def __init__(self, rows):
        self._cursor = FakeCursor(rows)

    def cursor(self):
        return self._cursor

# Utility to reload cli with patches applied via context managers
def reload_cli_with_patches(patches):
    module_name = 'pm'
    """
    patches: list of (target, value) pairs to be used with patch(target, value=value)
    Returns the imported cli module after applying patches and reloading.
    """
    # Ensure fresh import
    if module_name in sys.modules: 
        del sys.modules[module_name]

    # Enter all patches as context managers
    managers = [patch(target, new=value) for target, value in patches]
    contexts = [m.__enter__() for m in managers]
    
    # Use importlib to import by the string name
    try:
        module = importlib.import_module(module_name)
        importlib.reload(module)
        return module
    finally:
        # Exit in reverse order
        for m in reversed(managers):
            m.__exit__(None, None, None)

# --- Tests for inputAndValidateMasterPassword policy checks ---

#parametrized tests for various password policy failures
@pytest.mark.parametrize("pw, expected_fragment", [
    ("Short1!", "Password must be at least 8 characters long."),
    ("lowercase1!", "Password must contain at least one uppercase letter."),
    ("NoDigits!!", "Password must contain at least one number."),
    ("NoSpecial1A", "Password must contain at least one special character."),
])
def test_password_policy_failures(pw, expected_fragment, capsys):
    # Patch getpass.getpass to return pw and dbconfig to a harmless DB (not reached)
    patches = [
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[ "dummy" ]]))),
        # Ensure sys.argv minimal so module imports but doesn't trigger other branches
        ("sys.argv", [ "prog", "configure" ]),
    ]
    # Import module to access function
    cli = reload_cli_with_patches(patches)
    res = cli.inputAndValidateMasterPassword()
    captured = capsys.readouterr()
    assert res is None
    assert expected_fragment in captured.out

def test_input_master_password_wrong_hash(capsys):
    pw = "GoodPass1!"
    wrong_hash = hashlib.sha256("other".encode()).hexdigest()
    fake_db = FakeDB([[wrong_hash, "SALT"]])

    patches = [
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("sys.argv", [ "prog", "configure" ]),
    ]
    cli = reload_cli_with_patches(patches)
    res = cli.inputAndValidateMasterPassword()
    captured = capsys.readouterr()
    assert res is None
    # rich.print may include color tags; check for either marker
    assert "WRONG" in captured.out or "[red][!]" in captured.out

def test_input_master_password_success():
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALTVALUE"]])

    patches = [
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("sys.argv", [ "prog", "configure" ]),
    ]
    cli = reload_cli_with_patches(patches)
    res = cli.inputAndValidateMasterPassword()
    #ensure plaintext password and salt returned
    assert res == [pw, "SALTVALUE"]

# --- Tests for main() branches, mocking external functions ---

"""sys.argv is patched per-test to simulate command-line args for each CLI option, 
    including add, extract, remove, modify, import, 
    export, configure, delete configuration, reconfigure."""

def test_add_missing_fields(capsys):
    # argv: program name + option 'add' (no required fields)
    patches = [
        ("sys.argv", [ "prog", "add" ]),
        ("getpass.getpass", MagicMock(return_value="Ignored1!")),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[ "h", "s" ]]))),
        ("project.add.addEntry", MagicMock()),  # should not be called
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    # addEntry should not have been called
    assert not sys.modules['cli'].add.addEntry.called if hasattr(sys.modules['cli'], 'add') else True
    assert "Site Name" in captured.out or "Username" in captured.out or "Password" in captured.out

def test_add_all_fields_calls_addEntry():
    argv = [ "prog", "add", "-s", "site", "-l", "user", "-p", "pass", "-e", "mail", "-u", "url" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALT"]])

    fake_add = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.add.addEntry", fake_add),
    ]
    cli = reload_cli_with_patches(patches)
    # verify addEntry called with expected args
    fake_add.assert_called_once_with(pw, "SALT", "site", "url", "mail", "user", "pass")

def test_extract_no_master(capsys):
    #simulates prog extract -s site with a wrong master hash in DB.
    argv = [ "prog", "extract", "-s", "site" ]
    pw = "GoodPass1!"
    fake_db = FakeDB([[hashlib.sha256("other".encode()).hexdigest(), "SALT"]])

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.retrieve.retrieveEntries", MagicMock()),
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    assert "WRONG" in captured.out or "[red][!]" in captured.out

def test_extract_no_search_fields_and_no_all(capsys):
    # Simulates prog extract with valid master but no search flags and no --all
    argv = [ "prog", "extract" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALT"]])

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.retrieve.retrieveEntries", MagicMock()),
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    assert "Please enter at least one search field" in captured.out

def test_extract_with_search_fields_calls_retrieve():
    argv = [ "prog", "extract", "-s", "mysite", "-l", "myuser", "-u", "myurl", "-e", "myemail" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALT"]])

    fake_retrieve = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.retrieve.retrieveEntries", fake_retrieve),
    ]
    cli = reload_cli_with_patches(patches)
    # ensure retrieveEntries called once and inspect args
    fake_retrieve.assert_called_once()
    called_args = fake_retrieve.call_args[0]
    assert called_args[0] == pw
    assert called_args[1] == "SALT"
    assert set(called_args[2].keys()) == {"Site", "URL", "Email", "Username"}

def test_extract_with_all_calls_retrieve():
    # simulates prog extract --all
    argv = [ "prog", "extract", "--all" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALT"]])

    fake_retrieve = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.retrieve.retrieveEntries", fake_retrieve),
    ]
    cli = reload_cli_with_patches(patches)
    fake_retrieve.assert_called_once()
    called_args = fake_retrieve.call_args[0]
    assert called_args[2] == {}
    # default decryptPassword is False
    assert called_args[3] is False

def test_remove_without_id(capsys):
    # simulates prog remove with no --id
    argv = [ "prog", "remove" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALT"]])

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.delete.delete_entry", MagicMock()),
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    assert "Entry ID (--id) is required for deletion" in captured.out

def test_remove_with_id_calls_delete():
    """Simulates prog remove --id 42.
       Asserts delete_entry called with id, master, salt."""
    argv = [ "prog", "remove", "--id", "42" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()
    fake_db = FakeDB([[hashed, "SALT"]])

    fake_delete = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=fake_db)),
        ("project.delete.delete_entry", fake_delete),
    ]
    cli = reload_cli_with_patches(patches)
    fake_delete.assert_called_once_with("42", pw, "SALT")

def test_modify_without_id(capsys):
     # simulates prog modify with no --id
    argv = [ "prog", "modify" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[hashed, "SALT"]]))),
        ("project.modify.modify_entry", MagicMock()),
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    assert "Entry ID (--id) is required for modification" in captured.out

def test_modify_with_id_calls_modify():
    """Simulates prog modify --id 99.
       Asserts modify_entry called with id, master, salt"""
    argv = [ "prog", "modify", "--id", "99" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()

    fake_modify = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[hashed, "SALT"]]))),
        ("project.modify.modify_entry", fake_modify),
    ]
    cli = reload_cli_with_patches(patches)
    fake_modify.assert_called_once_with("99", pw, "SALT")

def test_import_without_file(capsys):
    # simulates prog import without -f.
    argv = [ "prog", "import" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[hashed, "SALT"]]))),
        ("project.importf.import_entries", MagicMock()),
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    assert "File path (-f/--file) is required for import" in captured.out

def test_import_with_file_calls_import_entries():
    """simulates prog import -f data.csv.
       Asserts import_entries called with path, master, salt."""
    argv = [ "prog", "import", "-f", "data.csv" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()

    fake_import = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[hashed, "SALT"]]))),
        ("project.importf.import_entries", fake_import),
    ]
    cli = reload_cli_with_patches(patches)
    fake_import.assert_called_once_with("data.csv", pw, "SALT")

def test_export_without_file(capsys):
    # simulates prog export without -f.
    argv = [ "prog", "export" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[hashed, "SALT"]]))),
        ("project.export.export_entries", MagicMock()),
    ]
    cli = reload_cli_with_patches(patches)
    captured = capsys.readouterr()
    assert "File path (-f/--file) is required for export" in captured.out

def test_export_with_file_calls_export_entries():
    """simulates prog export -f out.csv.
       Asserts export_entries called with path, master, salt."""
    argv = [ "prog", "export", "-f", "out.csv" ]
    pw = "GoodPass1!"
    hashed = hashlib.sha256(pw.encode()).hexdigest()

    fake_export = MagicMock()

    patches = [
        ("sys.argv", argv),
        ("getpass.getpass", MagicMock(return_value=pw)),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[hashed, "SALT"]]))),
        ("project.export.export_entries", fake_export),
    ]
    cli = reload_cli_with_patches(patches)
    fake_export.assert_called_once_with("out.csv", pw, "SALT")

def test_configure_delete_reconfigure_calls():
    # prepare MagicMocks for config, delete, reconfig
    fake_config = MagicMock()
    fake_delete = MagicMock()
    fake_reconfig = MagicMock()

    # running three reloads with different argv values
     # configure
    patches = [
        ("sys.argv", [ "prog", "configure" ]),
        ("getpass.getpass", MagicMock(return_value="Ignored1!")),
        ("project.dbconfig.dbconfig", MagicMock(return_value=FakeDB([[ "h", "s" ]]))),
        ("project.config.config", fake_config),
        ("project.config.delete", fake_delete),
        ("project.config.reconfig", fake_reconfig),
    ]
    cli = reload_cli_with_patches(patches)
    fake_config.assert_called_once()

    # delete configuration (script expects exact string "delete configuration")
    patches[0] = ("sys.argv", [ "prog", "delete configuration" ])
    cli = reload_cli_with_patches(patches)
    fake_delete.assert_called_once()

    # reconfigure
    patches[0] = ("sys.argv", [ "prog", "reconfigure" ])
    cli = reload_cli_with_patches(patches)
    fake_reconfig.assert_called_once()
