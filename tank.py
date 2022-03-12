import pygame
from config import Colors, Constants, screen

degrees_tk1 = 0
degrees_tk2 = 0

class Tank1:

    def __init__(self, velocity):
        self.velocity = velocity
        self.image = pygame.image.load("img/tank_p1.png")
        self.image = pygame.transform.rotate(pygame.image.load("img/tank_p1.png"), degrees_tk1)
        screen.blit(self.image, (90, 324))

    def movement(self):
        global degrees_tk1
        if pygame.key.get_pressed()[pygame.K_d]:
            degrees_tk1 -= 3
        if pygame.key.get_pressed()[pygame.K_a]:
            degrees_tk1 += 3

class Tank2:

    def __init__(self, velocity):
        self.velocity = velocity
        self.image = pygame.image.load("img/tank_p2.png")
        self.image = pygame.transform.rotate(pygame.image.load("img/tank_p2.png"), degrees_tk2)
        screen.blit(self.image, (900, 324))

    def movement(self):
        global degrees_tk2
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            degrees_tk2 -= 3
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            degrees_tk2 += 3


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.bullet = []
        self.bullet.append(pygame.image.load("img/sprite_shoot.png"))
        self.image = self.bullet[0]
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect(center=pos)
        self.speed_x = 3
        self.speed_y = 3

        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
