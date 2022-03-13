import pygame
from config import Colors, Constants, screen, obs_list
import math
import numpy

degrees_tk1 = 0
degrees_tk2 = 0
add_x1 = 0
add_x2 = 0
add_y1 = 0
add_y2 = 0

image_tk1 = pygame.image.load("img/tank_p1.png")
rect_tk1 = image_tk1.get_rect(center=(90 + add_x1, 324 + add_y1))
image_tk2 = pygame.image.load("img/tank_p2.png")
rect_tk2 = image_tk2.get_rect(center=(900 - add_x2, 324 - add_y2))

class Tank1:

    def __init__(self, velocity):
        global rect_tk1
        self.velocity = velocity
        image_tk1 = pygame.transform.rotate(pygame.image.load("img/tank_p1.png"), degrees_tk1)
        rect_tk1 = image_tk1.get_rect(center=(90 + add_x1, 324 + add_y1))
        screen.blit(image_tk1, rect_tk1)

    def movement(self):

        global degrees_tk1, add_x1, add_y1
        if pygame.key.get_pressed()[pygame.K_d]:
            degrees_tk1 -= 3
        if pygame.key.get_pressed()[pygame.K_a]:
            degrees_tk1 += 3
        if pygame.key.get_pressed()[pygame.K_w]:
            add_x1 += 3 * math.cos(numpy.radians(degrees_tk1))
            add_y1 += 3 * (-math.sin(numpy.radians(degrees_tk1)))

    def tank_1_limit(self):
        global add_y1, add_x1

        # tank 1 collision with the top
        if add_y1 <= -240:
            add_y1 = -240

        # tank 1 collision with the bottom
        if add_y1 >= 320:
            add_y1 = 320

        # tank 1 collision with the left wall
        if add_x1 <= -80:
            add_x1 = -80

        # tank 1 collision with the right wall
        if add_x1 >= 840:
            add_x1 = 840

        for e in obs_list:
            if rect_tk1.colliderect(e):
                print("Tanque 1 colidiu")

        if rect_tk1.colliderect(rect_tk2):
            print("Tanque 1 colidiu com Tanque 2")

class Tank2:

    def __init__(self, velocity):
        global rect_tk2
        self.velocity = velocity
        image_tk2 = pygame.transform.rotate(pygame.image.load("img/tank_p2.png"), degrees_tk2)
        rect_tk2 = image_tk2.get_rect(center=(900 - add_x2, 324 - add_y2))
        screen.blit(image_tk2, rect_tk2)


    def movement(self):
        global degrees_tk2, add_x2, add_y2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            degrees_tk2 -= 3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            degrees_tk2 += 3
        if pygame.key.get_pressed()[pygame.K_UP]:
            add_x2 += 3 * math.cos(numpy.radians(degrees_tk2))
            add_y2 += 3 * (-math.sin(numpy.radians(degrees_tk2)))


    def tank_2_limit(self):
        global add_y2, add_x2

        # tank 1 collision with the bottom
        if add_y2 <= -315:
            add_y2 = -315

        # tank 1 collision with the top
        if add_y2 >= 250:
            add_y2 = 250

        # tank 1 collision with the right wall
        if add_x2 <= -50:
            add_x2 = -50

        # tank 1 collision with the left wall
        if add_x2 >= 900:
            add_x2 = 900

        for e in obs_list:
            if rect_tk2.colliderect(e):
                print("Tanque 2 colidiu")

        if rect_tk2.colliderect(rect_tk1):
            print("Tanque 2 colidiu com Tanque 1")

class Bullet_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center = pos)
        self.speed_x = 3
        self.speed_y = 3

        
    def update(self):
        self.rect.x -= self.speed_x


    
class Bullet_2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5,5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center = pos)
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x

