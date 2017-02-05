from pacman3d.abstract_movement import AbstractMoveStrategy
import random

class AutoMoveStrategy(AbstractMoveStrategy):
    def __init__(self, node, moving_object):
        super().__init__(node, moving_object)

    def move(self):
        if self.moving_object.position == self.target.position:

            next_targets = self.target.get_neighbor_list()
            next_targets.pop(self.get_direction_str(next_targets), None)
            self.node = self.target
            next_target = random.choice(list(next_targets.keys()))

            if next_target == 'LEFT':
                self.target = next_targets['LEFT']
                self.direction = self.LEFT
            if next_target == 'RIGHT':
                self.target = next_targets['RIGHT']
                self.direction = self.RIGHT
            if next_target == 'UP':
                self.target = next_targets['UP']
                self.direction = self.UP
            if next_target == 'DOWN':
                self.target = next_targets['DOWN']
                self.direction = self.DOWN
        super().move()
