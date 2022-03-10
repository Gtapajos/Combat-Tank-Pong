import pygame
import game
from config import game_loop, Constants


pygame.init()

# game clock (FPS)
game_clock = pygame.time.Clock()
game = game.Game()

while game_loop:
    game.main()
    game.draw()
    game_clock.tick(Constants.CLOCK_TICK)
    pygame.display.update()