from pacman3d.vectors import Vector2D
from pygame.locals import *
import pygame

class MoveStrategy:

    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    STOP = Vector2D(0, 0)

    def __init__(self, node, moving_object):
        self.node = node
        self.target = node.upper_neighbor
        self.moving_object = moving_object
        self.direction = self.UP

    def move(self):
        self.key_continuous(pygame.key.get_pressed())
        if self.moving_object.position == self.target.position:
            self.node = self.target

            if self.direction == self.UP and self.node.upper_neighbor is not None:
                self.target = self.node.upper_neighbor
                print(self.node.upper_neighbor)
            elif self.direction == self.DOWN and self.node.lower_neighbor is not None:
                self.target = self.node.lower_neighbor
            elif self.direction == self.LEFT and self.node.left_neighbor is not None:
                self.target = self.node.left_neighbor
            elif self.direction == self.RIGHT and self.node.right_neighbor is not None:
                self.target = self.node.right_neighbor
            else:
                self.direction = self.STOP
        self.moving_object.position = self.moving_object.position + self.direction

    def draw_target_node(self, screen):
        pygame.draw.circle(screen, (0, 200, 0), self.target.position.to_tuple(), 8)
        pygame.draw.circle(screen, (0, 0, 200), self.node.position.to_tuple(), 8)

    def key_continuous(self, key):
        if key[K_UP]:
            if self.node.upper_neighbor is not None and self.direction_up_down():
                self.target = self.node.upper_neighbor
                self.direction = self.UP
        elif key[K_DOWN]:
            if self.node.lower_neighbor is not None and self.direction_up_down() :
                self.target = self.node.lower_neighbor
                self.direction = self.DOWN
        elif key[K_RIGHT]:
            if self.node.right_neighbor is not None and self.direction_left_right():
                self.target = self.node.right_neighbor
                self.direction = self.RIGHT
        elif key[K_LEFT]:
            if self.node.left_neighbor is not None and self.direction_left_right():
                self.target = self.node.left_neighbor
                self.direction = self.LEFT
        else:
            self.direction = self.direction

    def direction_up_down(self):
        return self.direction == self.UP or self.direction == self.DOWN \
               or self.moving_object.position == self.node.position

    def direction_left_right(self):
        return self.direction == self.LEFT or self.direction == self.RIGHT \
               or self.moving_object.position == self.node.position
