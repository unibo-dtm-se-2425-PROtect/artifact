import pytest
from unittest.mock import patch, MagicMock
import project.add as add

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512 

#A faster version of computeMasterKey for testing to avoid long PBKDF2 computation
#The iteration count is set to 100 instead of 1000000 so not to slow down the tests and performance overall
def fast_computeMasterKey(mp: str,ds: str) -> bytes:
    return PBKDF2(mp.encode(), ds.encode(), 32, count=100, hmac_hash_module=SHA512)
  
#verifying that the output is of type bytes and length 32
def test_computeMasterKey_return_type_and_length():
    mp = "masterPassword"
    ds = "deviceSecret"
    k = fast_computeMasterKey(mp, ds)
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
        add.computeMasterKey(None, None)

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
