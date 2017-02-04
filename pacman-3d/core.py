import pygame
from pygame.locals import *

screen_res = (1200, 800)

pygame.init()
screen = pygame.display.set_mode(screen_res, 0, 32)
clock = pygame.time.Clock()

nav_x, nav_y = (600, 400)

background = pygame.surface.Surface(screen_res).convert()
background.fill((0, 0, 0))

while True:
    key_pressend = pygame.key.get_pressed()

    time_passed = clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    if key_pressend[K_UP]:
        nav_y -= 6
    elif key_pressend[K_DOWN]:
        nav_y += 6
    elif key_pressend[K_LEFT]:
        nav_x -= 6
    elif key_pressend[K_RIGHT]:
        nav_x += 6

    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, (255, 255, 0), [nav_x, nav_y, 16, 16])
    pygame.display.update()
