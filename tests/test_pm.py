import sys 
import importlib
import hashlib
from unittest.mock import patch, MagicMock

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
    """
    patches: list of (target, value) pairs to be used with patch(target, value=value)
    Returns the imported cli module after applying patches and reloading.
    """
    # Ensure fresh import
    if 'cli' in sys.modules:
        del sys.modules['cli']

    # Enter all patches as context managers
    managers = [patch(target, new=value) for target, value in patches]
    contexts = [m.__enter__() for m in managers]
    try:
        import cli
        importlib.reload(cli)
        return cli
    finally:
        # Exit in reverse order
        for m in reversed(managers):
            m.__exit__(None, None, None)
