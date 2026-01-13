import pytest
from unittest.mock import patch, MagicMock
import sys
import hashlib
import project.pm as pm


#pytest fixtures

@pytest.fixture
def mock_db_setup():
    #Mocking the database connection for password validation
    with patch("project.pm.dbconfig") as mock_conn:
        mock_db = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.return_value = mock_db
        mock_db.cursor.return_value = mock_cursor
        yield mock_cursor

@pytest.fixture
def valid_auth_setup(mock_db_setup):
    #Setting up a valid password hash and device secret in the mock DB
    #Row structure: (ID, Username, Hash, DeviceSecret)
    correct_hash = hashlib.sha256("ValidPass1!".encode()).hexdigest()
    mock_db_setup.fetchone.return_value = (1, "user", correct_hash, "valid_ds")
    return correct_hash


#password policy and and authentication (auth) tests

def test_password_policy_failures(capsys):
    #test a short password to trigger policy check
    with patch("project.pm.getpass", return_value="Short1!"):
        res = pm.inputAndValidateMasterPassword()
        assert res is None
        assert "Password policy not met" in capsys.readouterr().out

def test_master_password_wrong_hash(mock_db_setup, capsys):
    #DB has one hash, user provides a different valid-format password
    db_hash = hashlib.sha256("RealPass1!".encode()).hexdigest()
    mock_db_setup.fetchone.return_value = (1, "user", db_hash, "ds")

    with patch("project.pm.getpass", return_value="WrongPass1!"):
        res = pm.inputAndValidateMasterPassword()
        
    assert res is None
    assert "WRONG MASTER PASSWORD" in capsys.readouterr().out

def test_master_password_success(valid_auth_setup):
    #user provides correct password
    with patch("project.pm.getpass", return_value="ValidPass1!"):
        res = pm.inputAndValidateMasterPassword()
    
    # Expect [OriginalPassword, DeviceSecret]
    assert res == ["ValidPass1!", "valid_ds"]


#Add Entry tests

@patch("project.pm.add.addEntry")
def test_cli_add_success(mock_add, valid_auth_setup):
    test_args = ["pm.py", "add", "-s", "Site", "-u", "url", "-e", "mail", "-l", "user", "-p", "pass"]
    
    with patch.object(sys, 'argv', test_args), \
         patch("project.pm.getpass", return_value="ValidPass1!"):
        pm.main()
        
    mock_add.assert_called_with("ValidPass1!", "valid_ds", "Site", "url", "mail", "user", "pass")

@patch("project.pm.add.addEntry")
def test_cli_add_missing_args(mock_add, capsys):
    #missing password (-p)
    test_args = ["pm.py", "add", "-s", "Site", "-l", "user"]
    with patch.object(sys, 'argv', test_args):
        pm.main()
    
    mock_add.assert_not_called()
    assert "are required" in capsys.readouterr().out


#Retrieve tests 

@patch("project.pm.retrieve.retrieveEntries")
def test_cli_extract_specific_fields(mock_retrieve, valid_auth_setup):
    test_args = ["pm.py", "extract", "-s", "Site"]
    
    with patch.object(sys, 'argv', test_args), \
         patch("project.pm.getpass", return_value="ValidPass1!"):
        pm.main()
        
    # Verify search dict
    args = mock_retrieve.call_args[0]
    assert args[2] == {"Site": "Site"}

@patch("project.pm.retrieve.retrieveEntries")
def test_cli_extract_all(mock_retrieve, valid_auth_setup):
    test_args = ["pm.py", "extract", "--all"]
    
    with patch.object(sys, 'argv', test_args), \
         patch("project.pm.getpass", return_value="ValidPass1!"):
        pm.main()
        
    #verify empty search dict (means all)
    args = mock_retrieve.call_args[0]
    assert args[2] == {}
