import pygame
import game
from config import Config


# game clock (FPS)
game_clock = pygame.time.Clock()
game = game.Game()
game.menu()

while Config.game_loop:
    game.main()
    game.pause()
    game.draw_obstacles()
    game.draw_bullets()
    game.tanks_draw_move()
    game.draw_scores()
    game.collision_bullet_tank_1()
    game.collision_bullet_tank_2()
    game.destroy_bullets()
    game.cooldown_bullet_1()
    game.cooldown_bullet_2()
    game_clock.tick(Config.Constants.CLOCK_TICK)
    pygame.display.update()
