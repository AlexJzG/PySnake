import pygame


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = [127, 127, 127]

    def draw(self, screen, size):
        for x in range(0, self.width):
            for y in range(0, self.height):
                rect = pygame.Rect(x * size, y * size, size, size)
                pygame.draw.rect(screen, self.color, rect, 1)
