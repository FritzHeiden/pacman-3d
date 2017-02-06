import pygame
from pacman3d.game_board import GameBoard
from pacman3d.pacman import Pacman
from pacman3d.ghost import Ghost
import os

class GameScene:
    screen = None
    font = None
    tile_width = None
    tile_height = None
    game_board = None
    row = None
    cols = None
    background = None

    def __init__(self):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        def resource_path(relative_path):
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        pygame.init()
        self.tile_width, self.tile_height = (20, 20)
        self.game_board = GameBoard(self.tile_width, self.tile_height)
        self.game_board.read_in_game_board(resource_path('data/maze.txt'))

        self.rows, self.cols = self.game_board.get_size()

        self.screen = pygame.display.set_mode((self.cols*self.tile_width, self.rows*self.tile_height), 0, 32)
        self.background = pygame.surface.Surface((self.cols*self.tile_width, self.rows*self.tile_height)).convert()
        self.background.fill((0,0,0))
        self.font = pygame.font.SysFont("monospace", 35)

        self.score = None
        self.pacman = Pacman((16,16), self.game_board.nodelist[4])
        self.ghost_list = list()
        self.ghost_list.append(Ghost((12, 12), self.game_board.nodelist[10]))
        self.ghost_list.append(Ghost((12, 12), self.game_board.nodelist[20]))
        self.ghost_list.append(Ghost((12, 12), self.game_board.nodelist[30]))
        self.ghost_list.append(Ghost((12, 12), self.game_board.nodelist[40]))

    def handle_input(self):
        test = None

    def update(self, time_elapsed):
        self.pacman.update()
        self.pacman.eat_breadcrump(self.game_board.breadcrumb_list, self.game_board.score)

        if self.game_board.score.lives == 0:
            exit()

    def draw(self):
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.font.render(str(self.game_board.score), 10, (255, 0, 0)), (0,0)),

        self.game_board.draw(self.screen)
        self.pacman.draw(self.screen)

        for ghost in self.ghost_list:
            ghost.draw(self.screen)
            ghost.update()
            ghost.kill_pacman(self.pacman.position, self.game_board.score)
