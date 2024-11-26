import pygame


class Player:
    def __init__(self, x=1, y=1, start_direction='right'):
        self.x = [x]
        self.y = [y]
        self.color = [127, 255, 127]
        self.head_color = [0, 255, 0]
        self.direction = [start_direction]
        self.size = 1
        self.last = None

    def grow(self):
        if self.last is None:
            return

        x, y, dir = self.last
        self.x.append(x)
        self.y.append(y)
        self.direction.append(dir)
        self.size += 1

    def move(self, grid):
        self.last = [self.x[-1], self.y[-1], self.direction[-1]]
        for i in range(len(self.x)-1, -1, -1):
            if self.direction[i] == 'left':
                if self.x[i] == 0:
                    return False
                self.x[i] -= 1

            if self.direction[i] == 'right':
                if self.x[i] + 1 == grid.width:
                    return False
                self.x[i] += 1

            if self.direction[i] == 'up':
                if self.y[i] == 0:
                    return False
                self.y[i] -= 1

            if self.direction[i] == 'down':
                if self.y[i] + 1 == grid.height:
                    return False
                self.y[i] += 1

            if (self.x[i], self.y[i]) in zip(self.x[i+1:], self.y[i+1:]):
                return False

            if i != 0:
                self.direction[i] = self.direction[i-1]

        return True

    def can_change_direction(self, direction):
        return self.size == 1 or \
                (self.direction[0] == 'left' and direction != 'right') or \
                (self.direction[0] == 'right' and direction != 'left') or \
                (self.direction[0] == 'up' and direction != 'down') or \
                (self.direction[0] == 'down' and direction != 'up')

    def change_direction(self, new_direction):
        if self.can_change_direction(new_direction):
            self.direction[0] = new_direction

    def draw(self, screen, size):
        for i in range(self.size):
            pygame.draw.rect(screen, self.color if i != 0 else self.head_color,
                             (self.x[i] * size, self.y[i] * size, size, size))

    def position(self):
        return [coord for coord in zip(self.x, self.y)]

    def head(self):
        return (self.x[0], self.y[0])
