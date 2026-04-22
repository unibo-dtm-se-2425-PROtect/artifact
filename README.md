# PROtect - Password Manager

PROtect, a desktop password manager designed to securely store, retrieve, modify, and manage credentials.
The alternation between uppercase and lowercase letters in the name highlights the core idea of the project: protection. At the same time, “PRO” recalls efficiency and proficiency, while “tect” evokes technology and structure. 

## 📁 Project Structure
```text
unibo-dtm-se-2425-PROtect/
├── artifact/                                  # Code         
  ├── .github/workflows                                  
    ├── check.yml
    └── deploy.yml
  ├── .vscode/
    └── launch.json
  ├──devtools/
    ├── GUIdemo.py                             # GUI demo to test functionalities without real logic and calls to db
    └── __init__.py                            # __init__.py to recognize folders as packages
  ├── project                                  # start of main code base in python
    ├── AES256util.py                          # existing libraries set to use cryptography 
    ├── __init__.py
    ├── add.py                                 # ADD new entry functionality
    ├── config.py                              # (first) configuration, reconfiguration and delete configuration functionalities 
    ├── dbconfig.py                            # configuration of the connection to MySQL database
    ├── delete.py                              # DELETE entry functionality
    ├── export.py                              # EXPORT entries functionality into csv files
    ├── importf.py                             # IMPORT entries from external csv ("f" added to avoid conflict with "import" statement in python)
    ├── modify.py                              # MODIFY entry functionality
    ├── pm.py                                  # password manager functionalities for CLI 
    └── retrieve.py                            # RETRIEVE entry by ID functionality 
  ├── tests/                                   # TEST SUITE for all files said above
    ├── __init__.py
    ├── test_AES256util.py
    ├── test_add.py
    ├── test_config.py
    ├── test_dbconfig.py
    ├── test_delete.py
    ├── test_export.py
    ├── test_importf.py
    ├── test_modify.py
    ├── test_pm.py
    └── test_retrieve.py
  ├── ui/                                      # GUI UI divided into MVC pattern
    ├── CONTROLLER/                            # glue between model and view, coordinator that handles interactions 
      ├── GUIcontroller.py
      ├── Logincontroller.py
      └── __init__.py
    ├── MODEL/                                 # data and business logic 
      ├── GUImodel.py
      ├── Loginmodel.py
      └── __init__.py
    ├── VIEW/                                  # the interface the user sees on the screen, no logic 
      ├── GUIview.py
      ├── Loginview.py
      └── __init__.py
  └── __init__.py
├── .gitattributes                             # set of necessary, good-practice files 
├── .gitignore
├── .mypy.ini
├── .python-version
├── CHANGELOG.md                               # automatic update of release version based on SemVer
├── LICENSE.md
├── MANIFEST.in                                # defines packages to exlude or include in releases 
├── README.md
├── VERSION
├── package-lock.json
├── package.json
├── protect.py                                 # ENTRY-POINT to activate GUI Login + Main App after authentication 
├── pyproject.toml
├── release.config.js
├── renovate.js
├── requirements-dev.txt
├── requirements.txt
└── setup.py
```
