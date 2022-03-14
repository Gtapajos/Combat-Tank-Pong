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
    game.draw_bullets()
    game.tanks_draw_move()
    game.draw_scores()
    game.destroy_bullets()
    game.cooldown_bullet_1()
    game.cooldown_bullet_2()
    game_clock.tick(Constants.CLOCK_TICK)
    pygame.display.update()