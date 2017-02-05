from pacman3d.vectors import Vector2D
from pygame.locals import *
import pygame
import random


class AbstractMoveStrategy:

    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    STOP = Vector2D(0, 0)

    def __init__(self, node, moving_object):
        self.node = node
        self.target = self.node
        self.moving_object = moving_object
        self.direction = self.UP
        self.dict_directions = {'UP': self.UP, 'DOWN': self.DOWN, 'LEFT': self.LEFT, 'RIGHT': self.RIGHT}

    def move(self):
        self.moving_object.position = self.moving_object.position + self.direction * self.moving_object.speed

    def get_direction_str(self, dict):
        for i, value in dict.items():
            if value == self.node:
                return i

    def draw_target_node(self, screen):
        pygame.draw.circle(screen, (0, 200, 0), self.target.position.to_tuple(), 8)
        pygame.draw.circle(screen, (0, 0, 200), self.node.position.to_tuple(), 8)


