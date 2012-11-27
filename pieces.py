class Pieces(object):
    def __init__(self):
        self.position = [0, 0]
        self.color = 0, 0, 0
        self.fill = [[0 for m in range(4)] for n in range(4)]

    def y_max(self):
        for y in range(len(self.fill) - 1, -1, -1):
            for x in range(len(self.fill[y])):
                if self.fill[y][x] == 1:
                    return self.position[1] + y
        raise Exception("No y max found", None)

    def y_min(self):
        for y in range(len(self.fill)):
            for x in range(len(self.fill[y])):
                if self.fill[y][x] == 1:
                    return self.position[1] + y
        raise Exception("No y min found", None)

    def x_max(self):
        for x in range(len(self.fill) - 1, -1, -1):
            for y in range(len(self.fill[x])):
                if self.fill[y][x] == 1:
                    return self.position[0] + x
        raise Exception("No x max found", None)
    
    def x_min(self):
        for x in range(len(self.fill)):
            for y in range(len(self.fill[x])):
                if self.fill[y][x] == 1:
                    return self.position[0] + x
        raise Exception("No x min found", None)
    
    def rotate_right(self):
        new_fill = []
        for y in range(len(self.fill)):
            new_fill.append([])
            for x in range(len(self.fill[y])):
                new_fill[y].insert(0, self.fill[x][y])
        self.fill = new_fill

    def rotate_left(self):
        new_fill = []
        for y in range(len(self.fill)):
            new_fill.append([])
            for x in range(len(self.fill[y])):
                new_fill[y].insert(0, self.fill[len(self.fill[y]) - 1 - x][len(self.fill[y]) - 1 - y])
        self.fill = new_fill

    def move(self, direction):
        self.position[0] += direction[0]
        self.position[1] += direction[1]

    def get_blocks(self):
        filled = []
        for y in range(len(self.fill)):
            for x in range(len(self.fill[y])):
                if self.fill[y][x] == 1:
                    filled.append([self.position[0] + x, self.position[1] + y])

        return filled                

class Long_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 100, 150, 255
        self.fill = [[0, 1, 0, 0],\
                     [0, 1, 0, 0],\
                     [0, 1, 0, 0],\
                     [0, 1, 0, 0]]

class T_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 255, 0, 255
        self.fill = [[0, 1, 0, 0],\
                     [0, 1, 1, 0],\
                     [0, 1, 0, 0],\
                     [0, 0, 0, 0]]

class LRight_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 255, 200, 100
        self.fill = [[0, 1, 0, 0],\
                     [0, 1, 0, 0],\
                     [0, 1, 1, 0],\
                     [0, 0, 0, 0]]

class LLeft_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 0, 0, 255
        self.fill = [[0, 0, 1, 0],\
                     [0, 0, 1, 0],\
                     [0, 1, 1, 0],\
                     [0, 0, 0, 0]]

class ZRight_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 150, 255, 150
        self.fill = [[0, 1, 0, 0],\
                     [0, 1, 1, 0],\
                     [0, 0, 1, 0],\
                     [0, 0, 0, 0]]

class ZLeft_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 255, 0, 0
        self.fill = [[0, 0, 1, 0],\
                     [0, 1, 1, 0],\
                     [0, 1, 0, 0],\
                     [0, 0, 0, 0]]

class Square_Piece(Pieces):
    def __init__(self, position):
        self.position = position
        self.color = 255, 255, 0
        self.fill = [[0, 0, 0, 0],\
                     [0, 1, 1, 0],\
                     [0, 1, 1, 0],\
                     [0, 0, 0, 0]]

