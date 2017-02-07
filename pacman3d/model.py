import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Model:
    vertices = None
    normals = None
    faces = None
    angle = 0

    def update(self):
        self.angle+=2

    def draw(self):
        glRotatef(self.angle, 1, 3, 1)
        glBegin(GL_TRIANGLES)

        for face in self.faces:
            for vertex in face:
                glVertex3fv(self.vertices[vertex-1])

        glEnd()
