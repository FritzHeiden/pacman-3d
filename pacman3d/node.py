from pacman3d.vectors import Vector2D

class Node(object):
    def __init__(self, position, width, height):
        self.col, self.row = position
        self.position = Vector2D(self.col*width, self.row*height)
        self.neighbors = []
        self.target = None
        self.directions = []
        self.portal = None

    def validDirections(self):
        for node in self.neighbors:
            tempvec = node.position - self.position
            self.directions.append(tempvec.normalize())
