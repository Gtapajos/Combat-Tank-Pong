import pygame
import game
import tank
from config import game_loop, Constants


# game clock (FPS)
game_clock = pygame.time.Clock()
game = game.Game()
game.menu()

while game_loop:
    game.main()
    game.draw_obstacles()
    game.draw_tanks()
    game.draw_scores()
    game_clock.tick(Constants.CLOCK_TICK)
    pygame.display.update()