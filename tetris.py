"""
Tetris in Python/Pygame

Just trying out my hand at making a complete tetris game in Python
"""

__author__ = "Tony Yang <xaestro>"
__date__   = "November 29, 2012"

import sys, pygame, traceback, GameScreen
from Constants import *

class Tetris:

    def __init__(self):

        self.END_GAME = 0
        self.RUN_GAME = 1
        self.game_state = self.RUN_GAME

        pygame.init()
        self.game_timer = pygame.time.Clock()
        self.game_time = 0
        self.screen = pygame.display.set_mode(SIZE)
        self.font = pygame.font.Font(pygame.font.match_font('arialms'), 20)
        
                
        self.current_screen = GameScreen.GameScreen()

    def update(self):

        while 1:
            elapsed_time = self.game_timer.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    self.current_screen.key_down_handler(event.key)
                if event.type == pygame.KEYUP:
                    self.current_screen.key_up_handler(event.key)

            self.game_time += elapsed_time / 1000.0

            self.current_screen.update(elapsed_time)
            self.draw()

    def draw(self):
        self.screen.fill(GREY)

        self.current_screen.draw(self.screen, self.font)
        
        self.screen.blit(self.font.render(str(self.game_time), True, (255, 255, 255)), (0, 0)) 
        
        pygame.display.flip()

if __name__ == '__main__':
    mainGame = Tetris()
    try:
        mainGame.update()
    except:
        if sys.exc_info()[0] != SystemExit:
            sys.stderr.write(traceback.print_exc())
            pygame.quit()
