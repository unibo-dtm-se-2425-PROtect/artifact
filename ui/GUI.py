#Tkinter + ttkbootstrap (theme='vapor')
#Features:
  # -Login with Master Password (required on app open)
  # -Optional re-lock
  # -List entries in table (password never shown by default)
  # -Copy to clipboard (no on-screen reveal)
  # -Show Password (requires master password again) with 10s auto-hide
  # -Add, Edit, Delete entries (each requires master password confirmation)
  # -Generate password tool (length slider) + copy
  # -First-time Setup (GUI wrapper for config): create DB/tables + set master password
  # -Import/Export JSON (optional convenience)

from __future__ import allocations
import json
import os
import sys
import threading
import time
from dataclasses import asdict, dataclass
from typing import List, Optional, Tuple

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import StringVar, IntVar

import ttkbootstrap as tb
from ttkbootstrap.constants import *

#back-end imports for the project
try:
    from project.dbconfig import dbconfig
except Exception as e: 
    raise SystemExit("dbconfig.py not found or import error: " +str(e))

try: 
    from project.add import computeMasterKey
except Exception:
    #useful whether the user has not imported its own add.py which includes the PBKDF2 implementation 
    # so we use a local one directly imported from PyCryptodome
    from Crypto.Protocol.KDF import PBKDF2
    from Crypto.Hash import SHA256
    def computeMasterKey(mp, ds):
        return PBKDF2(mp.encode(), ds.encode(), 32, count=1_000_000, hmac_hash_module=SHA256)
    
try:
    import project.AES256util
except Exception as e:
    raise SystemExit("AES256util.py not found or import error: " + str(e))


