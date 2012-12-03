"""
Tetris in Python/Pygame

Just trying out my hand at making a complete tetris game in Python
"""

__author__ = "Tony Yang <xaestro>"
__date__   = "November 29, 2012"

import sys, pygame, traceback, random, GameBoard
from Constants import *

class Tetris:

    def __init__(self):

        self.END_GAME = 0
        self.RUN_GAME = 1
        self.game_state = self.RUN_GAME

        self.drop_piece = False
        self.move_dir = 0
        self.move_sideways_timer = 0

        pygame.init()
        self.game_timer = pygame.time.Clock()
        self.game_time = 0
        self.screen = pygame.display.set_mode(SIZE)
        self.board = GameBoard.GameBoard()
        self.font = pygame.font.Font(pygame.font.match_font('arialms'), 20)
        self.scoreboard = pygame.Surface((200, 200))

        self.move_timer = 500
                
    def key_down_handler(self, key):
        if key == pygame.K_LEFT:
            self.board.update_pieces([-1, 0])
            self.move_sideways_timer = 150
            self.move_dir = -1
        if key == pygame.K_RIGHT:
            self.board.update_pieces([1, 0])
            self.move_sideways_timer = 150
            self.move_dir = 1
        if key == pygame.K_DOWN:
            self.move_timer = 100
            self.drop_piece = True
        if key == pygame.K_SPACE:
            self.board.drop_piece()
        if key == pygame.K_z:
            self.board.rotate_piece(False)
        if key == pygame.K_x or \
           key == pygame.K_UP:
            self.board.rotate_piece(True)
        if key == pygame.K_w:
            self.board.spawn_piece()

    def key_up_handler(self, key):
        if key == pygame.K_DOWN:
            self.move_timer = 500
            self.drop_piece = False
        if key == pygame.K_LEFT and \
           self.move_dir == -1 or \
           key == pygame.K_RIGHT and \
           self.move_dir == 1:
            self.move_dir = 0

    def update(self):
        self.board.spawn_piece()

        while 1:
            elapsed_time = self.game_timer.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    self.key_down_handler(event.key)
                if event.type == pygame.KEYUP:
                    self.key_up_handler(event.key)

            self.game_time += elapsed_time / 1000.0

            self.move_timer -= elapsed_time
            if self.move_timer < 0:
                self.board.update_pieces([0, -1])
                if self.drop_piece:
                    self.move_timer = 100
                else:
                    self.move_timer = 500
            if self.move_sideways_timer > 0:
                self.move_sideways_timer -= elapsed_time
            else:
                if self.move_dir != 0:
                    self.board.update_pieces([self.move_dir, 0])
                    self.move_sideways_timer = 150
                
                
            
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
        if sys.exc_info()[0] != SystemExit:
            sys.stderr.write(traceback.print_exc())
            pygame.quit()
