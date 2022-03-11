import pygame
from config import Colors, Constants, screen

class Tank1:

    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        pygame.draw.rect(screen, Colors.GREEN, [self.x, self.y + self.height/2.5, 52.5, 5])
        pygame.draw.rect(screen, Colors.GREEN, [self.x, self.y, self.width, self.height])

class Tank2:

    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        pygame.draw.rect(screen, Colors.GREEN, [self.x - self.width/2, self.y + self.height / 2.5, 20, 5])
        pygame.draw.rect(screen, Colors.GREEN, [self.x, self.y, self.width, self.height])

