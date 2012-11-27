"""
Tetris in Python/Pygame

Just trying out my hand at making a complete tetris game in Python
"""

__author__ = "Tony Yang <xaestro>"
__date__   = "November 19, 2012"

import sys, pygame, traceback, random
from Constants import *
from GameBoard import *

class Tetris:

    def __init__(self):

        self.END_GAME = 0
        self.RUN_GAME = 1
        self.game_state = self.RUN_GAME

        pygame.init()
        self.game_timer = pygame.time.Clock()
        self.game_time = 0
        self.screen = pygame.display.set_mode(SIZE)
        self.board = GameBoard()
        self.font = pygame.font.Font(pygame.font.match_font('arialms'), 20)
        self.scoreboard = pygame.Surface((200, 200))

        self.move_timer = 500
                
    def key_handler(self, key):
        if key == pygame.K_LEFT:
            self.board.update_pieces([-1, 0])
        if key == pygame.K_RIGHT:
            self.board.update_pieces([1, 0])
        if key == pygame.K_DOWN:
            self.board.update_pieces([0, -1])
        if key == pygame.K_SPACE:
            #redundant code, fix this up later
            while self.board.game_piece.y_min() >= 0 and \
            not self.board.check_collision():
                self.board.game_piece.move([0, -1])
            self.board.game_piece.move([0, 1])
            self.board.fill_blocks()
        if key == pygame.K_z:
            self.board.rotate_game_piece(False)
        if key == pygame.K_x or \
           key == pygame.K_UP:
            self.board.rotate_game_piece(True)
        if key == pygame.K_w:
            self.board.spawn_piece()



    def update(self):
        self.board.spawn_piece()
        
        self.move_timer = 500
        
        while 1:
            elapsed_time = self.game_timer.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    self.key_handler(event.key)

            self.game_time += elapsed_time / 1000.0

            self.move_timer -= elapsed_time
            if self.move_timer < 0:
                self.board.update_pieces([0, -1])
                self.move_timer = 500
                
            
            self.draw()

    def draw(self):
        self.screen.fill(GREY)

        for y in range(GAME_HEIGHT):
            for x in range(GAME_WIDTH):
                self.screen.fill(self.board.filled_blocks[y][x],\
                    pygame.Rect((BOARD_X + x * EDGE_LENGTH,\
                    BOARD_Y + (GAME_HEIGHT - y - 1) * EDGE_LENGTH),\
                    (EDGE_LENGTH, EDGE_LENGTH)))
                
        for block in self.board.game_piece.get_blocks():
            if block[1] < GAME_HEIGHT:
                self.screen.fill(self.board.game_piece.color,\
                         pygame.Rect((BOARD_X + block[0] * EDGE_LENGTH,\
                         BOARD_Y + (GAME_HEIGHT - block[1] - 1) * EDGE_LENGTH),\
                         (EDGE_LENGTH, EDGE_LENGTH)))

        self.screen.blit(self.font.render(str(self.game_time), True, (255, 255, 255)), (0, 0)) 
        
        pygame.display.flip()

if __name__ == '__main__':
    mainGame = Tetris()
    try:
        mainGame.update()
    except:
        sys.stderr.write(traceback.print_exc())
        if sys.exc_info()[0] != SystemExit:
            pygame.quit()
            sys.exit(0)
