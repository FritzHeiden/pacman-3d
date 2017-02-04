import pygame
from pygame.locals import *
from pacman3d.entity import AbstractEntity
from pacman3d.stack import Stack


class Pacman(AbstractEntity):
    def __init__(self, dim, pos=[0, 0]):
        pos = [dim[0]*13+dim[0]/2, dim[1]*26]
        super().__init__(dim, pos)
        self.COLOR = (255, 255, 0)
        self.direction = 'LEFT'
        self.direction_stack = Stack()

    def changeDirection(self, tilelist):
        self.direction_stack.push(self.direction)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP]:
            self.direction = 'UP'
        elif key_pressed[K_DOWN]:
            self.direction = 'DOWN'
        elif key_pressed[K_LEFT]:
            self.direction = 'LEFT'
        elif key_pressed[K_RIGHT]:
            self.direction = 'RIGHT'
        if self.direction_stack.peek() is not self.direction:
            self.direction_stack.push(self.direction)

        while len(self.direction_stack.items) > 0:
            self.direction = self.direction_stack.pop()
            self.move()
            for tile in tilelist:
                collided = self.collide(tile)
                if collided:
                    break
            if not collided:
                self.direction_stack.clear()

    def move(self):
        if self.direction is 'UP':
            self.pos.y -= 2
        elif self.direction is 'DOWN':
            self.pos.y += 2
        elif self.direction is 'LEFT':
            self.pos.x -= 2
        elif self.direction is 'RIGHT':
            self.pos.x += 2

        if self.pos.x+self.dim[0] <= 0:
            self.pos.x = self.dim[0]*28
        elif self.pos.x >= self.dim[0]*28:
            self.pos.x = self.dim[0]

    def collide(self, other):
        xcollide = self.axis_overlap(self.pos.x, self.dim[0],
                                     other.pos.x, other.dim[1])
        ycollide = self.axis_overlap(self.pos.y, self.dim[1],
                                     other.pos.y, other.dim[1])
        if xcollide & ycollide:
            if self.direction is 'UP':
                self.pos.y = other.pos.y + other.dim[1]
            elif self.direction is 'DOWN':
                self.pos.y = other.pos.y - self.dim[1]
            elif self.direction is 'LEFT':
                self.pos.x = other.pos.x + other.dim[0]
            elif self.direction is 'RIGHT':
                self.pos.x = other.pos.x - self.dim[0]

        return xcollide & ycollide

    def axis_overlap(self, p1, length1, p2, length2):
        collided = False
        if p1 < p2:
            if p2 + length2 - p1 < length1 + length2:
                collided = True
        elif p1 > p2:
            if p1 + length1 - p2 < length1 + length2:
                collided = True
        elif p1 == p2:
            collided = True
        return collided