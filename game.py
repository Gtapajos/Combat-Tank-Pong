import pygame
from pygame.locals import *
from config import Constants, Colors, screen, obs_1, obs_2, obs_3, obs_4, obs_5, obs_6, obs_7, obs_8, obs_9, obs_10, \
    obs_11, obs_12, obs_13, obs_14, obs_15, obs_16, obs_17, obs_18, obs_19, obs_20, obs_21, obs_22, obs_23, obs_24, \
    obs_25, obs_26
from tank import Bullet_1, Bullet_2, Tank1, Tank2, rect_tk1, rect_tk2, shot_angle_1, shot_angle_2

pygame.init()
# Screen

pygame.display.set_caption("TANK COMBAT")

# pygame.mixer.music.load("sounds/mainscreen_theme.mp3")
#pygame.mixer.music.play(-1)



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
        self.rect_tk1 = shot_angle_1()
        self.rect_tk2 = shot_angle_2()

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
            paused_txt = self.font.render("Press P to Unpaused", True, Colors.GREEN)
            quit_txt = self.font.render("Press ESC to Quit", True, Colors.GREEN)
            screen.blit(paused_txt, ((Constants.SCREEN_SIZE[1] / 2) - 30, 300))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2) - 30, 400))

            pygame.time.Clock().tick(Constants.CLOCK_TICK)
            pygame.display.update()


    def main(self):          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_p:
                    self.paused = True
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_e and self.cool_down_counter_1 == 0:
                    self.rect_tk1 = shot_angle_1()
                    self.bullets_2.add(Bullet_2(self.rect_tk1.center))
                    self.cool_down_counter_1 += 1
                elif event.key == pygame.K_KP0 and self.cool_down_counter_2 == 0:
                    self.rect_tk2 = shot_angle_2()
                    self.bullets_1.add(Bullet_1(self.rect_tk2.center))
                    self.cool_down_counter_2 += 1


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
        Tank1(3)
        Tank1.movement(Tank1)
        Tank1.tank_1_limit(Tank1)
        Tank2(3)
        Tank2.movement(Tank2)
        Tank2.tank_2_limit(Tank2)

    def draw_scores(self):
        font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_txt = font.render(str(self.score_p1), True, Colors.GREEN)
        screen.blit(score_txt, (250, 10))
        font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_txt = font.render(str(self.score_p2), True, Colors.BLUE)
        screen.blit(score_txt, (750, 10))

    # Draw e moviment the bullets
    def draw_bullets(self):
        self.bullets_1.draw(screen)
        self.bullets_2.draw(screen)
        self.bullets_1.update()
        self.bullets_2.update()


    def collision_bullet_tank_2(self):
        for bullets in self.bullets_2:
            if self.rect_tk2.x - 35 < bullets.rect.x < self.rect_tk2.x + 35 and self.rect_tk2.y < bullets.rect.y + 35 < self.rect_tk2.y + 35:
                bullets.kill()
                self.score_p1 += 1

    def collision_bullet_tank_1(self):
        for bullets in self.bullets_1:
            if self.rect_tk1.x - 35 < bullets.rect.x < self.rect_tk1.x + 35 and self.rect_tk1.y < bullets.rect.y + 35 < self.rect_tk1.y + 35:
                bullets.kill()
                self.score_p2 += 1


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


