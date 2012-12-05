class Pieces(object):
    def __init__(self):
        self.edge_length = len(self.fill)

    def y_max(self):
        for y in range(self.edge_length - 1, -1, -1):
            for x in range(self.edge_length):
                if self.fill[y][x] == 1:
                    return self.position[1] + y
        raise Exception("No y max found", None)

    def y_min(self):
        for y in range(self.edge_length):
            for x in range(self.edge_length):
                if self.fill[y][x] == 1:
                    return self.position[1] + y
        raise Exception("No y min found", None)

    def x_max(self):
        for x in range(self.edge_length - 1, -1, -1):
            for y in range(self.edge_length):
                if self.fill[y][x] == 1:
                    return self.position[0] + x
        raise Exception("No x max found", None)
    
    def x_min(self):
        for x in range(self.edge_length):
            for y in range(self.edge_length):
                if self.fill[y][x] == 1:
                    return self.position[0] + x
        raise Exception("No x min found", None)
    
    def rotate_left(self):
        new_fill = []
        for y in range(self.edge_length):
            new_fill.append([])
            for x in range(self.edge_length):
                new_fill[y].insert(0, self.fill[x][y])
        self.fill = new_fill

    def rotate_right(self):
        new_fill = []
        for y in range(self.edge_length):
            new_fill.append([])
            for x in range(self.edge_length):
                new_fill[y].insert(0, self.fill[self.edge_length - 1 - x][self.edge_length - 1 - y])
        self.fill = new_fill

    def move(self, direction):
        self.position[0] += direction[0]
        self.position[1] += direction[1]

    def get_blocks(self):
        filled = []
        for y in range(self.edge_length):
            for x in range(self.edge_length):
                if self.fill[y][x] == 1:
                    filled.append([self.position[0] + x, self.position[1] + y])

        return filled                

class Long_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 0
        self.position = position
        self.color = 100, 150, 255
        self.fill = [[0, 1, 0, 0],\
                     [0, 1, 0, 0],\
                     [0, 1, 0, 0],\
                     [0, 1, 0, 0]]
        Pieces.__init__(self)

class T_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 1
        self.position = position
        self.color = 255, 0, 255
        self.fill = [[0, 0, 0],\
                     [1, 1, 1],\
                     [0, 1, 0]]
        Pieces.__init__(self)

class LRight_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 2
        self.position = position
        self.color = 255, 200, 100
        self.fill = [[0, 0, 0],\
                     [1, 1, 1],\
                     [1, 0, 0]]
        Pieces.__init__(self)

class LLeft_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 3
        self.position = position
        self.color = 0, 0, 255
        self.fill = [[0, 0, 0],\
                     [1, 1, 1],\
                     [0, 0, 1]]
        Pieces.__init__(self)

class ZRight_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 4
        self.position = position
        self.color = 150, 255, 150
        self.fill = [[0, 0, 0],\
                     [0, 1, 1],\
                     [1, 1, 0]]
        Pieces.__init__(self)

class ZLeft_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 5
        self.position = position
        self.color = 255, 0, 0
        self.fill = [[0, 0, 0],\
                     [1, 1, 0],\
                     [0, 1, 1]]
        Pieces.__init__(self)

class Square_Piece(Pieces):
    def __init__(self, position=(0,0)):
        self.piece_id = 6
        self.position = position
        self.color = 255, 255, 0
        self.fill = [[1, 1],\
                     [1, 1]]
        Pieces.__init__(self)

