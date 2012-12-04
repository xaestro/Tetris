import pygame, random, GameBoard
from Constants import *

class GameScreen:
    def __init__(self):
        self.drop_piece = False
        self.move_dir = 0
        self.move_sideways_timer = 0
        self.move_timer = 500

        self.board = GameBoard.GameBoard()
        self.board.spawn_piece()

        self.level = 1
        self.lines_left = 4

        self.score = 0
        self.score_to_update = 0

    def key_down_handler(self, key):
        if key == pygame.K_LEFT:
            self.score_to_update += self.board.update_pieces([-1, 0])
            self.move_sideways_timer = 100
            self.move_dir = -1
        if key == pygame.K_RIGHT:
            self.score_to_update += self.board.update_pieces([1, 0])
            self.move_sideways_timer = 100
            self.move_dir = 1
        if key == pygame.K_DOWN:
            self.move_timer = 100
            self.drop_piece = True
        if key == pygame.K_SPACE:
            self.score_to_update += self.board.drop_piece()
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

    def new_level(self):
        self.level += 1
        self.lines_left += self.level * 4
        

    def update(self, elapsed_time):
        self.move_timer -= elapsed_time
        if self.move_timer < 0:
            self.score_to_update += self.board.update_pieces([0, -1])
            if self.drop_piece:
                self.move_timer = 50
            else:
                self.move_timer = 500
        if self.move_sideways_timer > 0:
            self.move_sideways_timer -= elapsed_time
        else:
            if self.move_dir != 0:
                self.score_to_update += self.board.update_pieces([self.move_dir, 0])
                self.move_sideways_timer = 150
        self.score += self.score_to_update
        self.lines_left -= self.score_to_update
        self.score_to_update = 0
        if self.lines_left <= 0:
            self.new_level()

    def draw(self, screen, font):
        for y in range(GAME_HEIGHT):
            for x in range(GAME_WIDTH):
                screen.fill(self.board.filled_blocks[y][x],\
                    pygame.Rect((BOARD_X + x * EDGE_LENGTH,\
                    BOARD_Y + (GAME_HEIGHT - y - 1) * EDGE_LENGTH),\
                    (EDGE_LENGTH, EDGE_LENGTH)))
                
        for block in self.board.game_piece.get_blocks():
            if block[1] < GAME_HEIGHT:
                screen.fill(self.board.game_piece.color,\
                         pygame.Rect((BOARD_X + block[0] * EDGE_LENGTH,\
                         BOARD_Y + (GAME_HEIGHT - block[1] - 1) * EDGE_LENGTH),\
                         (EDGE_LENGTH, EDGE_LENGTH)))
                
        screen.blit(font.render("Score: " + str(self.score), True, (255, 255, 255)), (0, 22))
        screen.blit(font.render("Level: " + str(self.level), True, (255, 255, 255)), (0, 44))
        screen.blit(font.render("Lines: " + str(self.lines_left), True, (255, 255, 255)), (0, 66))

        
