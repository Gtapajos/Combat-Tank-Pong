import pygame
from config import Constants, Colors, screen
from tank import Tank1, Tank2

pygame.init()
# Screen

pygame.display.set_caption("TANK COMBAT")

pygame.mixer.music.load("sounds/mainscreen_theme.mp3")
pygame.mixer.music.play(-1)


class Game:

    def menu(self):
        font = pygame.font.Font("img/DSEG14Classic-Bold.ttf", 24)
        play_txt = font.render("Press Enter to Play", True, Colors.BLUE)
        quit_txt = font.render("Press ESC to Quit", True, Colors.BLUE)
        self.menu_stats = True

        while self.menu_stats:
            screen.fill(Colors.WHITE)
            menu_img = pygame.image.load("img/menu_bg.jpg")
            screen.blit(menu_img, (0, 0))
            screen.blit(play_txt, ((Constants.SCREEN_SIZE[1] / 2) - 30, 300))
            screen.blit(quit_txt, ((Constants.SCREEN_SIZE[1] / 2) - 30, 400))

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


    def main(self):           
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


    def draw_obstacles(self):
        screen.fill(Colors.BROWN)
        pygame.draw.rect(screen, Colors.YELLOW, [0, 70, 15, 630])
        pygame.draw.rect(screen, Colors.YELLOW, [0, 70, 1000, 15])
        pygame.draw.rect(screen, Colors.YELLOW, [0, 685, 1000, 15])
        pygame.draw.rect(screen, Colors.YELLOW, [985, 70, 15, 630])
        pygame.draw.rect(screen, Colors.YELLOW, [170, 270, 15, 150])
        pygame.draw.rect(screen, Colors.YELLOW, [151, 255, 34, 15])
        pygame.draw.rect(screen, Colors.YELLOW, [151, 420, 34, 15])
        pygame.draw.rect(screen, Colors.YELLOW, [170, 150, 50, 18])
        pygame.draw.rect(screen, Colors.YELLOW, [170, 540, 50, 18])
        pygame.draw.rect(screen, Colors.YELLOW, [280, 320, 37, 38])
        pygame.draw.rect(screen, Colors.YELLOW, [350, 200, 50, 20])
        pygame.draw.rect(screen, Colors.YELLOW, [350, 200, 18, 34])
        pygame.draw.rect(screen, Colors.YELLOW, [350, 440, 18, 34])
        pygame.draw.rect(screen, Colors.YELLOW, [350, 460, 50, 20])
        pygame.draw.rect(screen, Colors.YELLOW, [500, 80, 45, 40])
        pygame.draw.rect(screen, Colors.YELLOW, [500, 650, 45, 40])
        pygame.draw.rect(screen, Colors.YELLOW, [630, 200, 50, 20])
        pygame.draw.rect(screen, Colors.YELLOW, [665, 200, 18, 34])
        pygame.draw.rect(screen, Colors.YELLOW, [630, 460, 50, 20])
        pygame.draw.rect(screen, Colors.YELLOW, [670, 446, 18, 34])
        pygame.draw.rect(screen, Colors.YELLOW, [710, 320, 37, 38])
        pygame.draw.rect(screen, Colors.YELLOW, [790, 150, 50, 18])
        pygame.draw.rect(screen, Colors.YELLOW, [790, 540, 50, 18])
        pygame.draw.rect(screen, Colors.YELLOW, [830, 255, 34, 15])
        pygame.draw.rect(screen, Colors.YELLOW, [830, 420, 34, 15])
        pygame.draw.rect(screen, Colors.YELLOW, [830, 270, 15, 150])

    def tanks_draw_move(self):
        Tank1(3)
        Tank1.movement(Tank1)
        Tank2(3)
        Tank2.movement(Tank2)

    def draw_scores(self):
        score_p1 = 0
        score_p2 = 0
        font = pygame.font.Font("img/DSEG14Classic-Bold.ttf", 50)
        score_txt = font.render(str(score_p1), True, Colors.WHITE)
        screen.blit(score_txt, (250, 10))
        font = pygame.font.Font("img/DSEG14Classic-Bold.ttf", 50)
        score_txt = font.render(str(score_p2), True, Colors.WHITE)
        screen.blit(score_txt, (750, 10))


