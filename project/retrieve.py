from project.dbconfig import dbconfig #needed to establish connection with the database
from project.add import computeMasterKey

#modules to be used in order to display the search results in a table-shaped format to the user
from rich import print as printc
from rich.console import Console
from rich.table import Table

import AES256util
import pyperclip

def retrieveEntries(mp, ds, search, decryptPassword = False):
    #search will contain the search fields that are inputted by the user and that we want to search in the database
    #decryptPassword is set to False for security reasons: it will be set to True only if the user explicitly wants it
    #if True, it will initiate the decryption operation on the needed password
    db = dbconfig()
    cursor = db.cursor(dictionary=True)

    query = "" #two cases to be considered: the user might either query the database without specifying any search field, or doing it instead.

    if not search:
        query = "SELECT * FROM PROtect.entries"
        cursor.execute(query)
    else: 
        conditions=[]
        values=[]
        for field, value in search.items():
            conditions.append(f"{field}=%s")
            values.append(value)
        query=f"SELECT * FROM PROtect.entries WHERE {' AND '.join(conditions)}"
        cursor.execute(query, tuple(values))

    results = cursor.fetchall()
    if not results:
        printc("[yellow][-][/yellow] No results for the search")
        db.close()
        return

    #handling the columns of the results table
    table = Table(title="Results")
    table.add_column("ID")
    table.add_column("Site")
    table.add_column("URL")
    table.add_column("Email")
    table.add_column("Username")
    table.add_column("Password") #never show plaintext by default
    
    if decryptPassword and len(results)==1:
        mk=computeMasterKey(mp,ds)
        mk_hex=mk.hex()
        decrypted=AES256util.decrypt(mk_hex, results[0]["Password"], keyType="hex").decode()
        pyperclip.copy(decrypted)
        printc("[green][+][/green] Password copied to clipboard")
    
    #Fill the table with masked passwords
    for row in results: 
        table.add_row(str(row["ID"]), row["Site"], row("URL", ""), row.get("Email", ""), row.get["Username"], "{hidden}")

    Console().print(table)
    db.close()
    return
