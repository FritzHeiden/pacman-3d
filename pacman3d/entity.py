import pygame
from pacman3d.vectors import Vector2D
from pacman3d.abstract_movement import AbstractMoveStrategy

class AbstractEntity(object):
    def __init__(self, dim, node):
        self.dim = dim
        self.node = node
        self.position = self.node.position
        self.COLOR = (0,0,0)
        self.move_strategy = AbstractMoveStrategy(None, None)
        self.speed = 2

    def move(self):
        self.move_strategy.move()

    #def draw(self, screen):
#        x, y = self.position.to_tuple()
        #pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), self.dim[0])
