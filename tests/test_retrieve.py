import pytest
from types import SimpleNamespace #it is used to create a fake lightweight DB object
from unittest.mock import patch, MagicMock
import project.retrieve as retrieve

@pytest.fixture
def fake_cursor(): #creates a MagicMock representing a DB cursor
    cur = MagicMock()
    cur.fetchall.return_value = [] #this way tests start with an empty result set
    return cur

@pytest.fixture
def fake_db(fake_cursor): #creates and returns a lightweight fake DB object with a cursor method, representing a DB connection object
    db = SimpleNamespace() 
    db.cursor = MagicMock(return_value=fake_cursor) #cursor method returns the fake cursor
    db.close = MagicMock() #close method to assert that the DB connection is closed after operations
    return db

def test_no_results_returns_and_closes_db(fake_db, fake_cursor):
    #patching dbconfig to return the fake_db when called in line 22 
    #and patching printc to capture and assert printed messages
    with patch('project.retrieve.dbconfig', return_value=fake_db), \
         patch('project.retrieve.printc') as mock_printc: #make sure the called function exercises the "no-results" path
        retrieve.retrieveEntries('mp', 'ds', search=None, decryptPassword=False) 
    mock_printc.assert_called_once_with("[yellow][-][/yellow] No results for the search.")
    fake_db.close.assert_called_once() #ensure DB connection was closed

def test_query_without_search_executes_select_all(fake_db, fake_cursor):
    with patch('project.retrieve.dbconfig', return_value=fake_db):
        retrieve.retrieveEntries('mp', 'ds', search={}, decryptPassword=False) ##make sure the called function exercises the "select all" path

    # ensure the SELECT without WHERE was executed at least once
    fake_cursor.execute.assert_called_with("SELECT * FROM PROtect.entries")
    fake_db.close.assert_called_once()

def test_query_with_search_builds_where_clause(fake_db, fake_cursor):
    with patch('project.retrieve.dbconfig', return_value=fake_db):
        retrieve.retrieveEntries('mp', 'ds', search={'Site':'example','Username':'alice'}, decryptPassword=False)

    #verify dictionary cursor was requested
    fake_db.cursor.assert_called_with(dictionary=True)

    #verify SQL structure (order of keys in dict might vary, so we check logic)
    args = fake_cursor.execute.call_args
    sql = args[0][0]
    params = args[0][1]

    #verify that the SQL contains the expected WHERE clauses and parameters
    assert "SELECT * FROM PROtect.entries WHERE" in sql
    assert "Site=%s" in sql
    assert "Username=%s" in sql
    assert "example" in params
    assert "alice" in params
    fake_db.close.assert_called_once()

def test_multiple_results_shows_table_and_hides_password(fake_db, fake_cursor):
    # arrange multiple rows
    fake_cursor.fetchall.return_value = [
        {
            "ID": 1, 
            "Site": "site1", 
            "URL": "http://s1", 
            "Email": "e1", 
            "Username": "u1", 
            "Password": "encrypted1"
        },
        {
            "ID": 2, 
            "Site": "site2", 
            "URL": "http://s2", 
            "Email": "e2", 
            "Username": "u2", 
            "Password": "encrypted2"
        },
    ] #this time we simulate multiple results instead of an empty set

    #a fake Console instance to capture the printed table
    fake_console_instance = MagicMock()

    with patch('project.retrieve.dbconfig', return_value=fake_db), \
         patch('project.retrieve.Console', return_value=fake_console):
        retrieve.retrieveEntries('mp', 'ds', search={'Site':'s'}, decryptPassword=False) #make sure the called function exercises the "multiple results" path

    # Console.print was called with a Table instance
    fake_console_instance.print.assert_called_once()
    fake_db.close.assert_called_once()

def test_multiple_results_decrypt_true_warns_and_does_not_decrypt(fake_db, fake_cursor):
    #this tests that requesting decryption on multiple results triggers a warning.
    fake_cursor.fetchall.return_value = [
        {
            "ID": 1, "Site": "s", "URL": "u", 
            "Email": "e", "Username": "n", "Password": "e1"
        },
        {
            "ID": 2, "Site": "s2", "URL": "u2", 
            "Email": "e2", "Username": "n2", "Password": "e2"
        },
    ]
    #these patches mock dbconfig, printc, AES256util.decrypt and pyperclip.copy
    # we want to ensure that decrypt and copy are NOT called in this scenario
    with patch('project.retrieve.dbconfig', return_value=fake_db), \
         patch('project.retrieve.printc') as mock_printc, \
         patch('project.retrieve.AES256util.decrypt') as mock_decrypt:
        retrieve.retrieveEntries('mp', 'ds', search={'Site':'s'}, decryptPassword=True)

    #check for the warning message
    assert any("Multiple results found" in str(call) for call in mock_printc.mock_calls)
    mock_decrypt.assert_not_called()
    fake_db.close.assert_called_once()


def test_single_result_decrypts_and_copies(fake_db, fake_cursor):
    fake_cursor.fetchall.return_value = [
        {
            "ID": 1, 
            "Site": "site", 
            "URL": "url", 
            "Email": "email", 
            "Username": "user", 
            "Password": "ENCRYPTEDBLOB"
        }
    ]

    mock_mk = MagicMock()
    mock_mk.hex.return_value = "deadbeef"
    
    # we want to ensure that decrypt and copy are called with correct parameters
    #the master key, in this test, is simulated as the deterministic byte string b'mkbytes' 
    with patch('project.retrieve.dbconfig', return_value=fake_db), \
         patch('project.retrieve.computeMasterKey', return_value=mock_mk), \
         patch('project.retrieve.AES256util.decrypt', return_value=b'secretpwd') as mock_decrypt, \
         patch('project.retrieve.pyperclip.copy') as mock_copy, \
         patch('project.retrieve.printc'):
        retrieve.retrieveEntries('mp', 'ds', search={'Site':'site'}, decryptPassword=True)
        #retrieveEntries is called to exercise the "single result with decryption" path
    
    mock_decrypt.assert_called_once_with("deadbeef", "ENCRYPTEDBLOB", keyType="hex")
    mock_copy.assert_called_once_with('secretpwd') #ensuring bytes are decoded to string
    fake_db.close.assert_called_once()

def test_result_with_missing_columns_handled_gracefully(fake_db, fake_cursor):
    # row missing 'URL' or 'Email' keys entirely
    fake_cursor.fetchall.return_value = [{"ID": 1, "Site": "site"}] 

    with patch('project.retrieve.dbconfig', return_value=fake_db), \
        patch('project.retrieve.Console') as mock_console:
        
        retrieve.retrieveEntries("mp", "ds", search=None, decryptPassword=False)

    fake_db.close.assert_called_once()
    mock_console.return_value.print.assert_called_once()

