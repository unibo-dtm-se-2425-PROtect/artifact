import sys 
import importlib #used to import or reload modules programmatically
import types #used to create new module objects at runtime
import base64 #used to encode and decode binary ciphertext to/from a printable ASCII form 
import hashlib #used to compute cryptographic hash digests (SHA-256) using the Python standard library
import pytest 

from unittest.mock import patch, MagicMock


# --- Helpers to inject a fake project.dbconfig module -----------------------

# We use MagicMock because it automatically handles sub-imports (like rich.console)
# preventing "is not a package" errors if pytest tries to use rich internally.
try:
    import rich
except ImportError:
    # Only mock if strictly necessary to avoid messing with pytest's own output
    mock_rich = MagicMock()
    # Ensure print calls go to real stdout so we can debug if needed
    mock_rich.print = print 
    sys.modules["rich"] = mock_rich

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


def _inject_dbconfig_module(result):
    """
    Create a temporary module named project.dbconfig in sys.modules that exposes
    a dbconfig() function returning a fake DB object. Returns a cleanup function
    that restores sys.modules to its previous state.
    """
    # Save previous entries to restore later
    prev_project = sys.modules.get("project")
    prev_dbconfig = sys.modules.get("project.dbconfig")

    # Ensure package module 'project' exists
    if "project" not in sys.modules:
        project_mod = types.ModuleType("project")
        sys.modules["project"] = project_mod
    else:
        project_mod = sys.modules["project"]

    # Create dbconfig submodule
    dbconfig_mod = types.ModuleType("project.dbconfig")
    def dbconfig():
        return _FakeDB(result)
    dbconfig_mod.dbconfig = dbconfig
    sys.modules["project.dbconfig"] = dbconfig_mod
    # Also attach as attribute to package module for normal import semantics
    setattr(project_mod, "dbconfig", dbconfig_mod)

    def _cleanup():
        # remove injected module and restore previous ones
        if prev_dbconfig is not None:
            sys.modules["project.dbconfig"] = prev_dbconfig
            setattr(sys.modules["project"], "dbconfig", prev_dbconfig)
        else:
            sys.modules.pop("project.dbconfig", None)
            if prev_project is None:
                # remove package if we created it
                sys.modules.pop("project", None)
            else:
                # restore package object
                sys.modules["project"] = prev_project

    return _cleanup

# --- Import target module helper -------------------------------------------
def _reload_aesutil():
    """
    Import or reload the AES256util module from the test working directory.
    Assumes the module file is named AES256util.py and is importable.
    """
    if "project.AES256util" in sys.modules:
        return importlib.reload(sys.modules["project.AES256util"])
    return importlib.import_module("project.AES256util")


# --- Tests for encryption / decryption -------------------------------------

#verify encrypt and decrypt roundtrip with hex key
def test_encrypt_decrypt_with_hex_key_roundtrip():
    aesutil = _reload_aesutil()
    msg = "Hello AES-256 CBC"
    hex_key = "9f735e0df9a1ddc702bf0a1a7b83033f9f7153a00c29de82cedadc9957289b05"
    
    cipher_b64 = aesutil.encrypt(hex_key, msg, encode=True, keyType="hex")
    assert isinstance(cipher_b64, str)
    
    decrypted = aesutil.decrypt(hex_key, cipher_b64, decode=True, keyType="hex")
    assert isinstance(decrypted, (bytes, bytearray))
    assert decrypted.decode() == msg

#verify encrypt and decrypt roundtrip with ascii key
def test_encrypt_decrypt_with_ascii_key_roundtrip():
    aesutil = _reload_aesutil()
    msg = "Short message"
    ascii_key = "testpassword"
    
    cipher_b64 = aesutil.encrypt(ascii_key, msg, encode=True, keyType="ascii")
    decrypted = aesutil.decrypt(ascii_key, cipher_b64, decode=True, keyType="ascii")
    assert decrypted.decode() == msg

#ensure padding is correctly handled for messages that are exact multiples of block size
def test_padding_for_blocksize_multiple():
    aesutil = _reload_aesutil()
    msg = "A" * 16
    key = "testpassword"
    cipher_b64 = aesutil.encrypt(key, msg, encode=True, keyType="ascii")
    decrypted = aesutil.decrypt(key, cipher_b64, decode=True, keyType="ascii")
    assert decrypted.decode() == msg

#verify that tampering with ciphertext raises invalid padding or integrity error
def test_tampered_cipher_raises_invalid_padding():
    aesutil = _reload_aesutil()
    msg = "Integrity test"
    key = "testpassword"
    cipher_b64 = aesutil.encrypt(key, msg, encode=True, keyType="ascii")
    raw = base64.b64decode(cipher_b64)
    tampered = bytearray(raw)
    tampered[-1] = (tampered[-1] ^ 0xFF) & 0xFF
    tampered_b64 = base64.b64encode(bytes(tampered)).decode()
    with pytest.raises(ValueError):
        aesutil.decrypt(key, tampered_b64, decode=True, keyType="ascii")

def test_raw_bytes_handling():
    """
    Tests that the fixed decrypt() function now handles raw bytes 
    correctly without crashing.
    """
    aesutil = _reload_aesutil()
    msg = "raw bytes check"
    key = "testpassword"
    
    raw_cipher = aesutil.encrypt(key, msg, encode=False, keyType="ascii")
    assert isinstance(raw_cipher, bytes)
    
    decrypted = aesutil.decrypt(key, raw_cipher, decode=False, keyType="ascii")
    assert decrypted.decode() == msg

#tests for verify_master_password 

#check behavior when no config is found
def test_verify_master_password_no_config(capsys):
    # inject fake dbconfig that returns None for fetchone
    cleanup = _inject_dbconfig_module(None)
    try:
        aesutil = _reload_aesutil()
        result = aesutil.verify_master_password("alice", "whatever")
        captured = capsys.readouterr()
        assert result is False
        assert "[!] No masterpassword configuration found" in captured.out
    finally:
        cleanup()
        importlib.reload(sys.modules["project.AES256util"])

#check behavior when wrong password is provided
def test_verify_master_password_wrong_password(capsys):
    stored_hash = hashlib.sha256("correct_mp".encode()).hexdigest()
    device_secret = "device-secret-xyz"
    
    mock_row = {
        "masterpassword_hash": stored_hash,
        "device_secret": "ds"
    }
    cleanup = _inject_dbconfig_module(mock_row)
    try:
        aesutil = _reload_aesutil()
        result = aesutil.verify_master_password("alice", "wrong_mp")
        captured = capsys.readouterr()
        assert result is None
        assert "Wrong Master Password!" in captured.out
    finally:
        cleanup()
        importlib.reload(sys.modules["project.AES256util"])

#verify successful password check
def test_verify_master_password_success():
    mp = "my_master_password"
    stored_hash = hashlib.sha256(mp.encode()).hexdigest()
    device_secret = "device-secret-xyz"
    
    mock_row = {
        "masterpassword_hash": stored_hash,
        "device_secret": device_secret
    }
    
    cleanup = _inject_dbconfig_module(mock_row)
    try:
        aesutil = _reload_aesutil()
        result = aesutil.verify_master_password("alice", mp)
        assert result == (mp, device_secret)
    finally:
        cleanup()
        importlib.reload(sys.modules["project.AES256util"])

def test_cli_main_encrypt_decrypt(capsys):
    aesutil =  _reload_aesutil()
    msg = "CLI_Test_Message"
    key = "testpassword"
    
    # 1. Test Encrypt
    args_enc = ["AES256util.py", "encrypt", msg, key, "ascii"]
    with patch.object(sys, "argv", args_enc):
        aesutil.main()
        captured = capsys.readouterr()
        cipher_text = captured.out.strip()
        assert len(cipher_text) > 0
        assert cipher_text != msg
    
    # 2. Test Decrypt
    args_dec = ["AES256util.py", "decrypt", cipher_text, key, "ascii"]
    with patch.object(sys, "argv", args_dec):
        aesutil.main()
        captured = capsys.readouterr()
        assert f"{msg}" in captured.out
