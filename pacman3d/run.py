import pygame
from pygame.locals import *
from pacman3d.pacman import Pacman
from pacman3d.tile import Tile


SCREEN_RES = (1200, 800)
pacman = Pacman((50, 50), [500, 200])
tile = Tile((150, 150), [150, 100])

pygame.init()
screen = pygame.display.set_mode(SCREEN_RES, 0, 32)
background = pygame.surface.Surface(SCREEN_RES).convert()
background.fill((0, 0, 0))

while True:
    key_pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    pacman.move()
    pacman.collide(tile)

    screen.blit(background, (0, 0))
    tile.draw(screen)
    pacman.draw(screen)
    pygame.display.update()
