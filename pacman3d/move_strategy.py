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
        '''node is the starting node.  All other nodes are connected
        entity is the entity that travels from node to node'''
        self.node = node
        self.target = node.upper_neighbor
        self.moving_object = moving_object
        self.direction = self.UP
        # self.valid_directions = self.node.directions
        # if self.moving_object.direction in self.valid_directions:
        #     self.set_entity_direction(self.moving_object.direction)

    def move(self):
        self.key_continuous(pygame.key.get_pressed())
        if self.moving_object.position == self.target.position:
            self.node = self.target
            self.direction = self.STOP
        self.moving_object.position = self.moving_object.position + self.direction

    def draw_target_node(self, screen):
        pygame.draw.circle(screen, (0, 200, 0), self.target.position.to_tuple(), 8)
        pygame.draw.circle(screen, (0, 0, 200), self.node.position.to_tuple(), 8)





    # def update(self, dt):
    #     self.move_towards_target(dt)
    #     if self.overshot_target():
    #         self.node = self.target
    #
    #         if self.node.portal:
    #             self.node = self.node.portal
    #             self.moving_object.position = self.node.position
    #             self.valid_directions = self.node.directions
    #
    #         self.valid_directions = self.node.directions
    #         if self.direction in self.valid_directions:
    #             if self.direction != self.moving_object.direction:
    #                 self.moving_object.position = self.node.position
    #                 self.set_entity_direction(self.direction)
    #             else:
    #                 self.set_target(self.moving_object.direction)
    #         else:
    #             if self.moving_object.direction in self.valid_directions:
    #                 self.set_target(self.moving_object.direction)
    #             else:
    #                 self.moving_object.position = self.node.position
    #                 self.moving_object.direction = self.STOP
    #     else:
    #         if self.moving_object.direction == self.STOP:
    #             if self.direction in self.valid_directions:
    #                 self.set_entity_direction(self.direction)
    #         else:
    #             if self.direction == self.moving_object.direction * -1:
    #                 self.reverse_direction()

    def set_entity_direction(self, direction):
        self.moving_object.direction = direction
        self.set_target(direction)
        self.valid_directions = [direction, direction * -1]

    def reverse_direction(self):
        '''Swap the node and target'''
        temp = self.target
        self.target = self.node
        self.node = temp
        self.moving_object.direction *= -1

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
        return self.direction is self.UP or self.direction is self.DOWN \
               or self.moving_object.position == self.node.position

    def direction_left_right(self):
        return self.direction is self.LEFT or self.direction is self.RIGHT \
               or self.moving_object.position == self.node.position

    def move_towards_target(self, dt):
        # ds = self.entity.speed * dt
        self.moving_object.position += self.direction

    def overshot_target(self):
        node_to_target = self.length_from_node(self.target.position)
        node_to_self = self.length_from_node(self.moving_object.position)
        return node_to_self > node_to_target
    
    def length_from_node(self, vector):
        vec = vector - self.node.position
        return vec.magnitude_squared()

    def set_target(self, direction):
        index = self.node.directions.index(direction)
        self.target = self.node.neighbors[index]