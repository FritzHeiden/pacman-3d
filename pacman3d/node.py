from pacman3d.vectors import Vector2D
from pacman3d.abstract_node import AbstractNode


class Node(AbstractNode):
    def __init__(self, position, width, height):
        super().__init__(position, width, height)
        self.left_neighbor = None
        self.right_neighbor = None
        self.upper_neighbor = None
        self.lower_neighbor = None

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
        neighbor_list = {}
        if self.left_neighbor is not None:
            neighbor_list['LEFT'] = self.left_neighbor
        if self.right_neighbor is not None:
            neighbor_list['RIGHT'] = self.right_neighbor
        if self.upper_neighbor is not None:
            neighbor_list['UP'] = self.upper_neighbor
        if self.lower_neighbor is not None:
            neighbor_list['DOWN'] = self.lower_neighbor

        return neighbor_list

    def set_neighbor(self, neighbor, position):
        if position == 'left':
            self.set_left_neighbor(neighbor, True)
        elif position == 'right':
            self.set_right_neighbor(neighbor, True)
        elif position == 'upper':
            self.set_upper_neighbor(neighbor, True)
        elif position == 'lower':
            self.set_lower_neighbor(neighbor, True)
