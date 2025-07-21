from utils.dbconfig import dbconfig #needed to establish connection with the database

#modules to be used in order to display the search results in a table-shaped format to the user
from rich import print as printc
from rich.console import Console
from rich.table import Table

from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.hash import SHA512
from Crypto.random import get_random_bytes

import utils.aesutil
