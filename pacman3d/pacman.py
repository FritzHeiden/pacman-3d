import pygame
from pygame.locals import *
from pacman3d.entity import AbstractEntity
from pacman3d.move_strategy import MoveStrategy


class Pacman(AbstractEntity):
    def __init__(self, dim, node):
        super().__init__(dim, node)
        self.COLOR = (255, 255, 0)
        self.move_strategy = MoveStrategy(node, self)
        # self.speed = self.node.selfgit

    def update(self):
        super().move()

    def draw(self, screen):
        x, y = self.position.to_tuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), self.dim[0])

    def eat_breadcrump(self, breadcrumps, score):
        for breadcrump in breadcrumps:
            if breadcrump.position == self.position:
                breadcrumps.remove(breadcrump)
                score.hit(10)
