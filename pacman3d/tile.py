from pacman3d.entity import AbstractEntity

class Tile(AbstractEntity):
    def __init__(self, dim, pos=[0, 0]):
        super().__init__(dim, pos)
        self.COLOR = (255, 0, 0)

