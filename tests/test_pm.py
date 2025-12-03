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

