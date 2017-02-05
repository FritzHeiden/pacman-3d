from numpy import loadtxt
from pacman3d.node import Node

class NodeGroup(object):
    def __init__(self, width, height):
        self.nodelist = []
        self.width = width
        self.height = height

    def getNode(self, row, col):
        '''Input a list of nodes, and the row and col integers.  Returns
        the Node object located at that grid position.'''
        for node in self.nodelist:
            if node.row == row and node.col == col:
                return node
        return None

    def createNodeList(self, filename):
        '''Create the list of nodes from a text file'''
        layout = loadtxt(filename, dtype=bytes).astype(str)
        rows, cols = layout.shape
        for row in range(rows):
            for col in range(cols):
                if layout[row][col] == '+':
                    self.nodelist.append(Node((col,row), self.width,
                                              self.height))

        symbols = ('-','-','|','|')
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        for node in self.nodelist:
            row, col = (node.row, node.col)
            for i, direction in enumerate(directions):
                xoffset, yoffset = direction
                valx, valy = direction
                try:
                    layout[row+yoffset][col+xoffset]
                except IndexError:
                    pass
                else:
                    if layout[row+yoffset][col+xoffset] == symbols[i]:
                        val = layout[row+yoffset][col+xoffset]
                        while val == '-' or val == '|':
                            xoffset += valx
                            yoffset += valy
                            val = layout[row+yoffset][col+xoffset]
                        thisnode = self.getNode(row+yoffset, col+xoffset)
                        node.neighbors.append(thisnode)

        for node in self.nodelist:
            node.validDirections()