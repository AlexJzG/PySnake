import pygame
import numpy as np

from .grid import Grid
from .player import Player
from .fruit import Fruit


class SnakeGame:
    def __init__(self, width=10, height=10, cell_size=50, gui=True):
        if width < 3 or height < 3:
            raise ValueError(
                    "Attributes 'height' and 'width' must be greater than 2.")
        if gui:
            self.screen = pygame.display.set_mode(
                    [width * cell_size,
                     (height + 0.5) * cell_size])
        else:
            self.screen = None
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.font = pygame.freetype.SysFont("Iosevka Nerd Font", cell_size / 2)
        self.grid = Grid(width, height)
        self.player = Player()
        self.fruit = Fruit()
        self.fruit.move(self.grid, self.player.position())

        self.ended = False
        self.won = False

    def move(self, direction=None):
        if direction in ['left', 'right', 'up', 'down']:
            self.player.change_direction(direction)

        if not self.player.move(self.grid):
            self.ended = True
            return

        if self.fruit.position() == self.player.head():
            if not self.fruit.move(self.grid, set(self.player.position())):
                self.ended = True
                self.won = True
                return
            self.player.grow()

    def get_score(self):
        return self.player.size

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.player.draw(self.screen, self.cell_size)
        self.fruit.draw(self.screen, self.cell_size)
        self.grid.draw(self.screen, self.cell_size)
        # Load text
        self.font.render_to(self.screen,
                            (0, self.height * self.cell_size),
                            f"Score : {self.get_score()}",
                            (0, 0, 0))

    def get_state(self):
        state_matrix = np.zeros((self.height, self.width))
        state_matrix[self.fruit.position()] = 3
        for coordinate in self.player.position():
            state_matrix[coordinate] = 1
        state_matrix[self.player.head()] = 2
