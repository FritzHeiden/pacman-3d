import pygame
from pacman3d.game_scene import GameScene
from pacman3d.testing_scene import TestingScene
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class GameLoop:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.scene = TestingScene()

        self.resolution = (800, 600)
        self.screen = pygame.display.set_mode(self.resolution, DOUBLEBUF|OPENGL)

        gluPerspective(45, (self.resolution[0]/self.resolution[1]), 0.1, 50.0)

    def loop(self):
        while True:
            dt = self.clock.tick(30) / 1000.0
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            self.scene.handleInput(pygame.event.get())
            self.scene.update(dt)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            self.scene.draw()

            pygame.display.flip()
            pygame.time.wait(10)
