import sys, pygame, Screen, GameScreen, MenuScreen, PauseScreen

SCREENS = { "MenuScreen": MenuScreen.MenuScreen,
            "GameScreen": GameScreen.GameScreen,
            "PauseScreen": PauseScreen.PauseScreen }

class ScreenManager:
    def __init__(self, game):
        self.screen_stack = []
        self.screen_stack.append(SCREENS["MenuScreen"]())
        self.game = game

    def add_screen(self):
        old_screen = self.get_top_screen()
        self.screen_stack.append(SCREENS[old_screen.get_next_screen()]())
        old_screen.reset_add_screen()

    def switch_screen(self):
        old_screen = self.get_top_screen()
        self.screen_stack = []
        self.screen_stack.append(SCREENS[old_screen.get_next_screen()]())

    def remove_top_screen(self):
        self.screen_stack.pop()

    def get_top_screen(self):
        return self.screen_stack[len(self.screen_stack) - 1]

    def exit_screen(self):
        if self.get_top_screen().get_next_screen() == "Exit":
            pygame.quit()
            sys.exit(0)
        elif self.get_top_screen().get_next_screen() == "":
            self.remove_top_screen()
        else:
            self.switch_screen()
        
    def key_down_handler(self, key):
        self.get_top_screen().key_down_handler(key)

    def key_up_handler(self, key):
        self.get_top_screen().key_up_handler(key)
        
    def update(self, elapsed_time):
        self.get_top_screen().update(elapsed_time)
        if self.get_top_screen().get_exit():
            self.exit_screen()
        if self.get_top_screen().get_add_screen():
            self.add_screen()

    def draw(self):
        for screen in self.screen_stack:
            screen.draw(self.game.get_screen(), self.game.get_font())
