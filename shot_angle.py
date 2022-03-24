import pygame
import tank
import math
import numpy
from tank import Tank
from config import Colors

angle_1 = 1
angle_2 = 1

class Shot_angle:
    def shot_angle(self, type_tank):
        if type_tank == 1:
            global angle_1
            angle_1 = Tank.movement_tk1(Tank)[0]
            return Tank.movement_tk1(Tank)[1]
        elif type_tank == 2:
            global angle_2
            angle_2 = Tank.movement_tk2(Tank)[0]
            return Tank.movement_tk2(Tank)[1]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 3
        self.speed_y = 3

    def update(self, factmulti, type_tank):
        if type_tank == 1:
            self.rect.x -= (
                self.speed_x * math.cos(numpy.radians(angle_2)) * factmulti
            )
            self.rect.y -= (
                self.speed_y * (-math.sin(numpy.radians(angle_2))) * factmulti
            )
        elif type_tank == 2:
            self.rect.x += (
                self.speed_x * math.cos(numpy.radians(angle_1)) * factmulti
            )
            self.rect.y += (
                self.speed_y * (-math.sin(numpy.radians(angle_1))) * factmulti
            )
