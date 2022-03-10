import pygame
from config import Constants, Colors

# Screen
screen = pygame.display.set_mode(Constants.SCREEN_SIZE)
pygame.display.set_caption("TANK COMBAT")


class Game:

    def main(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw(self):
        pygame.draw.rect(screen, Colors.WHITE, [0, 70, 15, 630])
        pygame.draw.rect(screen, Colors.WHITE, [0, 70, 1000, 15])
        pygame.draw.rect(screen, Colors.WHITE, [0, 685, 1000, 15])
        pygame.draw.rect(screen, Colors.WHITE, [985, 70, 15, 630])
        pygame.draw.rect(screen, Colors.WHITE, [170, 270, 15, 150])
        pygame.draw.rect(screen, Colors.WHITE, [151, 255, 34, 15])
        pygame.draw.rect(screen, Colors.WHITE, [151, 420, 34, 15])
        pygame.draw.rect(screen, Colors.WHITE, [170, 150, 50, 18])
        pygame.draw.rect(screen, Colors.WHITE, [170, 540, 50, 18])
        pygame.draw.rect(screen, Colors.WHITE, [280, 320, 37, 38])
        pygame.draw.rect(screen, Colors.WHITE, [350, 200, 50, 20])
        pygame.draw.rect(screen, Colors.WHITE, [350, 200, 18, 34])
        pygame.draw.rect(screen, Colors.WHITE, [350, 440, 18, 34])
        pygame.draw.rect(screen, Colors.WHITE, [350, 460, 50, 20])
        pygame.draw.rect(screen, Colors.WHITE, [500, 80, 45, 40])
        pygame.draw.rect(screen, Colors.WHITE, [500, 650, 45, 40])
        pygame.draw.rect(screen, Colors.WHITE, [630, 200, 50, 20])
        pygame.draw.rect(screen, Colors.WHITE, [665, 200, 18, 34])
        pygame.draw.rect(screen, Colors.WHITE, [630, 460, 50, 20])
        pygame.draw.rect(screen, Colors.WHITE, [670, 446, 18, 34])
        pygame.draw.rect(screen, Colors.WHITE, [710, 320, 37, 38])
        pygame.draw.rect(screen, Colors.WHITE, [790, 150, 50, 18])
        pygame.draw.rect(screen, Colors.WHITE, [790, 540, 50, 18])
        pygame.draw.rect(screen, Colors.WHITE, [830, 255, 34, 15])
        pygame.draw.rect(screen, Colors.WHITE, [830, 420, 34, 15])
        pygame.draw.rect(screen, Colors.WHITE, [830, 270, 15, 150])

