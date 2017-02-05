import pygame
from pygame.locals import *
from pacman3d.pacman import Pacman
from numpy import loadtxt
from pacman3d.game_board import GameBoard
from pacman3d.ghost import Ghost
import sys
import os

""" Get absolute path to resource, works for dev and for PyInstaller """
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()
tile_width, tile_height = (20, 20)
game_board = GameBoard(tile_width, tile_height)
game_board.read_in_game_board(resource_path('data/maze.txt'))

rows, cols = game_board.get_size()

screen = pygame.display.set_mode((cols*tile_width, rows*tile_height), 0, 32)
background = pygame.surface.Surface((cols*tile_width, rows*tile_height)).convert()
background.fill((0,0,0))
font = pygame.font.SysFont("monospace", 35)

score = None
pacman = Pacman((16,16), game_board.nodelist[4])
ghost_list = list()
ghost_list.append(Ghost((12, 12), game_board.nodelist[10]))
ghost_list.append(Ghost((12, 12), game_board.nodelist[20]))
ghost_list.append(Ghost((12, 12), game_board.nodelist[30]))
ghost_list.append(Ghost((12, 12), game_board.nodelist[40]))

clock = pygame.time.Clock()


while True:
    dt = clock.tick(30) / 1000.0
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))
    screen.blit(font.render(str(game_board.score), 10, (255, 0, 0)), (0,0))

    game_board.draw(screen)
    pacman.draw(screen)
    pacman.update()
    pacman.eat_breadcrump(game_board.breadcrumb_list, game_board.score)

    for ghost in ghost_list:
        ghost.draw(screen)
        ghost.update()
        ghost.kill_pacman(pacman.position, game_board.score)

    if game_board.score.lives == 0:
        exit()

    pygame.display.update()



