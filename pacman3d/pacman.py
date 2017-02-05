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

    def draw(self, screen):
        super().draw(screen)
        self.move_strategy.draw_target_node(screen)

    def update(self):
        self.move_strategy.move()

    def eat_breadcrump(self, breadcrumps, score):
        for breadcrump in breadcrumps:
            if breadcrump.position == self.position:
                breadcrumps.remove(breadcrump)
                score.hit(10)
