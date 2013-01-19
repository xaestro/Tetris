"""
Tetris in Python/Pygame

Just trying out my hand at making a complete tetris game in Python
"""

__author__ = "Tony Yang <xaestro>"
__date__   = "November 29, 2012"

import sys, pygame, traceback, SoundManager, ScreenManager
from Constants import *

class Tetris:

    def __init__(self):

        pygame.init()
        self.game_timer = pygame.time.Clock()
        self.game_time = 0
        self.screen = pygame.display.set_mode(SIZE, pygame.SRCALPHA)
        self.font = pygame.font.Font(pygame.font.match_font('arial'), 20)
        
        self.sound_manager = SoundManager.SoundManager()
        self.screen_manager = ScreenManager.ScreenManager(self)

    def get_screen(self):
        return self.screen

    def get_font(self):
        return self.font
    
    def update(self):
        
        while 1:
            elapsed_time = self.game_timer.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    self.screen_manager.key_down_handler(event.key)
                if event.type == pygame.KEYUP:
                    self.screen_manager.key_up_handler(event.key)
                    
            self.game_time += elapsed_time / 1000.0

            self.screen_manager.update(elapsed_time)
            self.draw()
            
        self.sound_manager.quit()

    def draw(self):
        self.screen.fill(GREY)

        self.screen_manager.draw()
        
        self.screen.blit(self.font.render(str(self.game_time), True, (255, 255, 255)), (0, HEIGHT - 22)) 
        
        pygame.display.flip()

if __name__ == '__main__':
    mainGame = Tetris()
    try:
        mainGame.update()
    except:
        if sys.exc_info()[0] != SystemExit:
            sys.stderr.write(traceback.print_exc())
            pygame.quit()
