import pygame
from pygame.locals import *
from pacman3d.pacman import Pacman
from pacman3d.tile import Tile
from numpy import loadtxt
from pacman3d.node_group import NodeGroup


pygame.init()
width, height = (24, 24)
screen = pygame.display.set_mode((28*width, 36*height), 0, 32)
background = pygame.surface.Surface((10*width,10*height)).convert()
background.fill((0,0,0))
filename = 'pacman3d/maze.txt'
nodes = NodeGroup(width, height)
nodes.createNodeList(filename)
pacman = Pacman((16,16), nodes.nodelist[47])

nodes.nodelist[26].portal = nodes.nodelist[31]
nodes.nodelist[31].portal = nodes.nodelist[26]

clock = pygame.time.Clock()


while True:
    dt = clock.tick(30) / 1000.0
    key_pressed = pygame.key.get_pressed()
    pacman.move.key_continuous(key_pressed)

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            pacman.move.keyDiscrete(event.key)

    screen.blit(background, (0,0))

    for node in nodes.nodelist:
        for nextnode in node.neighbors:
            pygame.draw.line(screen,(255,255,255),node.position.toTuple(), nextnode.position.toTuple(), 2)

    for node in nodes.nodelist:
        pygame.draw.circle(screen,(255,0,0),node.position.toTuple(), 10)

    pacman.update(dt)

    pacman.render(screen)
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
