from pacman3d.vectors import Vector2D
from pygame.locals import *

class FourWayMoving:

    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    STOP = Vector2D()

    def __init__(self, node, entity):
        '''node is the starting node.  All other nodes are connected
        entity is the entity that travels from node to node'''
        self.node = node
        self.target = node
        self.entity = entity
        self.direction = self.STOP
        self.entity.direction = self.STOP
        self.valid_directions = self.node.directions
        if self.entity.direction in self.valid_directions:
            self.set_entity_direction(self.entity.direction)

    def update(self, dt):
        self.move_towards_target(dt)
        if self.overshot_target():
            self.node = self.target

            if self.node.portal:
                self.node = self.node.portal
                self.entity.position = self.node.position
                self.valid_directions = self.node.directions

            self.valid_directions = self.node.directions
            if self.direction in self.valid_directions:
                if self.direction != self.entity.direction:
                    self.entity.position = self.node.position
                    self.set_entity_direction(self.direction)
                else:
                    self.set_target(self.entity.direction)
            else:
                if self.entity.direction in self.valid_directions:
                    self.set_target(self.entity.direction)
                else:
                    self.entity.position = self.node.position
                    self.entity.direction = self.STOP
        else:
            if self.entity.direction == self.STOP:
                if self.direction in self.valid_directions:
                    self.set_entity_direction(self.direction)
            else:
                if self.direction == self.entity.direction * -1:
                    self.reverse_direction()

    def set_entity_direction(self, direction):
        self.entity.direction = direction
        self.set_target(direction)
        self.valid_directions = [direction, direction * -1]

    def reverse_direction(self):
        '''Swap the node and target'''
        temp = self.target
        self.target = self.node
        self.node = temp
        self.entity.direction *= -1

    def key_continuous(self, key):
        if key[K_UP]:
            self.direction = self.UP
        elif key[K_DOWN]:
            self.direction = self.DOWN
        elif key[K_RIGHT]:
            self.direction = self.RIGHT
        elif key[K_LEFT]:
            self.direction = self.LEFT
        else:
            self.direction = self.STOP

    def key_discrete(self, key):
        pass

    def move_towards_target(self, dt):
        ds = self.entity.speed * dt
        self.entity.position += self.entity.direction * ds

    def overshot_target(self):
        node_to_target = self.length_from_node(self.target.position)
        node_to_self = self.length_from_node(self.entity.position)
        return node_to_self > node_to_target
    
    def length_from_node(self, vector):
        vec = vector - self.node.position
        return vec.magnitude_squared()

    def set_target(self, direction):
        index = self.node.directions.index(direction)
        self.target = self.node.neighbors[index]