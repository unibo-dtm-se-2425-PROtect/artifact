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
        self.cursor.execute("SELECT masterpassword_hash, device_secret FROM PROtect.secrets WHERE username=%s", (username,))
        row=self.cursor.fetchone()
        return row #returns None if the user is not found
    
    def create_new_user(self, username:str, masterpassword_hash:str, device_secret:str):
        #insert new user's secrets into the secrets table. The hashing is done by the controller 
        self.cursor.execute("INSERT INTO PROtect.secrets (username, masterpassword_hash, device_secret) VALUES (%s,%s,%s)", (username, masterpassword_hash, device_secret))
        self.db.commit()
    
    def close(self):
        self.cursor.close()
        self.db.close()




