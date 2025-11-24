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
