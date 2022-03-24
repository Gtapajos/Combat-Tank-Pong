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
ismoving = False

image_tk1 = pygame.image.load("img/tank_p1.png")
rect_tk1 = image_tk1.get_rect(center=(50 + add_x1, 300 + add_y1))
image_tk2 = pygame.image.load("img/tank_p2.png")
rect_tk2 = image_tk2.get_rect(center=(700 - add_x2, 300 - add_y2))
colide1 = False
colide2 = False
arrow_spin = 0


class Tank:
    def __init__(self):
        global rect_tk1, rect_tk2
        image_tk1 = pygame.transform.rotate(
            pygame.image.load("img/tank_p1.png"), degrees_tk1
        )
        rect_tk1 = image_tk1.get_rect(center=(90 + add_x1, 324 + add_y1))
        screen.blit(image_tk1, rect_tk1)
        rect_tk1.topleft = [rect_tk1.x + 18, rect_tk1.y + 18]
        image_tk2 = pygame.transform.rotate(
            pygame.image.load("img/tank_p2.png"), degrees_tk2
        )
        rect_tk2 = image_tk2.get_rect(center=(900 - add_x2, 324 - add_y2))
        screen.blit(image_tk2, rect_tk2)
        rect_tk2.topleft = [rect_tk2.x + 9, rect_tk2.y + 18]

    def movement_tk1(self):

        global degrees_tk1, add_x1, add_y1, colide1, ismoving
        if pygame.key.get_pressed()[pygame.K_d]:
            degrees_tk1 -= 3
        if pygame.key.get_pressed()[pygame.K_a]:
            degrees_tk1 += 3
        if pygame.key.get_pressed()[pygame.K_w] and colide1 is False:
            ismoving = False
            add_x1 += 3 * math.cos(numpy.radians(degrees_tk1))
            add_y1 += 3 * (-math.sin(numpy.radians(degrees_tk1)))

        rect_tk1 = image_tk1.get_rect(center=(90 + add_x1, 324 + add_y1))

        return (degrees_tk1, rect_tk1)

    def movement_tk2(self):
        global degrees_tk2, add_x2, add_y2, ismoving
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            degrees_tk2 -= 3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            degrees_tk2 += 3
        if pygame.key.get_pressed()[pygame.K_UP] and colide2 is False:
            ismoving = True
            add_x2 += 3 * math.cos(numpy.radians(degrees_tk2))
            add_y2 += 3 * (-math.sin(numpy.radians(degrees_tk2)))

        rect_tk2 = image_tk2.get_rect(center=(900 - add_x2, 324 - add_y2))

        return (degrees_tk2, rect_tk2)

    def tank_1_limit(self):
        global add_y1, add_x1, colide1, collide, ismoving

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
                colide1 = True
                add_x1 += -1 * 15 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 20 * (-math.sin(numpy.radians(degrees_tk1)))
                colide1 = False

        if rect_tk1.colliderect(rect_tk2) and ismoving is False:
            if abs(rect_tk1.left - rect_tk2.left) < 10:
                add_x1 += -1 * 12 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk1)))
            if abs(rect_tk1.bottom - rect_tk2.top) < 10:
                add_x1 += -1 * 12 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk1)))
            if abs(rect_tk1.top - rect_tk2.bottom) < 10:
                add_x1 += -1 * 12 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk1)))
            if abs(rect_tk1.right - rect_tk2.left) < 10:
                add_x1 += -1 * 12 * math.cos(numpy.radians(degrees_tk1))
                add_y1 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk1)))

    def tank_2_limit(self):
        global add_y2, add_x2, colide2, collide, ismoving

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
                colide2 = True
                add_x2 += -1 * 15 * math.cos(numpy.radians(degrees_tk2))
                add_y2 += -1 * 20 * (-math.sin(numpy.radians(degrees_tk2)))
                colide2 = False

        if rect_tk2.colliderect(rect_tk1) and ismoving:
            if abs(rect_tk2.left - rect_tk1.left) < 10:
                add_x2 += -1 * 12 * math.cos(numpy.radians(degrees_tk2))
                add_y2 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk2)))

            if abs(rect_tk2.bottom - rect_tk1.top) < 10:
                add_x2 += -1 * 12 * math.cos(numpy.radians(degrees_tk2))
                add_y2 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk2)))
            if abs(rect_tk2.top - rect_tk1.bottom) < 10:
                add_x2 += -1 * 12 * math.cos(numpy.radians(degrees_tk2))
                add_y2 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk2)))
            if abs(rect_tk2.right - rect_tk1.left) < 10:
                add_x2 += -1 * 12 * math.cos(numpy.radians(degrees_tk2))
                add_y2 += -1 * 12 * (-math.sin(numpy.radians(degrees_tk2)))

