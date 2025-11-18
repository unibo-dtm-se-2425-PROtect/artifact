import csv #to be used for CVS operations
import builtins
from unittest.mock import MagicMock, patch
import pytest

# Import the module under test
import project.export as export

def test_export_entries_db_connection_failure(capsys):
    # dbconfig returns falsy -> should print connection error and return without exception
    with patch("project.export.dbconfig", return_value=None) as mock_dbconfig: # Patch dbconfig to return None so the function thinks DB connection failed
        # Call with dummy filepath (no file will be created)
        export.export_entries("dummy.csv", "mp", "ds")

    captured = capsys.readouterr()
    assert "Could not connect to database" in captured.out
    mock_dbconfig.assert_called_once()
