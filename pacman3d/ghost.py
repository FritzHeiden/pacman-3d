from pacman3d.entity import AbstractEntity
from pacman3d.move_strategy import MoveStrategy

class Ghost(AbstractEntity):

    def __init__(self, dim, node):
        super().__init__(dim, node)
        self.COLOR = (255, 0, 255)
        self.move_strategy = MoveStrategy(node, self)

    def update(self):
        self.move_strategy.auto_move()

    def draw(self, screen):
        super().draw(screen)
        self.move_strategy.draw_target_node(screen)

    def kill_pacman(self, position_pacman, score):
        if self.position == position_pacman:
            print('kill')
            score.kill()