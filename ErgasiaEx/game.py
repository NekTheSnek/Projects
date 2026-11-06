import pygame
import random
import time
import sys
import os

pygame.init()
pygame.mixer.init()
#parathiro
WIDTH, HEIGHT = 800, 625
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Squid with a Twist")
#mousiki
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), "squid.mp3"))
pygame.mixer.music.play()
music= 5  # gian na kolisei sosta me music hehe 
music_pause = 1 
# loipon edo evala to shashoni mou ti gata mou 
cat_img_front = pygame.image.load("cat2.png")
cat_img_front = pygame.transform.scale(cat_img_front, (120, 120))
cat_img_back = pygame.image.load("cat.png")
cat_img_back = pygame.transform.scale(cat_img_back, (120, 120))
# eimai poli xaroumeni gia tous npc mou
alive_img = pygame.image.load("npc.png").convert_alpha()
alive_img = pygame.transform.scale(alive_img, (40, 60))
death_img = pygame.image.load("npcdead.png").convert_alpha()
death_img = pygame.transform.scale(death_img, (40, 60))
clock = pygame.time.Clock()
FPS = 60
# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
# text
font = pygame.font.SysFont("Arial", 24)
button_font = pygame.font.SysFont("Arial", 20)
# new game
def restart_game():
    python = sys.executable
    os.execl(python, python, *sys.argv)
# lipon dimiourgia npc 
class NPC:
    def __init__(self, index):
        self.x = 50
        self.y = 30 + (index % 25) * 22
        self.speed = random.uniform(0.35, 0.55)
        self.alive = True
        self.finished = False
    def move(self):
        if self.alive and not self.finished:
            self.x += self.speed + random.uniform(-0.1, 0.1)
            if self.x >= WIDTH - 130:
                self.finished = True
    def draw(self, surface):
        frame = alive_img if self.alive else death_img
        surface.blit(frame, (int(self.x), int(self.y)))
# score screen
def show_score_screen(survivors, executed, game_over):
    pygame.mixer.music.stop()
    screen.fill(BLACK)
    
    end_msg = "ΤΕΛΟΣ ΠΑΧΝΙΔΙΟΥ" if not game_over else "GAME OVER"
    gameover_text = font.render(end_msg, True, WHITE)
    score1 = font.render(f" Finished: {survivors}", True, GREEN)
    score2 = font.render(f" Terminated: {executed}", True, RED)

    # Κεντράρισμα κειμένων
    gameover_rect = gameover_text.get_rect(center=(WIDTH // 2, 100))
    score1_rect = score1.get_rect(center=(WIDTH // 2, 200))
    score2_rect = score2.get_rect(center=(WIDTH // 2, 250))

    screen.blit(gameover_text, gameover_rect)
    screen.blit(score1, score1_rect)
    screen.blit(score2, score2_rect)

    # Restart button
    button_rect = pygame.Rect(WIDTH // 2 - 80, 400, 160, 40)
    button_color = (50, 150, 255)
    button_text = button_font.render("NEW GAME", True, WHITE)
    button_text_rect = button_text.get_rect(center=button_rect.center)

    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, button_text_rect)

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    restart_game()
        clock.tick(FPS)
#restart button
    button_rect = pygame.Rect(WIDTH // 2 - 80, 400, 160, 40)
    button_color = (50, 150, 255)
    button_text = button_font.render("NEW GAME", True, WHITE)
    screen.blit(gameover_text, (WIDTH // 2 - 150, 100))
    screen.blit(score1, (WIDTH // 2 - 100, 200))
    screen.blit(score2, (WIDTH // 2 - 100, 250))
    pygame.draw.rect(screen, button_color, button_rect)
    screen.blit(button_text, (button_rect.x + 20, button_rect.y + 8))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    restart_game()
        clock.tick(FPS)
#to basiko pexnidi dokimasa na to valo pio pan oalla den epeze i dont know
while True:
    GAME_DURATION = 50
    start_time = time.time()
    green_light = True
    light_start_time = time.time()
    game_over = False
    npcs = [NPC(i) for i in range(50)]
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elapsed = time.time() - start_time
        remaining_time = max(0, int(GAME_DURATION - elapsed))
        if all(not npc.alive or npc.finished for npc in npcs):
            game_over = True
            running = False
            pygame.display.update()
            pygame.time.delay(2000)
        if remaining_time == 0:
            running = False
        if time.time() - light_start_time >= music:
            green_light = False
        if time.time() - light_start_time >= music + music_pause:
            green_light = True
            light_start_time = time.time()
            pygame.mixer.music.play()
        for npc in npcs:
            if green_light:
                npc.move()
            else:
                if not npc.finished and npc.alive and random.random() < 0.005:
                    npc.alive = False
            npc.draw(screen)
        pygame.draw.line(screen, GREEN, (WIDTH - 130, 0), (WIDTH - 130, HEIGHT), 2)
        current_cat_img = cat_img_front if green_light else cat_img_back
        screen.blit(current_cat_img, (WIDTH - 100, HEIGHT // 2 - 60))
        light_text = font.render("GREEN LIGHT" if green_light else "RED LIGHT", True, GREEN if green_light else RED)
        screen.blit(light_text, (WIDTH // 2 - 80, 20))
        time_text = font.render(f"Time Left: {remaining_time}", True, WHITE)
        screen.blit(time_text, (10, 10))
        pygame.display.update()
        clock.tick(FPS)
    survivors = len([npc for npc in npcs if npc.finished])
    executed = len([npc for npc in npcs if not npc.alive and not npc.finished])
    show_score_screen(survivors, executed, game_over)
