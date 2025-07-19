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
  
