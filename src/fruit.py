import pygame
import random


class Fruit:
    def __init__(self, x=0, y=0):
        self.color = [255, 127, 127]
        self.x = x
        self.y = y

    def move(self, grid, forbidden):
        coordinates = []
        for x in range(0, grid.width):
            for y in range(0, grid.height):
                if (x, y) not in forbidden:
                    coordinates.append((x, y))
        if len(coordinates) == 0:
            return False
        self.x, self.y = random.choice(coordinates)
        return True

    def draw(self, screen, size):
        pygame.draw.rect(screen, self.color,
                         (self.x * size, self.y * size, size, size))

    def position(self):
        return (self.x, self.y)
