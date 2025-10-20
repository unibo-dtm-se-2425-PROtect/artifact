import pytest
from unittest.mock import patch, MagicMock
import project.add as add

from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA512
