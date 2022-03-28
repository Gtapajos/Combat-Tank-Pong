import pygame
from pygame.locals import *


# colors class

class Config:
    class Colors:
        BLACK = (0, 0, 0)
        GREEN = (10, 189, 31)
        WHITE = (255, 255, 255)
        BLUE = (0, 110, 230)
        BROWN = (137, 50, 3)
        YELLOW = (255, 195, 0)

    class Constants:
        CLOCK_TICK = 60
        SCREEN_SIZE = (1000, 700)
        COOLDOWN_SHOT = 150

    # Global variables
    game_loop = True
    win_sound = True
    screen = pygame.display.set_mode(Constants.SCREEN_SIZE)

    obs_1 = Rect(0, 70, 15, 630)
    obs_2 = Rect(0, 70, 1000, 15)
    obs_3 = Rect(0, 685, 1000, 15)
    obs_4 = Rect(985, 70, 15, 630)
    obs_5 = Rect(170, 270, 15, 150)
    obs_6 = Rect(151, 255, 34, 15)
    obs_7 = Rect(151, 420, 34, 15)
    obs_8 = Rect(170, 150, 50, 18)
    obs_9 = Rect(170, 540, 50, 18)
    obs_10 = Rect(280, 320, 37, 38)
    obs_11 = Rect(350, 200, 50, 20)
    obs_12 = Rect(350, 200, 18, 34)
    obs_13 = Rect(350, 446, 18, 34)
    obs_14 = Rect(350, 460, 50, 20)
    obs_15 = Rect(500, 80, 45, 40)
    obs_16 = Rect(500, 650, 45, 40)
    obs_17 = Rect(630, 200, 50, 20)
    obs_18 = Rect(665, 200, 18, 34)
    obs_19 = Rect(630, 460, 50, 20)
    obs_20 = Rect(665, 446, 18, 34)
    obs_21 = Rect(710, 320, 37, 38)
    obs_22 = Rect(790, 150, 50, 18)
    obs_23 = Rect(790, 540, 50, 18)
    obs_24 = Rect(830, 255, 34, 15)
    obs_25 = Rect(830, 420, 34, 15)
    obs_26 = Rect(830, 270, 15, 150)

    obs_list = [
        obs_1,
        obs_2,
        obs_3,
        obs_4,
        obs_4,
        obs_5,
        obs_6,
        obs_7,
        obs_8,
        obs_9,
        obs_9,
        obs_10,
        obs_11,
        obs_12,
        obs_13,
        obs_14,
        obs_15,
        obs_16,
        obs_17,
        obs_18,
        obs_19,
        obs_20,
        obs_21,
        obs_22,
        obs_23,
        obs_24,
        obs_25,
        obs_26,
    ]

    degrees_tk1 = 0
    degrees_tk2 = 0
    add_x1 = 0
    add_x2 = 0
    add_y1 = 0
    add_y2 = 0

    factmulti1 = 1
    factmulti2 = 1
