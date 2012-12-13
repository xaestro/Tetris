import pygame
from Constants import *

class SoundManager:
    def __init__(self):
        self.mixer = pygame.mixer
        self.mixer.init(44100, -16, 2, 4096)

        self.swoosh_sound = self.mixer.Sound("drop.ogg")
