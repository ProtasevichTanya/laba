import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill ((200, 200, 200))

circle(screen, (255, 255, 80), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 2)

circle(screen, (255, 0, 0), (240, 180), 20)
circle(screen, (0, 0, 0), (240, 180), 20, 2)
circle(screen, (0, 0, 0), (240, 180), 10)
circle(screen, (255, 0, 0), (160, 180), 25)
circle(screen, (0, 0, 0), (160, 180), 25, 2)
circle(screen, (0, 0, 0), (160, 180), 10)

polygon(screen, (0, 0, 0), [(200,160), (195,170), (135,140),(140,130)] )
polygon(screen, (0, 0, 0), [(210,160), (215,170), (265,150),(260,140)] )

rect(screen, (0, 0, 0), (150, 250, 100, 15))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
