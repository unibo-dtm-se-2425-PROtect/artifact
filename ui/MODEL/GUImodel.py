import random, string
from typing import Tuple, List, Optional

class PasswordManagerModel:
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
    
    

