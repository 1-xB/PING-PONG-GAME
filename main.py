import random

import pygame
from sys import exit

paddle1_moveup = False
paddle1_movedown = False
paddle2_moveup = False
paddle2_movedown = False
score1 = 0
score2 = 0

class Paddle1:
    def __init__(self):
        self.paddle = pygame.image.load("img/paddle.png")
        self.rect = self.paddle.get_rect(center=(30, 480))

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
        self.paddle = pygame.image.load("img/paddle.png")
        self.rect = self.paddle.get_rect(center=(1250, 480))

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
    screen.fill('black')
    pygame.draw.line(screen, '#969696', (640, 0), (640, 960), 5)  # (x1, y1) -> (x2, y2), grubość linii
    screen.blit(paddle1.paddle, paddle1.rect)
    screen.blit(paddle2.paddle, paddle2.rect)
    screen.blit(ball.ball, ball.rect)
    pygame.display.update()
class Ball:
    def __init__(self):
        self.ball = pygame.image.load("img/Ball.png")
        self.rect = self.ball.get_rect(center=(640, 480))
        self.speed_x = 7
        self.speed_y = 7

    def draw(self, screen):
        global score1, score2
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.top <= 0 or self.rect.bottom >= 940:
            self.speed_y *= -1
        if self.rect.bottom <= 0:
            self.speed_x *= -1
        if self.rect.colliderect(paddle1):
            self.speed_x *= -1
        if self.rect.colliderect(paddle2):
            self.speed_x *= -1
        if self.rect.x <= 10:
            score1 += 1
            self.rect.y = 480
            self.rect.x = 625
            self.speed_x *= -1
            paddle1.rect.y = 480
            paddle2.rect.y = 480

            update()
            sco1 = font.render(f'{score1}', True, (255, 255, 255))
            sco1rect = sco1.get_rect(center=(600, 480))
            sco2 = font.render(f'{score2}', True, (255, 255, 255))
            sco2_rect = sco2.get_rect(center=(680, 480))
            screen.blit(sco1, sco1rect)
            screen.blit(sco2, sco2_rect)
            pygame.display.update()
            pygame.time.wait(1000)
        if self.rect.x >= 1270:
            score2 += 1
            self.rect.y = 480
            self.rect.x = 625
            paddle1.rect.y = 480
            paddle2.rect.y = 480

            update()
            score_p1 = font.render(f'{score1}', True, (255, 255, 255))
            score_p1_rect = score_p1.get_rect(center=(600, 480))
            score_p2 = font.render(f'{score2}', True, (255, 255, 255))
            score_p2_rect = score_p2.get_rect(center=(680, 480))
            screen.blit(score_p1, score_p1_rect)
            screen.blit(score_p2, score_p2_rect)
            pygame.display.update()

            los = random.randint(0,1)
            if los:
                self.speed_x *= -1
            if not los:
                self.speed_x *= -1
                self.speed_y *= -1

            screen.blit(self.ball, self.rect)

            pygame.time.wait(1000)

        screen.blit(self.ball, self.rect)


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption('PONG GAME')
run = True

font = pygame.font.SysFont('Arial', 50)


paddle1 = Paddle1()
paddle2 = Paddle2()
ball = Ball()



while True:

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
    score_p1 = font.render(f'{score1}', True, (255, 255, 255))
    score_p1_rect = score_p1.get_rect(center=(600, 480))
    score_p2 = font.render(f'{score2}', True, (255, 255, 255))
    score_p2_rect = score_p2.get_rect(center=(680, 480))
    screen.fill('black')
    pygame.draw.line(screen, '#969696', (640, 0), (640, 960), 5)  # (x1, y1) -> (x2, y2), grubość linii
    paddle1.draw(screen)
    paddle2.draw(screen)

    ball.draw(screen)
    screen.blit(score_p1, score_p1_rect)
    screen.blit(score_p2, score_p2_rect)
    pygame.display.update()
    clock.tick(75)
