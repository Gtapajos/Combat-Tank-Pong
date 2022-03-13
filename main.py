import pygame
import game
from config import game_loop, Constants


# game clock (FPS)
game_clock = pygame.time.Clock()
game = game.Game()
game.menu()

while game_loop:
    game.main()
    game.pause()
    game.draw_obstacles()
    game.tanks_draw_move()
    game.draw_scores()
    game.draw_bullets() 
    game_clock.tick(Constants.CLOCK_TICK)
    pygame.display.update()