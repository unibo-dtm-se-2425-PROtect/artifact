from rich import print as printc
from dbconfig import dbconfig
from add import computeMasterKey
import AES256util
from AES256util import verify_master_password

def modify_entry(ID, site, url, email, username, password, mp, ds):
    #Modify one or more fields of an existing entry
    if not verify_master_password(username, mp, ds):
        return
    
    try:
        db = dbconfig()
        if not db:
            printc("[red][!] Could not connect to database[/red]")
            return

        cursor = db.cursor()

        mk = computeMasterKey(mp, ds)
        enc_pass = AES256util.encrypt(mk, password, keyType="hex")

        query = "UPDATE PROtect.entries SET Site=%s, URL=%s, Email=%s, Username=%s, Password=%s WHERE ID=%s"
        cursor.execute(query, (site, url, email, username, enc_pass, ID))
        db.commit()
        printc(f"[green][+][/green] Entry with ID {ID} updated successfully")

    except Exception as e:
        printc(f"[red][!] Error updating entry: {e}[/red]")
    
    db.close()
    
def modify_entry_cli():
    #CLI handler for modifying an entry.
    #Asks for ID, fields to update, and master password.
    try:
        ID = input("Enter the ID of the entry to modify: ").strip()
        if not ID.isdigit():
            printc("[red][!] Invalid ID. Must be a number.[/red]")
            return

        site = input("Site: ").strip()
        url = input("URL: ").strip()
        email = input("Email: ").strip()
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        mp_ds = AES256util.verify_master_password(getpass("Enter your MASTER PASSWORD: "))
        if not mp_ds:
            return
        mp, ds = mp_ds

        modify_entry(ID, site, url, email, username, password, mp, ds)

    except Exception as e:
        printc(f"[red][!] Error during CLI modification: {e}[/red]")


if __name__ == "__main__":
    from getpass import getpass
    modify_entry_cli()