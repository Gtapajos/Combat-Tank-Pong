import pygame
from config import Constants

# Screen
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("TANK COMBAT")


class Game:

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()