import pygame
from sys import exit

paddle1_moveup = False

class Paddle1:
    def __init__(self):
        self.paddle = pygame.image.load("img/paddle.png")
        self.rect = self.paddle.get_rect(center=(10, 430))

    def draw(self, screen):
        screen.blit(self.paddle, self.rect)

    def move(self, event, move1):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move1 = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move1 = False
        return move1
class Paddle2:
    def __init__(self):
        self.paddle = pygame.image.load("img/paddle.png")
        self.rect = self.paddle.get_rect(center=(1270, 430))

    def draw(self, screen):
        screen.blit(self.paddle, self.rect)


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 960))
pygame.display.set_caption('PONG GAME')
run = True
paddle1 = Paddle1()
paddle2 = Paddle2()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        paddle1_moveup = paddle1.move(event, paddle1_moveup)

    if paddle1_moveup:
        if paddle1.rect.top >= 10:
            paddle1.rect.top -= 3
    screen.fill('black')
    paddle1.draw(screen)
    paddle2.draw(screen)
    pygame.display.update()
    clock.tick(75)
