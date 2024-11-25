import pygame
import random


class Snake:
    def __init__(self, x, y, cell_size, velocity):
        self.x = [x]
        self.y = [y]
        self.color = [127, 255, 127]
        self.head_color = [0, 255, 0]
        self.direction = ['right']
        self.cell_size = cell_size
        self.size = 1
        self.velocity = velocity
        self.tick = 0
        self.last = None
        self.next_direction = 'right'

    def grow(self):
        if self.last is None:
            return
        x, y, dir = self.last
        self.x.append(x)
        self.y.append(y)
        self.direction.append(dir)
        self.size += 1

    def move(self, grid):
        self.tick = (self.tick + 1) % self.velocity
        if self.tick != 0:
            return True
        self.direction[0] = self.next_direction
        self.last = [self.x[-1], self.y[-1], self.direction[-1]]
        for i in range(len(self.x)-1, -1, -1):
            if self.direction[i] == 'left':
                if self.x[i] == 0:
                    return False
                self.x[i] -= grid.step
            if self.direction[i] == 'right':
                if self.x[i] + grid.step == grid.width:
                    return False
                self.x[i] += grid.step
            if self.direction[i] == 'up':
                if self.y[i] == 0:
                    return False
                self.y[i] -= grid.step
            if self.direction[i] == 'down':
                if self.y[i] + grid.step == grid.height:
                    return False
                self.y[i] += grid.step
            if (self.x[i], self.y[i]) in zip(self.x[i+1:], self.y[i+1:]):
                return False
            if i != 0:
                self.direction[i] = self.direction[i-1]

        return True

    def change_direction(self, new_direction):
        if self.size == 1 or \
                self.direction[0] == 'left' and new_direction != 'right' or \
                self.direction[0] == 'right' and new_direction != 'left' or \
                self.direction[0] == 'up' and new_direction != 'down' or \
                self.direction[0] == 'down' and new_direction != 'up':
            self.next_direction = new_direction

    def draw(self, screen):
        for i in range(self.size):
            pygame.draw.rect(screen, self.color if i != 0 else self.head_color,
                             (self.x[i], self.y[i],
                              self.cell_size, self.cell_size))

    def position(self):
        return [coord for coord in zip(self.x, self.y)]

    def head(self):
        return (self.x[0], self.y[0])


class Fruit:
    def __init__(self, size):
        self.color = [255, 127, 127]
        self.x = 0
        self.y = 0
        self.size = size

    def move(self, grid, forbidden):
        coordinates = []
        for x in range(0, grid.width, grid.cell_size):
            for y in range(0, grid.height, grid.cell_size):
                if (x, y) not in forbidden:
                    coordinates.append((x, y))
        if len(coordinates) == 0:
            return False
        self.x, self.y = random.choice(coordinates)
        return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.size, self.size))

    def position(self):
        return (self.x, self.y)
