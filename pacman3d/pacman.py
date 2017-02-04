import pygame
from pygame.locals import *
from pacman3d.entity import AbstractEntity


class Pacman(AbstractEntity):
    def __init__(self, dim, pos=[0, 0]):
        super().__init__(dim, pos)
        self.COLOR = (255, 255, 0)
        self.direction = 'LEFT'

    def move(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_UP]:
            self.pos.y -= 6
            direction = 'UP'
        elif key_pressed[K_DOWN]:
            self.pos.y += 6
            direction = 'DOWN'
        elif key_pressed[K_LEFT]:
            self.pos.x -= 6
            direction = 'LEFT'
        elif key_pressed[K_RIGHT]:
            self.pos.x += 6
            direction = 'RIGHT'

    def collide(self, other):
        xcollide = self.axis_overlap(self.pos.y, self.dim[0], other.pos.y, other.dim[0])
        ycollide = self.axis_overlap(self.pos.x, self.dim[1], other.pos.x, other.dim[1])
        xycollide = xcollide & ycollide

        if xycollide:
            if self.direction == 'UP':
                self.pos.x = other.pos.x + other.dim[1]

            elif self.direction == 'DOWN':
                self.pos.x = other.pos.x - self.dim[1]

            elif self.direction == 'LEFT':
                test = 1
                self.pos.y = other.pos.y + other.dim[0]
            elif self.direction == 'RIGHT':
                test = 1
                self.pos.y = other.pos.y - self.dim[0]

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
