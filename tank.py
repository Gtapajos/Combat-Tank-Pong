import pygame
from config import Colors, Constants, screen
import math
import numpy

degrees_tk1 = 0
degrees_tk2 = 0
add_x1 = 0
add_x2 = 0
add_y1 = 0
add_y2 = 0

class Tank1:

    def __init__(self, velocity):
        self.velocity = velocity
        self.image = pygame.image.load("img/tank_p1.png")
        self.image = pygame.transform.rotate(pygame.image.load("img/tank_p1.png"), degrees_tk1)
        screen.blit(self.image, (90 + add_x1, 324 + add_y1))

    def movement(self):
        global degrees_tk1, add_x1, add_y1
        if pygame.key.get_pressed()[pygame.K_d]:
            degrees_tk1 -= 3
        if pygame.key.get_pressed()[pygame.K_a]:
            degrees_tk1 += 3
        if pygame.key.get_pressed()[pygame.K_w]:
            add_x1 += 3 * math.cos(numpy.radians(degrees_tk1))
            add_y1 += 3 * (-math.sin(numpy.radians(degrees_tk1)))
            print(f"cosseno: {math.cos(numpy.radians(degrees_tk1))}")
            print(f"seno: {math.sin(numpy.radians(degrees_tk1))}")
            print(f"degrees: {degrees_tk1}")


class Tank2:

    def __init__(self, velocity):
        self.velocity = velocity
        self.image = pygame.image.load("img/tank_p2.png")
        self.image = pygame.transform.rotate(pygame.image.load("img/tank_p2.png"), degrees_tk2)
        screen.blit(self.image, (900 - add_x2, 324 - add_y2))
        self.rect = self.image.get_rect(center = (900 - add_x2, 324 - add_y2))
        self.rect.topleft = [self.rect.x, self.rect.y]

    def movement(self):
        global degrees_tk2, add_x2, add_y2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            degrees_tk2 -= 3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            degrees_tk2 += 3
        if pygame.key.get_pressed()[pygame.K_UP]:
            add_x2 += 3 * math.cos(numpy.radians(degrees_tk2))
            add_y2 += 3 * (-math.sin(numpy.radians(degrees_tk2)))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center = pos)
        self.speed_x = 3
        self.speed_y = 3

        
    def update(self):
        self.rect.x -= self.speed_x
        self.rect.y -= self.speed_y


