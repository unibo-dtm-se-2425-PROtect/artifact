from getpass import getpass
from rich import print as printc
from dbconfig import dbconfig
import hashlib

def delete_entry(ID, mp, ds):
    #deletes and entry by its ID after confirming and verifying master password
    db = dbconfig()
    cursor = db.cursor()

    #Retrieve the stored hash and device secret from database
    cursor.execute("SELECT masterpassword_hash, device_secret FROM PROtect.secrets")
    result = cursor.fetchone()

    if not result:
        printc("[red][!] No master password configuration found.[/red]")
        db.close()
        return

    stored_hash, stored_ds = result

    #Check if the device secret matches
    if ds != stored_ds:
        printc("[red][!] Device secret mismatch. Operation aborted.[/red]")
        db.close()
        return

    #Hash provided master password and compare
    hashed_mp = hashlib.sha256(mp.encode()).hexdigest()

    if hashed_mp != stored_hash:
        printc("[red][!] Wrong master password. Deletion not authorized.[/red]")
        db.close()
        return

    #Confirm deletion
    confirm = input(f"Are you sure you want to delete entry with ID {ID}? (y/N): ").strip().lower()
    if confirm != "y":
        printc("[yellow][-][/yellow] Deletion cancelled.")
        db.close()
        return

    #Perform deletion
    cursor.execute("DELETE FROM PROtect.entries WHERE ID=%s", (ID,))
    db.commit()

    if cursor.rowcount > 0:
        printc(f"[green][+][/green] Entry with ID {ID} successfully deleted.")
    else:
        printc("[yellow][-][/yellow] No entry found with the provided ID.")

    db.close()


def delete_entry_cli():
    #CLI handler to delete an entry.
    #It asks for ID, confirmation, and master password.
    try:
        ID = input("Enter the ID of the entry to delete: ").strip()
        if not ID.isdigit():
            printc("[red][!] Invalid ID. Must be a number.[/red]")
            return

        # Ask for master password before proceeding
        mp = getpass("Enter your MASTER PASSWORD: ")
        ds = get_device_secret()  # Get from DB

        delete_entry(ID, mp, ds)

    except Exception as e:
        printc(f"[red][!] Error during deletion: {e}[/red]")


def get_device_secret():
    #Helper to fetch device secret from the PROtect.secrets table.
    db = dbconfig()
    cursor = db.cursor()
    cursor.execute("SELECT device_secret FROM PROtect.secrets")
    result = cursor.fetchone()
    db.close()
    return result[0] if result else None


if __name__ == "__main__":
    delete_entry_cli()