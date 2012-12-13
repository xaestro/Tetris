import sys
from Constants import *

class Screen:
    def __init__(self):
        self.exit = False
        self.add = False
        self.next_screen = ""

    def get_exit(self):
        return self.exit

    def get_next_screen(self):
        return self.next_screen

    def reset_add_screen(self):
        self.add = False
        self.next_screen = ""
    
    def get_add_screen(self):
        return self.add

    def exit_screen(self, next_screen=""):
        self.exit = True
        self.next_screen = next_screen

    def add_screen(self, next_screen=""):
        self.add = True
        self.next_screen = next_screen
        
    def key_down_handler(self, key):
        pass

    def key_up_handler(self, key):
        pass

    def update(self, elapsed_time):
        pass

    def draw(self, screen, font):
        pass
