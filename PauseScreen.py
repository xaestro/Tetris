import sys, pygame
from Constants import *
from Screen import *

class PauseScreen(Screen):
    def __init__(self):
        self.title = "Pause"
        self.menu_options = []

        self.menu_options.append("Resume")
        self.menu_options.append("Restart")
        self.menu_options.append("Quit to Menu")
        self.menu_options.append("Exit Game")

        self.selected_option = 0

        self.background = pygame.Surface(SIZE, pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 200))
        
        Screen.__init__(self)

    def key_down_handler(self, key):
        if key == pygame.K_UP:
            self.selected_option = (self.selected_option - 1) % len(self.menu_options)
        if key == pygame.K_DOWN:
            self.selected_option = (self.selected_option + 1) % len(self.menu_options)
        if key == pygame.K_RETURN:
            if self.menu_options[self.selected_option] == "Resume":
                self.exit_screen()
            if self.menu_options[self.selected_option] == "Restart":
                self.exit_screen("GameScreen")
            if self.menu_options[self.selected_option] == "Quit to Menu":
                self.exit_screen("MenuScreen")
            if self.menu_options[self.selected_option] == "Exit Game":
                self.exit_screen("Exit")
        if key == pygame.K_ESCAPE:
            self.exit_screen()

    def draw(self, screen, font):
        screen.blit(self.background, (0, 0))
        screen.blit(font.render(self.title, True, WHITE), (WIDTH / 4, HEIGHT / 4))
        
        for menu_item in range(len(self.menu_options)):
            color = WHITE
            if self.selected_option == menu_item:
                color = GREEN
            screen.blit(font.render(self.menu_options[menu_item], True, color), (WIDTH / 4, HEIGHT / 2 + 22 * (menu_item + 1)))
        
        
