import builtins #used to patch the global builtins input function so tests can simulate user responses
from unittest.mock import patch, MagicMock
import pytest

#import module under test (adjust import path if needed)
import project.delete as delete_mod

 --- Test doubles for DB and Cursor ---

#creating the FakeCursor object to simulate the minimal interface needed for testing
class FakeCursor:
    def __init__(self, raise_on_execute=False, rowcount=1):
        self.queries = [] #records (sql, params) tuples passed to execute
        self.raise_on_execute = raise_on_execute #toggles a simulated DB error to test exception propagation
        self.rowcount = rowcount #models the cursor's rowcount value used to decide if rows were affected, or not found

    def execute(self, sql, params=None):
        if self.raise_on_execute:
            raise RuntimeError("execute error") #simulate a database error
        # record exactly as the real code would receive
        self.queries.append((sql, params)) #store the executed query and parameters if no error
