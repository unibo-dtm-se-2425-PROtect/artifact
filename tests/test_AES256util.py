import sys 
import importlib #used to import or reload modules programmatically
import types #used to create new module objects at runtime
import base64 #used to encode and decode binary ciphertext to/from a printable ASCII form 
import hashlib #used to compute cryptographic hash digests (SHA-256) using the Python standard library
import pytest 

# --- Helpers to inject a fake project.dbconfig module -----------------------
class _FakeCursor:
    def __init__(self, result):
        self._result = result
        self.executed = None
        self.params = None

    def execute(self, query, params=None):
        self.executed = query
        self.params = params

    def fetchone(self):
        return self._result

class _FakeDB:
    def __init__(self, result):
        self._cursor = _FakeCursor(result)
        self.closed = False

    def cursor(self, dictionary=True):
        return self._cursor

    def close(self):
        self.closed = True
