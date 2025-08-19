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
    
    

