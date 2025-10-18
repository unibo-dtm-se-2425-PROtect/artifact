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
        printc("[green][+][/green] Connected to db")
        return db
    except Exception as e:
        printc("[red][!] An error occurred while trying to connect to the database [/red]")
        console.print_exception(show_locals=True)



