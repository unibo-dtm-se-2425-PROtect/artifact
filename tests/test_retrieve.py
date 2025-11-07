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




