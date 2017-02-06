import pygame
from pacman3d.entity import AbstractEntity
from pacman3d.auto_move_strategy import AutoMoveStrategy

class Ghost(AbstractEntity):

    def __init__(self, dim, node):
        super().__init__(dim, node)
        self.COLOR = (255, 0, 255)
        self.move_strategy = AutoMoveStrategy(node, self)
        # self.speed = 4

    def update(self):
        super().move()

    def draw(self, screen):
        self.move_strategy.draw_target_node(screen)
        x, y = self.position.to_tuple()
        pygame.draw.circle(screen, self.COLOR, (int(x), int(y)), self.dim[0])

    def kill_pacman(self, position_pacman, score):
        if self.position == position_pacman:
            print('kill')
            score.kill()
