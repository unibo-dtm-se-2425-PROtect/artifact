from getpass import getpass
from rich import print as printc
from dbconfig import dbconfig
from AES256util import verify_master_password

def delete_entry(ID):
    #deletes an entry by its ID after confirming and verifying master password
    db = dbconfig()
    cursor = db.cursor()

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
        if not verify_master_password(mp):
            return

        delete_entry(ID)

    except Exception as e:
        printc(f"[red][!] Error during deletion: {e}[/red]")


if __name__ == "__main__":
    delete_entry_cli()