import pygame
from movement import handle_input
from player import Snake, Fruit
from grid import Grid

HEIGHT = 600
WIDTH = 600
FPS = 60
grid_size = 50

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Grid")

grid = Grid(WIDTH, HEIGHT, grid_size)
player = Snake(100, 100, grid_size, FPS // 6)
fruit = Fruit(grid_size)
fruit.move(grid, set(player.position()))

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input(player, grid)
    screen.fill((255, 255, 255))
    running = player.move(grid)
    if fruit.position() == player.head():
        running = fruit.move(grid, set(player.position()))
        if running:
            player.grow()

    player.draw(screen)
    fruit.draw(screen)
    grid.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
