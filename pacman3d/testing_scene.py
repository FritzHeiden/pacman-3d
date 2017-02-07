import pygame
from pacman3d.model_loader import ModelLoader

from OpenGL.GL import *
from OpenGL.GLU import *

class TestingScene:
    def __init__(self):
        loader = ModelLoader()
        self.model = loader.load("./data/ghost.obj")



    def handleInput(self, events):
        for event in events:
            print(event)

    def update(self, time_elapsed):
        test = None
        self.model.update()

    def draw(self):
        glPushMatrix()
        glTranslatef(0.0,0.0, -5)
        self.model.draw()
        glPopMatrix()
