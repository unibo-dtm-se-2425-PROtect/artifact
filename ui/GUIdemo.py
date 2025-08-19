#demo for GUI to create an interactive exploration for visual/manual verification 
#It's not the TEST for GUI!
#demo does not need to be tested, we directly test the MVC in the tests package 

import ttkbootstrap as tb

class DemoController:
    def __init__(self, view):
        self.view=view
        self.entries=[
            ("GitHub", "https://github.com", "git@mail.com", "myuser"),
            ("Gmail", "https://gmail.com", "me@mail.com", "me"),
        ]
        self.refresh()
    
    