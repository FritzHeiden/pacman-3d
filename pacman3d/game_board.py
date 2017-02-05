from numpy import loadtxt
from pacman3d.node import Node
import pygame
from pacman3d.breadcrump import Breadcrump
from pacman3d.score import Score

class GameBoard(object):
    def __init__(self, tile_width, tile_height):
        self.nodelist = []
        self.breadcrumb_list = []
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.score = Score()

    '''Input a list of nodes, and the row and col integers.  Returns
    the Node object located at that grid position.'''
    def get_node(self, row, col):
        for node in self.nodelist:
            if node.row == row and node.col == col:
                return node
        return None

    def create_basic_game_board(self):
        for i in range(1, 4):
            for j in range(1, 4):
                self.nodelist.append(Node((i, j), self.tile_width, self.tile_height))

        node = self.get_node(2, 2)
        node.set_lower_neighbor(self.get_node(3, 2), True)
        node.set_upper_neighbor(self.get_node(1, 2), True)
        node.set_right_neighbor(self.get_node(2, 3), True)
        node.set_left_neighbor(self.get_node(2, 1), True)
        self.get_node(1, 2).set_upper_neighbor(self.get_node(3, 2))

    def draw(self, screen):
        for node in self.nodelist:
            for key, next_node in node.get_neighbor_list().items():
                pygame.draw.line(screen, (255, 0, 0), node.position.to_tuple(), next_node.position.to_tuple(), 20)

        for breadcrump in self.breadcrumb_list:
            breadcrump.draw(screen)

    '''Create the list of nodes from a text file'''
    def read_in_game_board(self, filename):
        layout = loadtxt(filename, dtype=bytes).astype(str)
        self.rows, self.cols = layout.shape
        for row in range(self.rows):
            for col in range(self.cols):
                if layout[row][col] == '+':
                    self.nodelist.append(Node((col,row), self.tile_width, self.tile_height))
                    self.breadcrumb_list.append(Breadcrump((col, row), self.tile_width, self.tile_height))

        symbols = ['-','-','|','|']

        directions = {'left': (-1,0), 'right': (1,0), 'upper': (0,-1), 'lower': (0,1)}
        for node in self.nodelist:
            for key in directions:
                row, col = node.get_row_col()
                x_offset, y_offset = directions[key]
                val_x, val_y = directions[key]
                try:
                    layout[row+y_offset][col+x_offset]
                except IndexError:
                    pass
                else:
                    val = layout[row+y_offset][col+x_offset]
                    if val in symbols:
                        while val == '-' or val == '|':
                            self.breadcrumb_list.append(Breadcrump((col+x_offset, row+y_offset),
                                                        self.tile_width, self.tile_height))
                            x_offset += val_x
                            y_offset += val_y
                            val = layout[row+y_offset][col+x_offset]
                        node.set_neighbor(self.get_node(row+y_offset, col+x_offset), key)

    def get_size(self):
        return self.rows, self.cols

