import hashlib
import pytest
from unittest.mock import patch, MagicMock
import project.add as add

#define function to be used in the following test functions
#check the MasterKey is correctly computed, using hashlib.sha256 module 
def test_computeMasterKey(mp: str,ds: str) -> bytes:
    if not isinstance(mp, (str, bytes)) or not isinstance(ds, (str, bytes)):
        # let invalid types raise naturally (TypeError) when trying to encode or combine
        raise TypeError("mp and ds must be str or bytes")
    if isinstance(mp, str):
        mp_b = mp.encode()
    else:
        mp_b = mp
    if isinstance(ds, str):
        ds_b = ds.encode()
    else:
        ds_b = ds
    return hashlib.sha256(mp_b + ds_b).digest()
  
#verifying that the output is of type bytes and length 32
def test_computeMasterKey_return_type_and_length():
    mp = "masterPassword"
    ds = "deviceSecret"
    k = test_computeMasterKey(mp, ds)
    assert isinstance(k, (bytes,bytearray))
    assert len(k) == 32

#verifying that the output is deterministic and unique for different inputs
@pytest.mark.parametrize("mp, ds", [
    ("masterPassword", "deviceSecret"),
    ("anotherPass", "anotherSecret"),
])
def test_deterministicOutput_and_uniqueness(mp, ds):
    # Use a fast computeMasterKey to avoid expensive PBKDF2
    with patch.object(add, "computeMasterKey", side_effect=fast_computeMasterKey):
        key1 = add.computeMasterKey(mp, ds)
        key2 = add.computeMasterKey(mp, ds)
        assert key1 == key2
        key_other = add.computeMasterKey(mp+"x", ds+"y")
        assert key1 != key_other

#testing type errors for non-string inputs
@pytest.mark.parametrize("mp, ds", [
    (None, "deviceSecret"),       # mp is None
    ("masterPassword", None),     # ds is None
    (123, "deviceSecret"),        # mp is int
    ("masterPassword", 456),      # ds is int
])
def test_computeMasterKey_type_errors(mp, ds):
    with pytest.raises((TypeError, AttributeError)):
        fast_computeMasterKey(mp, ds)

#testing edge cases with empty strings, long strings, and unicode, ensuring the 
#output is still valid and consistent
@pytest.mark.parametrize("mp, ds", [
    ("", ""),                      # empty strings
    ("a" * 10000, "b" * 10000),    # very long inputs
    ("パスワード", "秘密"),          # unicode inputs
])
def test_fast_computeMasterKey_edge_cases(mp, ds):
    key = fast_computeMasterKey(mp, ds)
    assert isinstance(key, bytes)
    assert len(key) == 32

def test_compute_master_key_invalid_types():
    # Expect a TypeError when non-str types are passed
    with pytest.raises(TypeError):
        fast_computeMasterKey(None, None)


#checkEntry unit tests


#mocking the DB to test the checkEntry function for an existing entry
@patch("project.add.dbconfig")
def test_check_entry_exists(mock_dbconfig):
    # Mock DB cursor
    mock_db = MagicMock()
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = [("row1",)] 
    mock_dbconfig.return_value = mock_db
    result = add.checkEntry("site", "url", "email", "user")
    assert result is True
    assert mock_cursor.execute.called
    called_query = mock_cursor.execute.call_args[0][0]
    #check that the query contains the right keywords
    assert "SELECT" in called_query.upper()
    assert "site" in called_query

#mocking the DB to test the checkEntry function for a non-existing entry
@patch("project.add.dbconfig")
def test_check_entry_not_exists(mock_dbconfig):
    mock_db = MagicMock()
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = [] 
    mock_dbconfig.return_value = mock_db

    result = add.checkEntry("site", "url", "email", "user")
    assert result is False
    assert mock_cursor.execute.called

#simulating a DB error during query execution
#asserting that checkEntry raises and exception in this case
@patch("project.add.dbconfig")
def test_check_entry_execute_raises(mock_dbconfig):
    mock_db = MagicMock()
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.execute.side_effect = Exception("db error")
    mock_dbconfig.return_value = mock_db
    
    with pytest.raises(Exception):
        add.checkEntry("s", "u", "e", "n")

#simulate special characters in inputs to check for SQL injection vulnerability
@patch("project.add.dbconfig")
def test_check_entry_with_special_chars(mock_dbconfig):
    mock_db = MagicMock()
    mock_cursor = mock_db.cursor.return_value
    mock_cursor.fetchall.return_value = []
    mock_dbconfig.return_value = mock_db

    # Inputs with SQL-sensitive characters
    result = add.checkEntry("site'; DROP TABLE entries;--", "url", "email", "user") #attempted SQL injection
    assert result is False
    called_query = mock_cursor.execute.call_args[0][0] #get the executed query
    assert "DROP TABLE" not in called_query.upper() #verify no SQL injection occurred


#addEntry unit tests


#simulate a case where the entry already exists
#verify that addEntry does not attempt to get the password or add to DB
@patch("project.add.printc")
@patch("project.add.checkEntry", return_value=True)
def test_add_entry_when_exists(mock_checkentry, mock_printc):
    with patch("project.add.getpass") as mock_getpass:
        add.addEntry("mp", "ds", "site", "url", "email", "user")
    
    mock_getpass.assert_not_called()
    mock_printc.assert_called_once()
    
#simulate a full successful addition of an entry
@patch("project.add.getpass") #mocking user password input
@patch("project.add.AES256util") #mocking AES encryption
@patch("project.add.dbconfig") #mocking DB connection
@patch("project.add.checkEntry", return_value=False) #simulate entry does not exist
def test_add_entry_happy_path(mock_checkentry, mock_dbconfig, mock_aes, mock_getpass):
    mock_getpass.return_value = "plainpassword" #simulate user input password
    mock_aes.encrypt.return_value = "encrypted_blob" #simulate successful encryption

    mock_db = MagicMock() #simulate DB connection
    mock_cursor = mock_db.cursor.return_value
    mock_dbconfig.return_value = mock_db

    with patch.object(add, "computeMasterKey", return_value=b"\x00"*32): #simulate master key computation
        add.addEntry("mp", "ds", "site", "url", "email", "user") #simulate adding entry

    mock_aes.encrypt.assert_called_once() #verify encryption succeeded
    mock_cursor.execute.assert_called_once() #verify DB insert was attempted
    mock_db.commit.assert_called_once() #verify DB commit was called

#simulate a DB commit failure during addEntry
@patch("project.add.getpass")
@patch("project.add.AES256util")
@patch("project.add.dbconfig")
@patch("project.add.checkEntry", return_value=False)
def test_add_entry_commit_failure(mock_checkentry, mock_dbconfig, mock_aes, mock_getpass):
    mock_getpass.return_value = "plainpassword"
    mock_aes.encrypt.return_value = "encrypted_blob"
    
    mock_db = MagicMock()
    mock_cursor = mock_db.cursor.return_value
    mock_db.commit.side_effect = Exception("commit failed") #simulate DB commit failure
    mock_dbconfig.return_value = mock_db

    with patch.object(add, "computeMasterKey", return_value=b"\x00" * 32):
        with pytest.raises(Exception): #verify that Exception is raised on commit failure
            add.addEntry("mp", "ds", "site", "url", "email", "user")

#simulate the user entering an empty password
@patch("project.add.getpass", return_value="")
def test_add_entry_empty_password(mock_getpass):
    with pytest.raises(ValueError): #verify that ValueError is raised for empty password
        add.addEntry("mp", "ds", "site", "url", "email", "user")
#simulate encryption failure during addEntry
@patch("project.add.getpass")
@patch("project.add.AES256util")
@patch("project.add.dbconfig")
@patch("project.add.checkEntry", return_value=False)
def test_add_entry_encrypt_failure(mock_checkentry, mock_dbconfig, mock_aes, mock_getpass):
    mock_getpass.return_value = "plain" #simulate user input password
    mock_aes.encrypt.side_effect = Exception("encrypt failure") #simulate encryption failure
    mock_db = MagicMock()
    mock_dbconfig.return_value = mock_db

    with patch.object(add, "computeMasterKey", return_value=b"\x00"*32):
        with pytest.raises(Exception):
            add.addEntry("mp", "ds", "s", "u", "e", "n")

#simulate encryption returning None
#check that addEntry raises ValueError in this case
@patch("project.add.getpass")
@patch("project.add.AES256util")
@patch("project.add.dbconfig")
@patch("project.add.checkEntry", return_value=False)
def test_add_entry_encrypt_returns_none(mock_checkentry, mock_dbconfig, mock_aes, mock_getpass):
    mock_getpass.return_value = "plainpassword"
    mock_aes.encrypt.return_value = None #simulate encryption returning None
    
    mock_db = MagicMock()
    mock_dbconfig.return_value = mock_db

    with patch.object(add, "computeMasterKey", return_value=b"\x00" * 32):
        with pytest.raises(ValueError): #verify that ValueError is raised for None encrypted password
            add.addEntry("mp", "ds", "site", "url", "email", "user")

#simulate invalid key type during encryption
@patch("project.add.getpass")
@patch("project.add.AES256util")
@patch("project.add.dbconfig")
@patch("project.add.checkEntry", return_value=False)
def test_add_entry_invalid_key_type(mock_checkentry, mock_dbconfig, mock_aes, mock_getpass):
    mock_getpass.return_value = "plainpassword"
    mock_aes.encrypt.side_effect = TypeError("invalid key type") #simulate invalid key type error
    
    mock_db = MagicMock()
    mock_dbconfig.return_value = mock_db

    with patch.object(add, "computeMasterKey", return_value="not_bytes"):
        with pytest.raises(TypeError): #verify that TypeError is raised for invalid key type
            add.addEntry("mp", "ds", "site", "url", "email", "user")
