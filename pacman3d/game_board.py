from numpy import loadtxt
from pacman3d.node import Node
import pygame


class GameBoard(object):
    def __init__(self, tile_width, tile_height, rows, cols):
        self.nodelist = []
        self.tile_width = tile_width
        self.tile_height = tile_height

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
            for nextnode in node.get_neighbor_list():
                pygame.draw.line(screen, (255,255,255), node.position.to_tuple(), nextnode.position.to_tuple(), 2)

        for node in self.nodelist:

            pygame.draw.circle(screen, (255,0,0), node.position.to_tuple(), 10)





    # def read_in_game_board(self, filename):
    #     '''Create the list of nodes from a text file'''
    #     layout = loadtxt(filename, dtype=bytes).astype(str)
    #     rows, cols = layout.shape
    #     for row in range(rows):
    #         for col in range(cols):
    #             if layout[row][col] == '+':
    #                 self.nodelist.append(Node((col,row), self.width,
    #                                           self.height))
    #
    #     symbols = ('-','-','|','|')
    #     directions = ((-1,0),(1,0),(0,-1),(0,1))
    #     for node in self.nodelist:
    #         row, col = (node.row, node.col)
    #         for i, direction in enumerate(directions):
    #             xoffset, yoffset = direction
    #             valx, valy = direction
    #             try:
    #                 layout[row+yoffset][col+xoffset]
    #             except IndexError:
    #                 pass
    #             else:
    #                 if layout[row+yoffset][col+xoffset] == symbols[i]:
    #                     val = layout[row+yoffset][col+xoffset]
    #                     while val == '-' or val == '|':
    #                         xoffset += valx
    #                         yoffset += valy
    #                         val = layout[row+yoffset][col+xoffset]
    #                     thisnode = self.getNode(row+yoffset, col+xoffset)
    #                     node.neighbors.append(thisnode)
    #
    #     for node in self.nodelist:
    #         node.validDirections()