import mysql.connector 
from rich.console import Console 
from rich import print as printc
console = Console()

def dbconfig(): 
    try: 
        db = mysql.connector.connect(
          host="localhost",
          user="pm",
          password="password"
          )
    except Exception as e:
        console.print_exception(show_locals=True)

    return db


