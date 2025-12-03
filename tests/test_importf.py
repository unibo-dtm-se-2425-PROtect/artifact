import csv  # to be used for CSV operations
import builtins
from unittest.mock import MagicMock, patch
import pytest

# Import module under test
import importlib
import project.importf as importf_mod

class DummyCursor:
    """Cursor stub that records execute calls."""
    def __init__(self):
        self.executed = []

    def execute(self, query, params):
        # record the SQL and params for assertions
        self.executed.append((query, params))

    def close(self):
        pass

class DummyDB:
    #DB stub with cursor(), commit(), close() and flags to observe side effects.
    def __init__(self, cursor):
        self._cursor = cursor
        self.committed = False
        self.closed = False

    def cursor(self):
        return self._cursor

    def commit(self):
        self.committed = True

    def close(self):
        self.closed = True

def make_csv_file(tmp_path, content, name="test.csv"):
    """Create a UTF-8 CSV file and return its path (string)."""
    p = tmp_path / name
    p.write_text(content, encoding="utf-8")
    return str(p)

# ----- Tests -----

def test_import_entries_success(tmp_path, capsys):
    """
    Purpose:
    - Ensure import_entries inserts all complete rows, commits, closes DB and prints success.
    Setup:
    - Create CSV with header and two complete rows.
    - Patch dbconfig, computeMasterKey and AES256util.encrypt with deterministic fakes using patch/MagicMock.
    Assertions:
    - Two INSERT calls recorded, DB committed and closed, printed message contains count and filepath.
    """
    csv_content = "ID,Site,URL,Email,Username,Password\n" \
                  "1,site1,https://s1,e1@x.com,u1,plain1\n" \
                  "2,site2,https://s2,e2@x.com,u2,plain2\n"
    path = make_csv_file(tmp_path, csv_content)

    cursor = DummyCursor()
    db = DummyDB(cursor)

    # Fake computeMasterKey and AES256util.encrypt
    fake_compute = MagicMock(return_value="fake_master_key")
    class AESFake:
        @staticmethod
        def encrypt(mk, plaintext, keyType="hex"):
            assert mk == "fake_master_key"
            return f"enc:{plaintext}"

    with patch.object(importf_mod, "dbconfig", return_value=db), \
         patch.object(importf_mod, "computeMasterKey", fake_compute), \
         patch.object(importf_mod, "AES256util", AESFake):
        importf_mod.import_entries(path, mp="m", ds="d")

    # Assertions
    assert len(cursor.executed) == 2, "Expected two INSERT operations for two complete rows"
    q0, p0 = cursor.executed[0]
    assert "INSERT INTO PROtect.entries" in q0
    assert p0[0] == "1"
    assert p0[5] == "enc:plain1"
    assert db.committed is True
    assert db.closed is True

    out = capsys.readouterr().out
    assert "Imported 2 entries" in out
    assert path in out

def test_import_entries_skips_incomplete_rows(tmp_path, capsys):
    """
    Purpose:
    - Ensure rows with fewer than 6 columns are skipped.
    Setup:
    - CSV with one complete row and two incomplete rows.
    Assertions:
    - Only one INSERT executed, commit happens, printed count is 1.
    """
    csv_content = "ID,Site,URL,Email,Username,Password\n" \
                  "10,site,https://,a@b.com,user,pass\n" \
                  "too,few,cols\n" \
                  "also,short\n"
    path = make_csv_file(tmp_path, csv_content)

    cursor = DummyCursor()
    db = DummyDB(cursor)

    fake_compute = MagicMock(return_value="mk")
    AESFake = MagicMock()
    AESFake.encrypt = staticmethod(lambda mk, plaintext, keyType="hex": "E:" + plaintext)

    with patch.object(importf_mod, "dbconfig", return_value=db), \
         patch.object(importf_mod, "computeMasterKey", fake_compute), \
         patch.object(importf_mod, "AES256util", AESFake):
        importf_mod.import_entries(path, mp="m", ds="d")

    assert len(cursor.executed) == 1
    assert db.committed is True
    out = capsys.readouterr().out
    assert "Imported 1 entries" in out
