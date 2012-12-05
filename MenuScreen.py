import sys, pygame, GameScreen
from Constants import *

class MenuScreen:
    def __init__(self):
        self.title = "Tony's Tetris Clone"
        self.menu_options = []

        self.menu_options.append("Start Game")
        self.menu_options.append("Exit Game")

        self.selected_option = 0
        self.next_screen = None

    def key_down_handler(self, key):
        if key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        if key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        if key == pygame.K_RETURN:
            if self.menu_options[self.selected_option] == "Start Game":
                self.next_screen = GameScreen.GameScreen
            if self.menu_options[self.selected_option] == "Exit Game":
                pygame.quit()
                sys.exit(0)
    def key_up_handler(self, key):
        pass

    def update(self, elapsed_time):
        pass

    def draw(self, screen, font):
        screen.blit(font.render(self.title, True, WHITE), (WIDTH / 4, HEIGHT / 4))
        
        for menu_item in range(len(self.menu_options)):
            color = WHITE
            if self.selected_option == menu_item:
                color = GREEN
            screen.blit(font.render(self.menu_options[menu_item], True, color), (WIDTH / 4, HEIGHT / 2 + 22 * (menu_item + 1)))
        
        
