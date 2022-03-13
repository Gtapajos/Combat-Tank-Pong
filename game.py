import pygame
from pygame.locals import *
from config import Constants, Colors, screen
from tank import Bullet_1, Bullet_2, Tank1, Tank2

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
                elif event.key == pygame.K_e:
                    self.bullets_2.add(Bullet_2(Tank1(3).rect.center))
                elif event.key == pygame.K_KP0:
                    self.bullets_1.add(Bullet_1(Tank2(3).rect.center))


    def draw_obstacles(self):
        screen.fill(Colors.BROWN)

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
        score_p1 = 0
        score_p2 = 0
        font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_txt = font.render(str(score_p1), True, Colors.GREEN)
        screen.blit(score_txt, (250, 10))
        font = pygame.font.Font("img/upheavtt.ttf", 50)
        score_txt = font.render(str(score_p2), True, Colors.BLUE)
        screen.blit(score_txt, (750, 10))

    # Draw e moviment the bullets
    def draw_bullets(self):
        self.bullets_1.draw(screen)
        self.bullets_2.draw(screen)
        self.bullets_1.update()
        self.bullets_2.update()


