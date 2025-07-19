from getpass import getpass
from Crypto.Protocol.KDF import PBKDF2
from Crypto.hash import SHA512
from Crypto.random import get_random_bytes

import utils.aesutil

#function to comupute the masterkey from the masterPassword (mp) and the the deviceSecret (ds)
def computeMasterKey(mp,ds): 
  password = mp.encode() #encoding the mp and save it as password
  salt = ds.encode() #encoding the ds and save it as salt
  #using the PBDKF2 function from the Crypto.protocol module to derive a strong key from the two input values
  key = PBKDF2(password, salt, 32, count=1000000, hmac_hash_module=SHA512) #(mp, ds, length_key, nrRoundsforAESstrengthening, hashFunctionSpecification)
  return key

def addEntry(mp, ds, sitename, siteurl, email, username): 
  #get the password
  password = getpass("Password: ")

  mk = computeMasterKey(mp,ds): #mk stands for masterKey

  #using imported aesutil function to encrypt the mk 
  #this should return the encrypted password in base 64 encoded format
  encrypted = utils.aesutil.encrypt(key=mk, source=password, keyType="bytes")

  #add the new password to the database
  db = dbconfig()
  cursor = db.cursor()
  query = "INSERT INTO pm.entries (sitename, siteurl, email, username, password) values (%s, %s, %s, %s, %s)"
  val = (sitename.siteurl,email.username.encrypted)
  cursor.execute(query, val)
  db.commit()

printc("[green][+][/green] Added entry ")
