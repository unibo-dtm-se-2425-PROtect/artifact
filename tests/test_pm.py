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
