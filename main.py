import random

import pygame
from sys import exit
start_time = 100



paddle1_moveup = False
paddle1_movedown = False
paddle2_moveup = False
paddle2_movedown = False
czas = None
score1 = 0
score2 = 0


class Paddle1:
    def __init__(self):
        self.paddle = pygame.image.load("img/paddle.png").convert_alpha()
        self.rect = self.paddle.get_rect(center=(10, 480))

    def draw(self, screen):
        screen.blit(self.paddle, self.rect)

    def moveup(self, event, paddle1_moveup):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_moveup = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle1_moveup = False
        return paddle1_moveup

    def movedown(self, event, paddle1_movedown):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                paddle1_movedown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                paddle1_movedown = False
        return paddle1_movedown


class Paddle2:
    def __init__(self):
        self.paddle = pygame.image.load("img/paddle.png").convert_alpha()
        self.rect = self.paddle.get_rect(center=(1270, 480))

    def draw(self, screen):
        screen.blit(self.paddle, self.rect)

    def moveup(self, event, paddle2_moveup):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle2_moveup = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                paddle2_moveup = False
        return paddle2_moveup

    def movedown(self, event, paddle2_movedown):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                paddle2_movedown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                paddle2_movedown = False
        return paddle2_movedown


def update():
    global score1, score2, czas
    screen.fill('#2F373F')
    pygame.draw.line(screen, '#969696', (640, 0), (640, 960), 1)  # (x1, y1) -> (x2, y2), grubość linii
    screen.blit(paddle1.paddle, paddle1.rect)
    screen.blit(paddle2.paddle, paddle2.rect)
    screen.blit(ball.ball, ball.rect)
    score_p1 = font.render(f'{score1}', True, (255, 255, 255))
    score_p1_rect = score_p1.get_rect(center=(600, 480))
    score_p2 = font.render(f'{score2}', True, (255, 255, 255))
    score_p2_rect = score_p2.get_rect(center=(680, 480))

    screen.blit(score_p1, score_p1_rect)
    screen.blit(score_p2, score_p2_rect)
    if czas:
        x = 640
        y = 600

        # Renderowanie tekstu z tłem
        text_surface = font2.render(f'{czas}', True, (255, 0, 0))

        # Utworzenie powierzchni tła o odpowiednich wymiarach
        text_rect = text_surface.get_rect(center=(x, y))
        background_surface = pygame.Surface((text_rect.width, text_rect.height))
        background_surface.fill('#2F373F')

        # Narysowanie tekstu na powierzchni tła
        background_surface.blit(text_surface, (0, 0))
        screen.blit(background_surface, (x - text_rect.width / 2, y - text_rect.height / 2))

    pygame.display.update()


class Ball:
    def __init__(self):
        self.ball = pygame.image.load("img/Ball.png").convert_alpha()
        self.rect = self.ball.get_rect(center=(600, 480))
        self.speed_x = 0
        self.speed_y = 0

    def draw(self, screen):
        global score1, score2, start_time, current_time
        current_time = pygame.time.get_ticks()
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= 960 and not self.rect.colliderect(
                paddle1) and not self.rect.colliderect(paddle2):
            self.speed_y *= -1
            pong.play()
        if self.rect.bottom <= 0 and not self.rect.colliderect(paddle1) and not self.rect.colliderect(paddle2):
            self.speed_x *= -1
            pong.play()
        if self.rect.colliderect(paddle1):
            self.speed_x *= -1
            pong.play()
        if self.rect.colliderect(paddle2):
            self.speed_x *= -1
            pong.play()

        if self.rect.x <= 2:
            score.play()
            score2 += 1
            start_time = pygame.time.get_ticks()
            paddle1.rect.y = 410
            paddle2.rect.y = 410
            self.reset()
            update()

        if self.rect.x >= 1250:
            score.play()
            score1 += 1
            paddle1.rect.y = 410
            paddle2.rect.y = 410
            start_time = pygame.time.get_ticks()
            self.reset()
            update()

        screen.blit(self.ball, self.rect)

    def reset(self):
        global start_time,czas

        self.rect.x = 626
        self.rect.y = 470
        self.speed_x = 0
        self.speed_y = 0
        if start_time and 900 <= pygame.time.get_ticks() - start_time <= 1100:
            czas = 3
            update()
        elif 1900 <= pygame.time.get_ticks() - start_time <= 2100:
            czas = 2
            update()
        elif 2800 <= pygame.time.get_ticks() - start_time <= 3000:
            czas = 1
            update()
        elif 3700 <= pygame.time.get_ticks() - start_time <= 4000:
            czas = None
            start_time = 0
            self.speed_y = random.choice([-7, 7])
            self.speed_x = random.choice([-7, 7])



pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("sound/music/music1.mp3")
pygame.mixer.music.load("sound/music/music2.mp3")
pygame.mixer.music.load("sound/music/music3.mp3")
pygame.mixer.music.load("sound/music/music4.mp3")



pong = pygame.mixer.Sound("sound/pong.ogg")
pong.set_volume(0.3)
score = pygame.mixer.Sound("sound/score.ogg")
score.set_volume(0.3)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption('PONG GAME')
run = True

icon = pygame.image.load("favicon.ico")
pygame.display.set_icon(icon)
font = pygame.font.SysFont('font/freesansbold.ttf', 50)
font2 = pygame.font.SysFont('font/freesansbold.ttf', 60)

paddle1 = Paddle1()
paddle2 = Paddle2()
ball = Ball()

while True:
    if not pygame.mixer.music.get_busy():
        numer_piosenki = random.randint(1, 4)
        pygame.mixer.music.load(f"sound/music/music{numer_piosenki}.mp3")
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        paddle1_moveup = paddle1.moveup(event, paddle1_moveup)
        paddle1_movedown = paddle1.movedown(event, paddle1_movedown)
        paddle2_moveup = paddle2.moveup(event, paddle2_moveup)
        paddle2_movedown = paddle2.movedown(event, paddle2_movedown)

    if paddle1_moveup:
        if paddle1.rect.top >= 10:
            paddle1.rect.top -= 6
    if paddle1_movedown:
        if paddle1.rect.top <= 800:
            paddle1.rect.top += 6
    if paddle2_moveup:
        if paddle2.rect.top >= 10:
            paddle2.rect.top -= 6
    if paddle2_movedown:
        if paddle2.rect.top <= 800:
            paddle2.rect.top += 6

    screen.fill('#2F373F')
    pygame.draw.line(screen, '#969696', (640, 0), (640, 960), 5)  # (x1, y1) -> (x2, y2), grubość linii
    paddle1.draw(screen)
    paddle2.draw(screen)
    update()
    if ball.speed_x != 0:
        ball.draw(screen)
    if ball.speed_x == 0:
        ball.reset()

    pygame.display.update()
    clock.tick(75)
