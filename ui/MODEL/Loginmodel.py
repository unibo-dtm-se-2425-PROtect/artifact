from project.dbconfig import dbconfig
from typing import Optional, Tuple

class LoginModel:
    #handles DB ops specific to user authentication (fetch secrets and create new user records)
    def __init__(self):
        #connect to running DB on local host
        self.db=dbconfig()
        self.cursor=self.db.cursor()
    
    def get_user_secrets(self, username:str) -> Optional[Tuple[str, str]]:
        #retrieve the stored mp hash and ds for a given username from the secrets table
        self.cursor.execute("SELECT mp, ds FROM PROtect.secrets WHERE username=%s", (username,))
        row=self.cursor.fetchone()
        return row #returns None if the user is not found
    
    def create_new_user(self, username:str, derived_key_hex:str, salt:str):
        #insert new user's secrets into the secrets table. The hashing is done by the controller 
        self.cursor.execute("INSERT INTO PROtect.secrets (username, pm, ds) VALUES (%s,%s,%s)", (username, derived_key_hex, salt))
        self.dbcommit()
    
    def close(self):
        self.cursor.close()
        self.db.close()




