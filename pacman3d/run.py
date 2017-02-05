import pygame
from pygame.locals import *
from pacman3d.pacman import Pacman
from numpy import loadtxt
from pacman3d.game_board import GameBoard
from pacman3d.ghost import Ghost


pygame.init()
tile_width, tile_height = (20, 20)
game_board = GameBoard(tile_width, tile_height)
# game_board.read_in_game_board('maze.txt')
game_board.read_in_game_board('pacman3d/maze.txt')

rows, cols = game_board.get_size()

screen = pygame.display.set_mode((cols*tile_width, rows*tile_height), 0, 32)
background = pygame.surface.Surface((cols*tile_width, rows*tile_height)).convert()
background.fill((0,0,0))

pacman = Pacman((16,16), game_board.nodelist[4])
ghost0 = Ghost((12, 12), game_board.nodelist[10])

# clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background, (0,0))

    game_board.draw(screen)
    pacman.draw(screen)
    pacman.update()

    ghost0.draw(screen)
    ghost0.update()

    pygame.display.update()



# pygame.init()

# layout = loadtxt('pacman3d/maze.txt', dtype=bytes).astype(str)
# rows, cols = layout.shape
# width, height = (16, 16)
# SCREEN_SIZE = (width*cols, height*rows)
# screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
# tiles = []
#
# for col in range(cols):
#     for row in range(rows):
#         value = layout[row][col]
#         if value == '0':
#             pos = (col*width, row*height)
#             tiles.append(Tile((width, height), pos))
#
# background = pygame.surface.Surface(SCREEN_SIZE).convert()
# background.fill((0,0,0))
# pacman = Pacman((width,height), [32*2,32*4])
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#     pacman.changeDirection(tiles)
#
#     screen.blit(background, (0,0))
#     for tile in tiles:
#         tile.draw(screen)
#     pacman.draw(screen)
#     pygame.display.update()
