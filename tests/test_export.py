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

def test_export_entries_success_writes_csv(tmp_path, capsys):
    # Prepare fake DB rows and mocks
    rows = [
        # (ID, Site, URL, Email, Username, EncryptedPassword)
        (1, "example.com", "https://example.com", "a@e.com", "alice", "encpwd1"),
        (2, "test.com", "https://test.com", "b@t.com", "bob", "encpwd2"),
    ]

    # Fake DB cursor and connection
    fake_cursor = MagicMock()
    fake_cursor.execute = MagicMock()
    fake_cursor.fetchall = MagicMock(return_value=rows)
    fake_db = MagicMock()
    fake_db.cursor = MagicMock(return_value=fake_cursor)
    fake_db.close = MagicMock()

    # Patch dbconfig to return fake_db, computeMasterKey and AES256util.decrypt to simulate decryption
    with patch("project.export.dbconfig", return_value=fake_db) as mock_dbconfig, \
         patch("project.export.computeMasterKey", side_effect=lambda mp, ds: "masterkey") as mock_compute, \
         patch("project.export.AES256util.decrypt", side_effect=lambda enc, mk, keyType=None: f"dec({enc})") as mock_decrypt:

        out_file = tmp_path / "out.csv"
        export.export_entries(str(out_file), "mp-value", "ds-value")

        # Ensure DB functions were called
        mock_dbconfig.assert_called_once()
        fake_db.cursor.assert_called_once()
        fake_cursor.execute.assert_called_once()

        # Check file contents are valid CSV and decrypted passwords present
        with open(out_file, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            rows_list = list(reader)

        # ensure the header and the two rows previously defined are present
        assert rows_list[0] == ["ID", "Site", "URL", "Email", "Username", "Password (decrypted)"]
        assert rows_list[1] == ["1", "example.com", "https://example.com", "a@e.com", "alice", "dec(encpwd1)"]
        assert rows_list[2] == ["2", "test.com", "https://test.com", "b@t.com", "bob", "dec(encpwd2)"]

        # The function prints a success message
        captured = capsys.readouterr()
        assert "Entries exported to" in captured.out

        # ensure computeMasterKey used for each row
        assert mock_compute.call_count == len(rows)
        assert mock_decrypt.call_count == len(rows)

        # ensure db.close() was called
        fake_db.close.assert_called_once()


