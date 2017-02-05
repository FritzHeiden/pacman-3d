from pacman3d.node import Node
import pygame

class Breadcrump(Node):
    def __init__(self, position, width, height):
        super().__init__(position, width, height)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 0), self.position.to_tuple(), 4)