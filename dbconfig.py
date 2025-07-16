import mysql.connector 
from rich.console import Console 
console = Console()

def dbconfig(): 
  try: 
    db = mysql.connector.connect(
      host="localhost",
      user="pm",
      pass="password"
      )
except Exception as e:
    console.print_exception(show_locals=True)

return db


