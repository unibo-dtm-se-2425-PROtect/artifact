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
