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
angle_1 = 1
angle_2 = 1

image_tk1 = pygame.image.load("img/tank_p1.png")
rect_tk1 = image_tk1.get_rect(center=(90 + add_x1, 324 + add_y1))
image_tk2 = pygame.image.load("img/tank_p2.png")
rect_tk2 = image_tk2.get_rect(center=(900 - add_x2, 324 - add_y2))
colide1 = False
colide2 = False


class Tank1:

    def __init__(self, velocity):
        global rect_tk1, coords_tk1
        self.velocity = velocity
        image_tk1 = pygame.transform.rotate(pygame.image.load("img/tank_p1.png"), degrees_tk1)
        rect_tk1 = image_tk1.get_rect(center=(90 + add_x1, 324 + add_y1))
        screen.blit(image_tk1, rect_tk1)
        rect_tk1.topleft = [rect_tk1.x + 18, rect_tk1.y + 18]

    def movement(self):

        global degrees_tk1, add_x1, add_y1, colide1
        if pygame.key.get_pressed()[pygame.K_d]:
            degrees_tk1 -= 3
        if pygame.key.get_pressed()[pygame.K_a]:
            degrees_tk1 += 3
        if pygame.key.get_pressed()[pygame.K_w] and colide1 is False:
            add_x1 += 3 * math.cos(numpy.radians(degrees_tk1))
            add_y1 += 3 * (-math.sin(numpy.radians(degrees_tk1)))
        print(degrees_tk1)
        print(math.cos(numpy.radians(degrees_tk1)))

    def tank_1_limit(self):
        global add_y1, add_x1, colide1, collide

        # tank 1 collision with the top
        if add_y1 <= -240:
            add_y1 += 30

        # tank 1 collision with the bottom
        if add_y1 >= 340:
            add_y1 -= 30

        # tank 1 collision with the left wall
        if add_x1 <= -80:
            add_x1 += 50

        # tank 1 collision with the right wall
        if add_x1 >= 880:
            add_x1 -= 50

        for e in obs_list:
            if rect_tk1.colliderect(e):
                print("está colidindo")
                colide1 = True
                add_x1 += -1 * 15 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 20 * (-math.sin(numpy.radians(degrees_tk1)))
                colide1 = False

        if rect_tk1.colliderect(rect_tk2):
            if abs(rect_tk1.left - rect_tk2.left) < 10:
                collide = True
                add_x1 += -1 * 30 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 20 * (-math.sin(numpy.radians(degrees_tk1)))
                collide = False
            if abs(rect_tk1.bottom - rect_tk2.top) < 10:
                collide = True

                collide = False
            if abs(rect_tk1.top - rect_tk2.bottom) < 10:
                collide = True

                collide = False
            if abs(rect_tk1.right - rect_tk2.left) < 10:
                collide = True
                add_x1 += 1 * 30 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += 1 * 20 * (-math.sin(numpy.radians(degrees_tk1)))
                collide = False


class Tank2:

    def __init__(self, velocity):
        global rect_tk2
        self.velocity = velocity
        image_tk2 = pygame.transform.rotate(pygame.image.load("img/tank_p2.png"), degrees_tk2)
        rect_tk2 = image_tk2.get_rect(center=(900 - add_x2, 324 - add_y2))
        screen.blit(image_tk2, rect_tk2)
        rect_tk2.topleft = [rect_tk2.x + 9, rect_tk2.y + 18]

    def movement(self):
        global degrees_tk2, add_x2, add_y2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            degrees_tk2 -= 3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            degrees_tk2 += 3
        if pygame.key.get_pressed()[pygame.K_UP] and colide2 is False:
            add_x2 += 3 * math.cos(numpy.radians(degrees_tk2))
            add_y2 += 3 * (-math.sin(numpy.radians(degrees_tk2)))

    def tank_2_limit(self):
        global add_y2, add_x2, colide2, collide

        # tank 2 collision with the top
        if add_y2 <= -315:
            add_y2 += 30

        # tank 2 collision with the bottom
        if add_y2 >= 250:
            add_y2 -= 30

        # tank 2 collision with the left wall
        if add_x2 <= -50:
            add_x2 += 50

        # tank 2 collision with the right wall
        if add_x2 >= 900:
            add_x2 -= 50

        for e in obs_list:
            if rect_tk2.colliderect(e):
                print("está colidindo")
                colide2 = True
                add_x2 += -1 * 15 * math.cos(numpy.radians(degrees_tk2))
                add_y2 += -1 * 20 * (-math.sin(numpy.radians(degrees_tk2)))
                colide2 = False

        if rect_tk2.colliderect(rect_tk1):
            if abs(rect_tk2.left - rect_tk1.left) < 10:
                collide = True
                add_x2 += -1 * 30 * math.cos(numpy.radians(degrees_tk1))
                add_y2 += -1 * 20 * (-math.sin(numpy.radians(degrees_tk1)))
                collide = False
            if abs(rect_tk2.bottom - rect_tk1.top) < 10:
                collide = True

                collide = False
            if abs(rect_tk2.top - rect_tk1.bottom) < 10:
                collide = True

                collide = False
            if abs(rect_tk2.right - rect_tk1.left) < 10:
                collide = True
                add_x2 += 1 * 30 * math.cos(numpy.radians(degrees_tk1))
                add_y2 += 1 * 20 * (-math.sin(numpy.radians(degrees_tk1)))
                collide = False


class Bullet_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x -= self.speed_x * math.cos(numpy.radians(angle_2))
        self.rect.y -= self.speed_y * (-math.sin(numpy.radians(angle_2)))


class Bullet_2(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(Colors.WHITE)
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 3
        self.speed_y = 3

    def update(self):
        self.rect.x += self.speed_x * math.cos(numpy.radians(angle_1))
        self.rect.y += self.speed_y * (-math.sin(numpy.radians(angle_1)))


def shot_angle_1():
    global angle_1
    angle_1 = degrees_tk1


def shot_angle_2():
    global angle_2
    angle_2 = degrees_tk2