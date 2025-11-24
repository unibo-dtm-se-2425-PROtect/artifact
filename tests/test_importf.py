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
