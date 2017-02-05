import pygame
from pacman3d.vectors import Vector2D

class AbstractEntity(object):
    def __init__(self, dim, pos=[0, 0]):
        self.dim = dim
        self.pos = Vector2D(pos)
        self.COLOR = (0,0,0)

    def draw(self, screen):
        values = list(self.pos.to_tuple()) + list(self.dim)
        pygame.draw.rect(screen, self.COLOR, values)