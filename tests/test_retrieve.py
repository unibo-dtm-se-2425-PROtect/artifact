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
        retrieve.retrieveEntries(b'mp', b'ds', search=None, decryptPassword=False) 
    mock_printc.assert_called_once_with("[yellow][-][/yellow] No results for the search")
    fake_db.close.assert_called_once() #ensure DB connection was closed

def test_query_without_search_executes_select(fake_db, fake_cursor):
    with patch('project.retrieve.dbconfig', return_value=fake_db):
        retrieve.retrieveEntries(b'mp', b'ds', search={}, decryptPassword=False) ##make sure the called function exercises the "select all" path

    # ensure the SELECT without WHERE was executed at least once
    assert any("SELECT * FROM PROtect.entries" in call[0][0] for call in fake_cursor.execute.call_args_list)
    fake_db.close.assert_called_once()

def test_query_with_search_builds_where_clause(fake_db, fake_cursor):
    with patch('project.retrieve.dbconfig', return_value=fake_db):
        retrieve.retrieveEntries(b'mp', b'ds', search={'site':'example','username':'alice'}, decryptPassword=False)
    # verify the SELECT with WHERE clause was executed at least once
    expected = "SELECT * FROM PROtect.entries WHERE site=%s AND username=%s"
    assert any(call_args[0][0] == expected or expected in call_args[0][0] for call_args in fake_cursor.execute.call_args_list)
    # assert that the tuple below was used as parameters to an execute call
    assert any(call_args[0][1] == ('example','alice') for call_args in fake_cursor.execute.call_args_list if len(call_args[0]) > 1)
    fake_db.close.assert_called_once()

def test_multiple_results_shows_table_and_hides_password(fake_db, fake_cursor):
    # arrange multiple rows
    fake_cursor.fetchall.return_value = [
        ('site1','http://s1','e1','u1', b'encrypted1'),
        ('site2','http://s2','e2','u2', b'encrypted2'),
    ] #this time we simulate multiple results instead of an empty set

    #a fake Console instance to capture the printed table
    fake_console_instance = MagicMock()
    FakeConsole = MagicMock(return_value=fake_console_instance)

    with patch('project.retrieve.dbconfig', return_value=fake_db), \
         patch('project.retrieve.Console', FakeConsole):
        retrieve.retrieveEntries(b'mp', b'ds', search={'site':'s'}, decryptPassword=False) #make sure the called function exercises the "multiple results" path

    # Console.print was called with a Table instance
    fake_console_instance.print.assert_called_once()
    fake_db.close.assert_called_once()

ef test_multiple_results_decrypt_true_warns_and_does_not_decrypt(fake_db, fake_cursor):
    fake_cursor.fetchall.return_value = [
        ('s','u','e','n', b'e1'),
        ('s2','u2','e2','n2', b'e2'),
    ]
    #these patches mock dbconfig, printc, AES256util.decrypt and pyperclip.copy
    # we want to ensure that decrypt and copy are NOT called in this scenario
    with patch('project.retrieve.dbconfig', return_value=fake_db), \
         patch('project.retrieve.printc') as mock_printc, \
         patch('project.retrieve.AES256util.decrypt') as mock_decrypt, \
         patch('project.retrieve.pyperclip.copy') as mock_copy:
        retrieve.retrieveEntries(b'mp', b'ds', search={'site':'s'}, decryptPassword=True)

    mock_printc.assert_any_call("[yellow][-][/yellow] More than one result found from the search, therefore not extracting the password. Please, be more specific")
    #ensure that printc was called with the warning message specific to multiple results, and that the password decryption and clipboard copy were NOT attempted
    mock_decrypt.assert_not_called() #assert decryption was not attempted
    mock_copy.assert_not_called() #assert clipboard copy was not attempted
    fake_db.close.assert_called_once()






