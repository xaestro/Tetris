import sys, pygame, traceback, random
from pieces import *

SIZE = WIDTH, HEIGHT = 200, 600
BLACK = 0, 0, 0
GREY = 128, 128, 128

GAME_WIDTH = 10
GAME_HEIGHT = 30
TOP_BUFFER = 4

EDGE_LENGTH = WIDTH // GAME_WIDTH

TIMER_EVENT = pygame.USEREVENT + 1

class Tetris:

    def __init__(self):
        self.speed = [2, 2]

        self.END_GAME = 0
        self.RUN_GAME = 1
        self.game_state = self.RUN_GAME

        self.game_piece = None
        self.filled_blocks = [[False for i in range(GAME_WIDTH)] \
                                     for j in range(GAME_HEIGHT + TOP_BUFFER)]
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE)

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
        
    def check_collision(self, block_list):
        for block in block_list:
            if self.filled_blocks[block[1]][block[0]]:
                return True
        return False

    def fill_blocks(self):
        for n in self.game_piece.get_blocks():
            self.filled_blocks[n[1]][n[0]] = True
            if n[1] >= GAME_HEIGHT:
                for j in range(GAME_HEIGHT + TOP_BUFFER):
                    for i in range(GAME_WIDTH):
                        self.filled_blocks[j][i] = False
                break
        starting_row = -1
        rows_to_clear = 0
        for y in range(GAME_HEIGHT):
            clear_row = True
            for x in range(GAME_WIDTH):
                clear_row = clear_row and self.filled_blocks[y][x]
            if clear_row:
                if starting_row == -1:
                    starting_row = y
                rows_to_clear += 1
        for rows in range(starting_row, GAME_HEIGHT):
            for x in range(GAME_WIDTH):
                self.filled_blocks[rows][x] = self.filled_blocks[rows + rows_to_clear][x]
            
        self.spawn_piece()
    
    def update_pieces(self, direction):
        self.game_piece.move(direction)
        if direction[1] == -1:
            if self.game_piece.y_min() < 0 or \
                self.check_collision(self.game_piece.get_blocks()):
                    self.game_piece.move([0, 1])
                    self.fill_blocks()
                    
        else:    
            if self.game_piece.x_min() < 0 or \
               self.game_piece.x_max() >= GAME_WIDTH or \
               self.check_collision(self.game_piece.get_blocks()):
                self.game_piece.move([direction[0] * -1, 0])
                

    def update(self):
        self.spawn_piece()

        pygame.time.set_timer(TIMER_EVENT, 500)
        
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                   (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit(0)
                if event.type == TIMER_EVENT:
                    self.update_pieces([0, -1])
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.update_pieces([-1, 0])
                    if event.key == pygame.K_RIGHT:
                        self.update_pieces([1, 0])
                    if event.key == pygame.K_DOWN:
                        self.update_pieces([0, -1])
                    if event.key == pygame.K_SPACE:
                        #redundant code, fix this up later
                        while self.game_piece.y_min() >= 0 and \
                        not self.check_collision(self.game_piece.get_blocks()):
                            self.game_piece.move([0, -1])
                        self.game_piece.move([0, 1])
                        self.fill_blocks()
                    if event.key == pygame.K_z:
                        self.game_piece.rotate_left()
                        if self.game_piece.y_min() < 0:
                            self.game_piece.move([0, y_min()])
                        if self.game_piece.x_min() < 0 or \
                           self.game_piece.x_max() > GAME_WIDTH - 1:
                            self.game_piece.rotate_right()
                    if event.key == pygame.K_x or \
                       event.key == pygame.K_UP:
                        self.game_piece.rotate_right()
                        if self.game_piece.y_min() < 0:
                            self.game_piece.move([0, y_min()])
                        if self.game_piece.x_min() < 0 or \
                           self.game_piece.x_max() > GAME_WIDTH - 1:
                            self.game_piece.rotate_left()
                    if event.key == pygame.K_w:
                        self.spawn_piece()
            self.draw()

    def draw(self):
        self.screen.fill(BLACK)
        
        for block in self.game_piece.get_blocks():
            self.screen.fill(self.game_piece.color,\
                             pygame.Rect((block[0] * EDGE_LENGTH,\
                             (GAME_HEIGHT - block[1] - 1) * EDGE_LENGTH),\
                             (EDGE_LENGTH, EDGE_LENGTH)))

        for y in range(len(self.filled_blocks)):
            for x in range(len(self.filled_blocks[y])):
                if self.filled_blocks[y][x]:
                    self.screen.fill(GREY,\
                        pygame.Rect((x * EDGE_LENGTH,\
                        (GAME_HEIGHT - y - 1) * EDGE_LENGTH),\
                        (EDGE_LENGTH, EDGE_LENGTH)))
                    
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
