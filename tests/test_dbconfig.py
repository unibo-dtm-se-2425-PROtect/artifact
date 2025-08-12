import pytest
from unittest.mock import patch, MagicMock
from project.dbconfig import dbconfig 

@patch("project.dbconfig.mysql.connector.connect")
def test_dbconfig_success(mock_connect):
    mock_db=MagicMock()
    mock_connect.return_value=mock_db

    db=dbmod.dbconfig()

    