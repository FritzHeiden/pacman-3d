from pacman3d.vectors import Vector2D


class Node(object):
    def __init__(self, position, width, height):
        self.col, self.row = position
        self.position = Vector2D(self.col*width - 1/2*width, self.row*height - 1/2*height)
        self.left_neighbor = None
        self.right_neighbor = None
        self.upper_neighbor = None
        self.lower_neighbor = None

    def __str__(self, *args, **kwargs):
        return str(self.row) + ' / ' + str(self.col)

    def set_neighbors(self, left_neighbor, right_neighbor, upper_neighbor, lower_neighbor):
        self.set_left_neighbor(left_neighbor, True)
        self.set_right_neighbor(right_neighbor, True)
        self.set_upper_neighbor(upper_neighbor, True)
        self.set_lower_neighbor(lower_neighbor, True)

    def set_left_neighbor(self, left_neighbor, first_time=False):
        self.left_neighbor = left_neighbor
        if first_time:
            left_neighbor.set_right_neighbor(self)

    def set_right_neighbor(self, right_neighbor, first_time=False):
        self.right_neighbor = right_neighbor
        if first_time:
            right_neighbor.set_left_neighbor(self)

    def set_upper_neighbor(self, upper_neighbor, first_time=False):
        self.upper_neighbor = upper_neighbor
        if first_time:
            upper_neighbor.set_lower_neighbor(self)

    def set_lower_neighbor(self, lower_neighbor, firts_time=False):
        self.lower_neighbor = lower_neighbor
        if firts_time:
            lower_neighbor.set_upper_neighbor(self)

    def get_neighbor_list(self):
        neighbor_list = []
        if self.left_neighbor is not None:
            neighbor_list.append(self.left_neighbor)
        if self.right_neighbor is not None:
            neighbor_list.append(self.right_neighbor)
        if self.upper_neighbor is not None:
            neighbor_list.append(self.upper_neighbor)
        if self.lower_neighbor is not None:
            neighbor_list.append(self.lower_neighbor)

        return neighbor_list
