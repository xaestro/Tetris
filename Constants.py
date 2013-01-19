import pygame
from Pieces import *

SIZE = WIDTH, HEIGHT = 800, 600

BLACK = 0, 0, 0, 255
GREY = 128, 128, 128, 255
WHITE = 255, 255, 255, 255
GREEN = 100, 255, 100, 255

GAME_WIDTH = 10
GAME_HEIGHT = 30
TOP_BUFFER = 4

EDGE_LENGTH = HEIGHT / (GAME_HEIGHT + 4)
BOARD_LOCATION = BOARD_X, BOARD_Y = WIDTH / 3, EDGE_LENGTH * 2

PIECES = { 0: Long_Piece, 1: T_Piece, 2: LRight_Piece, 3: LLeft_Piece, 4: ZRight_Piece, 5: ZLeft_Piece, 6: Square_Piece }
