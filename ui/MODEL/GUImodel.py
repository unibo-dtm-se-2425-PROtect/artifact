import random, string
from typing import Tuple, List, Optional
import mysql.connector
from project.dbconfig import dbconfig
from project import AES256util
from project.add import computeMasterKey

class PasswordManagerModel:
    #Establish DB connection
    def __init__(self):
        self.db = dbconfig()
        self.cursor = self.db.cursor()
        self.__init__schema()
        
    #Model to manage password entries (tuples)
    def __init__(self):
        self.entries:List[Tuple[str,str,str,str,str]]=[]
    
    def get_entries(self) -> List[Tuple[str,str,str,str,str]]:
        return self.entries #returns all stored entries
    
    def add_entry(self, site:str, URL:str, email:str, username:str, password:str):
        self.entries.append((site, URL, email, username, password))
    
    def edit_entry(self, index:int, site:str, url:str, email:str, username:str, password:str):
        if 0<=index<len(self.entries):
            self.entries[index]=(site,url,email,username,password)
    
    def delete_entry(self, index:int):
        if 0<=index<len(self.entries):
            del self.entries[index]
    
    def generate_password(self, length: int=12, use_symbols:bool=True) -> str:
        chars = string.ascii_letters + string.digits
        if use_symbols:
            chars += string.punctuation
        return ''.join(random.choices(chars, k=length))
    
    def export_to_file(self, filepath:str):
        #Export entries to a simple CSV file (demo purpose)
        import csv
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Site", "URL", "Email", "Username", "Password"])
            writer.writerows(self.entries)
    
    def import_from_file(self, filepath:str):
        import csv
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if len(row) == 5:
                    self.entries.append(tuple(row))
    
    


