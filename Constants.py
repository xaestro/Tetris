import pygame
from Pieces import *

SIZE = WIDTH, HEIGHT = 1024, 768
BOARD_LOCATION = BOARD_X, BOARD_Y = 200, 100
BLACK = 0, 0, 0
GREY = 128, 128, 128

GAME_WIDTH = 10
GAME_HEIGHT = 30
TOP_BUFFER = 4

EDGE_LENGTH = 20

PIECES = { 0: Long_Piece, 1: T_Piece, 2: LRight_Piece, 3: LLeft_Piece, 4: ZRight_Piece, 5: ZLeft_Piece, 6: Square_Piece }
