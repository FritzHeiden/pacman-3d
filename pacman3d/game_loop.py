import pygame
from pacman3d.game_scene import GameScene
from pygame.locals import *

class GameLoop:
    clock = None
    scene = None

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.scene = GameScene()

    def loop(self):
        while True:
            dt = self.clock.tick(30) / 1000.0
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.scene.update(dt)
            self.scene.draw()

            pygame.display.update()
