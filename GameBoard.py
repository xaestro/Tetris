import random
from Pieces import *
from Constants import *

class GameBoard:
    def __init__(self):
        
        self.game_piece = None
        self.filled_blocks = [[BLACK for i in range(GAME_WIDTH)] \
                                     for j in range(GAME_HEIGHT + TOP_BUFFER)]
        
    
    def spawn_piece(self):
        num = random.randrange(7)
        if num == 0:
            piece = Long_Piece
        elif num == 1:
            piece = T_Piece
        elif num == 2:
            piece = LRight_Piece
        elif num == 3:
            piece = LLeft_Piece
        elif num == 4:
            piece = ZRight_Piece
        elif num == 5:
            piece = ZLeft_Piece
        elif num == 6:
            piece = Square_Piece
        self.game_piece = piece([GAME_WIDTH // 2 - 2, GAME_HEIGHT - 1])

    def check_collision(self):
        for block in self.game_piece.get_blocks():
            if block[1] < 0 or \
               block[0] > GAME_WIDTH - 1 or \
               block[0] < 0 or \
               self.filled_blocks[block[1]][block[0]] != BLACK:
                #print str(block[0]), str(block[1])
                return True
        return False
    
    def fill_blocks(self):
        for n in self.game_piece.get_blocks():
            self.filled_blocks[n[1]][n[0]] = self.game_piece.color
            if n[1] >= GAME_HEIGHT:
                for j in range(GAME_HEIGHT + TOP_BUFFER):
                    for i in range(GAME_WIDTH):
                        self.filled_blocks[j][i] = BLACK
                break
        rows_to_drop = []
        for y in range(GAME_HEIGHT):
            clear_row = True
            for x in range(GAME_WIDTH):
                clear_row = clear_row and (self.filled_blocks[y][x] != BLACK)
            if clear_row:
                rows_to_drop.append(y + 1)
        line_drop = 0
        if len(rows_to_drop) > 0:
            for rows in range(rows_to_drop[0], GAME_HEIGHT + TOP_BUFFER - 1):
                for x in range(GAME_WIDTH):
                    if len(rows_to_drop) > 0 and rows == rows_to_drop[0]:
                        rows_to_drop.pop(0)
                        line_drop += 1
                    self.filled_blocks[rows - line_drop][x] = self.filled_blocks[rows][x]
            
        self.spawn_piece()

    def rotate_piece(self, right):
        if right:
            self.game_piece.rotate_right()
        else:
            self.game_piece.rotate_left()
        rotate_back = False
        if self.game_piece.y_min() < 0:
            y = self.game_piece.y_min()
            self.game_piece.move([0, -y])
            if self.check_collision():
                self.game_piece.move([0, y])
                rotate_back = True
        if self.game_piece.x_min() < 0:
            x = 0 - self.game_piece.x_min()
            self.game_piece.move([x, 0])
            if self.check_collision():
                self.game_piece.move([-x, 0])
                rotate_back = True
        if self.game_piece.x_max() > GAME_WIDTH - 1:
            x = GAME_WIDTH - 1 - self.game_piece.x_max()
            self.game_piece.move([x, 0])
            if self.check_collision():
                self.game_piece.move([-x, 0])
                rotate_back = True
        if self.check_collision():
            rotate_back = True
        if rotate_back:
            if right:
                self.game_piece.rotate_left()
            else:
                self.game_piece.rotate_right()

    def drop_piece(self):
        while self.game_piece.y_min() >= 0 and \
        not self.check_collision():
            self.game_piece.move([0, -1])
        self.game_piece.move([0, 1])
        self.fill_blocks()
         
    def update_pieces(self, direction):
        self.game_piece.move(direction)
        if direction[1] == -1:
            if self.game_piece.y_min() < 0 or \
                self.check_collision():
                    self.game_piece.move([0, 1])
                    self.fill_blocks()
                    
        else:    
            if self.game_piece.x_min() < 0 or \
               self.game_piece.x_max() >= GAME_WIDTH or \
               self.check_collision():
                self.game_piece.move([direction[0] * -1, 0])

    def fill_test(self):
        for y in range(6):
            for x in range(GAME_WIDTH - 1):
                self.filled_blocks[y][x] = GREY
        self.filled_blocks[1][1] = BLACK
        self.filled_blocks[1][3] = BLACK
        self.filled_blocks[3][2] = BLACK
        self.game_piece = Long_Piece([GAME_WIDTH // 2 - 2, GAME_HEIGHT - 1])
