import pygame
from pygame.locals import *

import tank
from config import (
    Constants,
    Colors,
    screen,
    obs_1,
    obs_2,
    obs_3,
    obs_4,
    obs_5,
    obs_6,
    obs_7,
    obs_8,
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
    obs_list,
    factmulti1,
    factmulti2,
)
from tank import (
    Tank
)
from shot_angle import Shot_angle, Bullet_1, Bullet_2
import math
import numpy

pygame.init()
# Screen

pygame.display.set_caption("TANK COMBAT")

pygame.mixer.music.load("sounds/mainscreen_theme.mp3")
pygame.mixer.music.play(-1)


class Game:
    def menu(self):
        self.font = pygame.font.Font("img/upheavtt.ttf", 50)
        play_txt = self.font.render("Press Enter to Play", True, Colors.WHITE)
        quit_txt = self.font.render("Press ESC to Quit", True, Colors.WHITE)
        self.menu_stats = True
        self.paused = False
        self.bullets_1 = pygame.sprite.Group()
        self.bullets_2 = pygame.sprite.Group()
        self.cool_down_counter_1 = 0
        self.cool_down_counter_2 = 0
        self.score_p1 = 0
        self.score_p2 = 0
        self.rect_tk1 = Shot_angle.shot_angle_1(Shot_angle)
        self.rect_tk2 = Shot_angle.shot_angle_2(Shot_angle)

        while self.menu_stats:
            screen.fill(Colors.WHITE)
            menu_img = pygame.image.load("img/menu_bg.jpg")
            screen.blit(menu_img, (0, 0))
            screen.blit(play_txt, ((Constants.SCREEN_SIZE[1] / 2) - 100, 300))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2) - 100, 400))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_RETURN:
                        self.menu_stats = False
            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()

    def pause(self):
        while self.paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_p:
                        self.paused = False
                        pygame.mixer.music.unpause()

            screen.fill(Colors.BLACK)
            paused_txt = self.font.render(
                "Press P to Unpaused", True, Colors.GREEN
            )
            quit_txt = self.font.render(
                "Press ESC to Quit", True, Colors.GREEN
            )
            screen.blit(paused_txt, ((Constants.SCREEN_SIZE[1] / 2) - 30, 300))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2) - 30, 400))

            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()

    def main(self):
        global factmulti1, factmulti2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = True
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_e and self.cool_down_counter_1 == 0:
                    sounds = pygame.mixer.Sound("sounds/tankshoot.wav")
                    sounds.play()
                    self.rect_tk1 = Shot_angle.shot_angle_1(Shot_angle)
                    self.bullets_2.add(Bullet_2(self.rect_tk1.center))
                    self.colision_1 = 0
                    self.cool_down_counter_1 += 1
                    factmulti1 = 1
                elif (
                    event.key == pygame.K_KP0 and self.cool_down_counter_2 == 0
                ):
                    sounds = pygame.mixer.Sound("sounds/tankshoot.wav")
                    sounds.play()
                    self.rect_tk2 = Shot_angle.shot_angle_2(Shot_angle)
                    self.bullets_1.add(Bullet_1(self.rect_tk2.center))
                    self.colision_2 = 0
                    self.cool_down_counter_2 += 1
                    factmulti2 = 1
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    def draw_obstacles(self):
        screen.fill(Colors.BROWN)

        pygame.draw.rect(screen, Colors.YELLOW, obs_1)
        pygame.draw.rect(screen, Colors.YELLOW, obs_2)
        pygame.draw.rect(screen, Colors.YELLOW, obs_3)
        pygame.draw.rect(screen, Colors.YELLOW, obs_4)
        pygame.draw.rect(screen, Colors.YELLOW, obs_5)
        pygame.draw.rect(screen, Colors.YELLOW, obs_6)
        pygame.draw.rect(screen, Colors.YELLOW, obs_7)
        pygame.draw.rect(screen, Colors.YELLOW, obs_8)
        pygame.draw.rect(screen, Colors.YELLOW, obs_9)
        pygame.draw.rect(screen, Colors.YELLOW, obs_10)
        pygame.draw.rect(screen, Colors.YELLOW, obs_11)
        pygame.draw.rect(screen, Colors.YELLOW, obs_12)
        pygame.draw.rect(screen, Colors.YELLOW, obs_13)
        pygame.draw.rect(screen, Colors.YELLOW, obs_14)
        pygame.draw.rect(screen, Colors.YELLOW, obs_15)
        pygame.draw.rect(screen, Colors.YELLOW, obs_16)
        pygame.draw.rect(screen, Colors.YELLOW, obs_17)
        pygame.draw.rect(screen, Colors.YELLOW, obs_18)
        pygame.draw.rect(screen, Colors.YELLOW, obs_19)
        pygame.draw.rect(screen, Colors.YELLOW, obs_20)
        pygame.draw.rect(screen, Colors.YELLOW, obs_21)
        pygame.draw.rect(screen, Colors.YELLOW, obs_22)
        pygame.draw.rect(screen, Colors.YELLOW, obs_23)
        pygame.draw.rect(screen, Colors.YELLOW, obs_24)
        pygame.draw.rect(screen, Colors.YELLOW, obs_25)
        pygame.draw.rect(screen, Colors.YELLOW, obs_26)

    def tanks_draw_move(self):
        Tank()
        Tank.movement_tk1(Tank)
        Tank.tank_1_limit(Tank)
        Tank.movement_tk2(Tank)
        Tank.tank_2_limit(Tank)

    def draw_scores(self):
        font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_txt = font.render(str(self.score_p1), True, Colors.GREEN)
        screen.blit(score_txt, (250, 10))
        font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_txt = font.render(str(self.score_p2), True, Colors.BLUE)
        screen.blit(score_txt, (750, 10))

        quit_txt = self.font.render("Press ESC to Quit", True, Colors.GREEN)

        if self.score_p1 >= 5:
            victory1_img = pygame.image.load("img/p1win.png")
            screen.blit(victory1_img, (375, 225))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2 - 45), 600))

        elif self.score_p2 >= 5:
            victory2_img = pygame.image.load("img/p2win.png")
            screen.blit(victory2_img, (375, 225))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2 - 45), 600))

    # Draw e moviment the bullets
    def draw_bullets(self):
        global factmulti
        self.bullets_1.draw(screen)
        self.bullets_2.draw(screen)
        self.bullets_1.update(factmulti2)
        self.bullets_2.update(factmulti1)

    def collision_bullet_tank_2(self):
        global factmulti1
        for bullets in self.bullets_2:
            if (
                self.rect_tk2.x - 25 < bullets.rect.x < self.rect_tk2.x + 25
                and self.rect_tk2.y
                < bullets.rect.y + 25
                < self.rect_tk2.y + 25
            ):
                bullets.kill()
                self.score_p1 += 1
            elif bullets.rect.y <= 110:
                factmulti1 *= -1
                self.colision_1 += 1
            elif bullets.rect.x <= 40:
                factmulti1 *= -1
                self.colision_1 += 1
            elif bullets.rect.x >= 970:
                factmulti1 *= -1
                self.colision_1 += 1
            elif bullets.rect.y >= 680:
                factmulti1 *= -1
                self.colision_1 += 1
            else:
                for i in obs_list:
                    if (
                        math.sqrt(
                            (i.x + (i.w / 2) - bullets.rect.x) ** 2
                            + (i.y + (i.h / 2) - bullets.rect.y) ** 2
                        )
                        <= 20
                        or math.sqrt(
                            (i.x + (i.w) - bullets.rect.x) ** 2
                            + (i.y + (i.h) - bullets.rect.y) ** 2
                        )
                        <= 20
                        or math.sqrt(
                            (i.x - bullets.rect.x) ** 2
                            + (i.y - bullets.rect.y) ** 2
                        )
                        <= 20
                    ):
                        factmulti1 *= -1
                        self.colision_1 += 1

            if self.colision_1 == 5:
                bullets.kill()

    def collision_bullet_tank_1(self):
        global factmulti2
        for bullets in self.bullets_1:
            if (
                self.rect_tk1.x - 25 < bullets.rect.x < self.rect_tk1.x + 25
                and self.rect_tk1.y
                < bullets.rect.y + 25
                < self.rect_tk1.y + 25
            ):
                bullets.kill()
                self.score_p2 += 1
                # Tank1.rot_1(Tank1)
            elif bullets.rect.y <= 110:
                factmulti2 *= -1
                self.colision_2 += 1
            elif bullets.rect.x <= 40:
                factmulti2 *= -1
                self.colision_2 += 1
            elif bullets.rect.x >= 970:
                factmulti2 *= -1
                self.colision_2 += 1
            elif bullets.rect.y >= 680:
                factmulti2 *= -1
                self.colision_2 += 1
            else:
                for i in obs_list:
                    if (
                        math.sqrt(
                            (i.x + (i.w / 2) - bullets.rect.x) ** 2
                            + (i.y + (i.h / 2) - bullets.rect.y) ** 2
                        )
                        <= 20
                        or math.sqrt(
                            (i.x + (i.w) - bullets.rect.x) ** 2
                            + (i.y + (i.h) - bullets.rect.y) ** 2
                        )
                        <= 20
                        or math.sqrt(
                            (i.x - bullets.rect.x) ** 2
                            + (i.y - bullets.rect.y) ** 2
                        )
                        <= 20
                    ):
                        factmulti2 *= -1
                        self.colision_2 += 1
            if self.colision_2 == 5:
                bullets.kill()

    # Function to destroy bullets that pass the screen
    def destroy_bullets(self):
        for bullets in self.bullets_1:
            if bullets.rect.y > 900 or bullets.rect.y < 50:
                bullets.kill()
        for bullets in self.bullets_2:
            if bullets.rect.y > 900 or bullets.rect.y < 50:
                bullets.kill()

    # Shots cooldown function

    def cooldown_bullet_1(self):
        if self.cool_down_counter_1 >= Constants.COOLDOWN_SHOT:
            self.cool_down_counter_1 = 0
        elif self.cool_down_counter_1 > 0:
            self.cool_down_counter_1 += 1

    def cooldown_bullet_2(self):
        if self.cool_down_counter_2 >= Constants.COOLDOWN_SHOT:
            self.cool_down_counter_2 = 0
        elif self.cool_down_counter_2 > 0:
            self.cool_down_counter_2 += 1
