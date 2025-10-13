import csv
from getpass import getpass
from rich import print as printc
from dbconfig import dbconfig
from AES256util import verify_master_password, decrypt

def export_entries(filepath, masterkey):
    #Export entries to a CSV file decrypting password
    try:
        db = dbconfig()
        if not db:
            printc("[red][!] Could not connect to database[/red]")
            return

        cursor = db.cursor()
        cursor.execute("SELECT ID, Site, URL, Email, Username, password FROM PROtect.entries")
        rows = cursor.fetchall()

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Site", "URL", "Email", "Username", "password (decrypted)"])
            for r in rows:
                writer.writerow([r[0], r[1], r[2], r[3], r[4], r[5]])

        printc(f"[green][+][/green] Entries exported to [cyan]{filepath}[/cyan]")

    except Exception as e:
        printc(f"[red][!] Error during export: {e}[/red]")
    db.close()

def export_entries_cli():
    #CLI handler for exporting entries
    try:
        filepath = input("Enter the path where you want to save the CSV file: ").strip()
        if not filepath:
            printc("[red][!] File path cannot be empty.[/red]")
            return

        master_password = getpass("Enter your MASTER PASSWORD: ")
        if not verify_master_password(master_password):
            return 

        export_entries(filepath, master_password)

    except Exception as e:
        printc(f"[red][!] Export error: {e}[/red]")


if __name__ == "__main__":
    export_entries_cli()
