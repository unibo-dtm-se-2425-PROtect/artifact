import csv
from getpass import getpass
from rich import print as printc
from dbconfig import dbconfig
from add import computeMasterKey
import AES256util
from AES256util import verify_master_password


def import_entries(filepath, mp, ds):
    #Import entries from a CSV file into the PROtect.entries table
    db = dbconfig()
    cursor = db.cursor()

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None) #skips header

            imported = 0
            for row in reader:
                if len(row) < 6:
                    continue  #skips incomplete rows

                ID, site, url, email, username, password_plain = row
                mk = computeMasterKey(mp, ds)
                enc_pass = AES256util.encrypt(mk, password_plain, keyType="hex")

                cursor.execute(
                    "INSERT INTO PROtect.entries (ID, Site, URL, Email, Username, password) VALUES (%s,%s,%s,%s,%s,%s)",
                    (ID, site, url, email, username, enc_pass)
                )
                imported += 1

            db.commit()
            printc(f"[green][+][/green] Imported {imported} entries from {filepath}")

    except FileNotFoundError:
        printc(f"[red][!] File not found: {filepath}[/red]")
    except Exception as e:
        printc(f"[red][!] Error during import: {e}[/red]")
    db.close()


def import_entries_cli():
    #CLI handler for importing entries
    try:
        filepath = input("Enter the path to the CSV file to import: ").strip()
        if not filepath:
            printc("[red][!] File path cannot be empty.[/red]")
            return

        master_password = getpass("Enter your MASTER PASSWORD: ")
        if not verify_master_password(master_password):
            return 

        import_entries(filepath, master_password)

    except Exception as e:
        printc(f"[red][!] Import error: {e}[/red]")


if __name__ == "__main__":
    import_entries_cli()