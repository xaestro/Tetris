import pygame, random, GameBoard
from Constants import *
from Screen import *

class GameScreen(Screen):
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

        self.instructions = []
        self.instructions.append("Left/Right: Move sideways")
        self.instructions.append("Down: Increase drop speed")
        self.instructions.append("Up: Rotate Clockwise")
        self.instructions.append("Z: Rotate Counterclockwise")
        self.instructions.append("Space: Instant Drop")
        self.instructions.append("Shift: Store Current Piece")
        self.instructions.append("Escape: Exit to Menu")

        self.stored_piece = None

        Screen.__init__(self)

    def key_down_handler(self, key):
        if key == pygame.K_LEFT:
            self.score_to_update += self.board.update_pieces([-1, 0])
            self.move_sideways_timer = 125
            self.move_dir = -1
        if key == pygame.K_RIGHT:
            self.score_to_update += self.board.update_pieces([1, 0])
            self.move_sideways_timer = 125
            self.move_dir = 1
        if key == pygame.K_DOWN:
            self.score_to_update += self.board.update_pieces([0, -1])
            if 500 - 40 * self.level > 75:
                self.move_timer = 75
            self.drop_piece = True
        if key == pygame.K_SPACE:
            self.score_to_update += self.board.drop_piece()
            #self.game.sound_manager.swoosh_sound.play()
        if key == pygame.K_z:
            self.board.rotate_piece(False)
        if key == pygame.K_x or \
           key == pygame.K_UP:
            self.board.rotate_piece(True)
        if key == pygame.K_w:
            self.board.spawn_piece()
        if key == pygame.K_LSHIFT:
            self.board.swap_piece()
        if key == pygame.K_ESCAPE:
            self.add_screen("PauseScreen")

    def key_up_handler(self, key):
        if key == pygame.K_DOWN:
            self.move_timer = 500 - self.move_timer
            self.drop_piece = False
        if key == pygame.K_LEFT and \
           self.move_dir == -1 or \
           key == pygame.K_RIGHT and \
           self.move_dir == 1:
            self.move_dir = 0
            self.move_sideways_timer = 0

    def new_level(self):
        self.level += 1
        self.lines_left += self.level * 4
        

    def update(self, elapsed_time):
        self.move_timer -= elapsed_time
        if self.move_timer < 0:
            self.score_to_update += self.board.update_pieces([0, -1])
            if self.drop_piece:
                self.move_timer = 75
            else:
                self.move_timer = 500 - 40 * self.level
        if self.move_sideways_timer > 0:
            self.move_sideways_timer -= elapsed_time
        else:
            if self.move_dir != 0:
                self.score_to_update += self.board.update_pieces([self.move_dir, 0])
                self.move_sideways_timer = 75
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

        screen.fill(BLACK, pygame.Rect((BOARD_X + (GAME_WIDTH + 1) * EDGE_LENGTH,\
             BOARD_Y ), (6 * EDGE_LENGTH, 6 * EDGE_LENGTH)))

        if self.board.stored_piece != None:
            for block in self.board.stored_piece.get_blocks():
                screen.fill(self.board.stored_piece.color,\
                         pygame.Rect((BOARD_X + (GAME_WIDTH + 4 - self.board.stored_piece.edge_length / 2.0 + block[0]) * EDGE_LENGTH,\
                         BOARD_Y + (2 + self.board.stored_piece.edge_length / 2.0 - block[1]) * EDGE_LENGTH),\
                         (EDGE_LENGTH, EDGE_LENGTH)))
                
        screen.blit(font.render("Score: " + str(self.score), True, (255, 255, 255)), (0, 22))
        screen.blit(font.render("Level: " + str(self.level), True, (255, 255, 255)), (0, 44))
        screen.blit(font.render("Lines: " + str(self.lines_left), True, (255, 255, 255)), (0, 66))
        i = 0
        for text in self.instructions:
            screen.blit(font.render(text, True, (255, 255, 255)), (0, HEIGHT / 2 + 22 * i))
            i += 1

        
