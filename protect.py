from ui.CONTROLLER.GUIcontroller import PasswordManagerController
import sys


if __name__ == "__main__":
    testmode = "--test" in sys.argv
    controller = PasswordManagerController(master_password="password")
    controller.view.mainloop()
