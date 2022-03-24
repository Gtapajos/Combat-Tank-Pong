import pygame
import tank
import math
import numpy
from tank import Tank
from config import Colors

angle_1 = 1
angle_2 = 1

class Shot_angle:
    def shot_angle_1(self):
        global angle_1
        angle_1 = Tank.movement_tk1(Tank)[0]
        return Tank.movement_tk1(Tank)[1]


    def shot_angle_2(self):
        global angle_2
        angle_2 = Tank.movement_tk2(Tank)[0]
        return Tank.movement_tk2(Tank)[1]

class Bullet_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 3
        self.speed_y = 3

    def update(self, factmulti):
        self.rect.x -= (
            self.speed_x * math.cos(numpy.radians(angle_2)) * factmulti
        )
        self.rect.y -= (
            self.speed_y * (-math.sin(numpy.radians(angle_2))) * factmulti
        )


class Bullet_2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 3
        self.speed_y = 3

    def update(self, factmulti):
        self.rect.x += (
                self.speed_x * math.cos(numpy.radians(angle_1)) * factmulti
        )
        self.rect.y += (
                self.speed_y * (-math.sin(numpy.radians(angle_1))) * factmulti
        )