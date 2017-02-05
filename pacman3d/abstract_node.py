from pacman3d.vectors import Vector2D


class AbstractNode(object):
    def __init__(self, position, width, height):
        self.col, self.row = position
        self.position = Vector2D(self.col*width - 1/2*width, self.row*height - 1/2*height)

    def __str__(self, *args, **kwargs):
        return str(self.row) + ' / ' + str(self.col)

    def get_row_col(self):
        return self.row, self.col
