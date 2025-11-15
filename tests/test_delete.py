import builtins #used to patch the global builtins input function so tests can simulate user responses
from unittest.mock import patch, MagicMock
import pytest

#import module under test (adjust import path if needed)
import project.delete as delete_mod

# --- Test doubles for DB and Cursor ---

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

#emulate the DB connection object returned by dbconfig()
class FakeDB:
    def __init__(self, cursor_obj):
        self._cursor = cursor_obj 
        self.committed = False 
        self.closed = False 

    def cursor(self):
        return self._cursor #returns the injected FakeCursor

    def commit(self):
        self.committed = True #flips the committed flag when commit() is called

    def close(self):
        self.closed = True #flips the closed flag when close() is called

#lightweight factory to create a FakeDB with a FakeCursor
def make_fake_db(rowcount=1, raise_on_execute=False):
    cur = FakeCursor(raise_on_execute=raise_on_execute, rowcount=rowcount) #create the FakeCursor with configurable rowcount and error behavior
    db = FakeDB(cur) #create the FakeDB with the FakeCursor
    return db, cur #return the paired objects for use in tests

# --- Tests ---

#exercise the branch where the user does not confirm deletion
def test_delete_entry_cancel_confirmation(capsys):
    #capsys is a pytest fixture to capture stdout/stderr output during the test
    db, cursor = make_fake_db(rowcount=1)

    # patch dbconfig to return our fake DB
    with patch.object(delete_mod, "dbconfig", return_value=db), \
         patch.object(builtins, "input", lambda prompt="": "n"): #builtins.input patched to simulate user cancelling
        delete_mod.delete_entry("123") #invoke the function under test

    # assert that no SQL was executed
    assert cursor.queries == []
    # assert that the DB was closed and not committed
    assert db.closed is True
    assert db.committed is False
    #assert the output mandatorily includes the cancellation message
    captured = capsys.readouterr().out #capture stdout
    assert "Deletion cancelled." in captured

#test the happy path where deletion is confirmed and successful
def test_delete_entry_successful_delete(capsys):
    db, cursor = make_fake_db(rowcount=1)
    with patch.object(delete_mod, "dbconfig", return_value=db), \
         patch.object(builtins, "input", lambda prompt="": "y"):
        delete_mod.delete_entry("42")

    # SQL executed with ID param as string (code passes ID unchanged)
    assert cursor.queries == [("DELETE FROM PROtect.entries WHERE ID=%s", ("42",))]
    assert db.committed is True
    assert db.closed is True
    captured = capsys.readouterr().out
    assert "Entry with ID 42 successfully deleted." in captured

#test the scenario where the deletion SQL raises an exception 
#exception should be raised since DELETE affects no rows
def test_delete_entry_no_row_found(capsys):
    db, cursor = make_fake_db(rowcount=0) #rowcount=0 simulates no rows affected
    #after execute, delete_entry inspects cursor.rowcount to decide what to print out to the user
    with patch.object(delete_mod, "dbconfig", return_value=db), \
         patch.object(builtins, "input", lambda prompt="": "y"):
        delete_mod.delete_entry("99") 

    assert db.committed is True #commit should be called also in this case
    assert db.closed is True 
    captured = capsys.readouterr().out
    assert "No entry found with the provided ID." in captured #inform user no rows matched
