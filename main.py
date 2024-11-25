import pygame
from game import SnakeGame

FPS = 5
GUI = True

pygame.init()
snake = SnakeGame()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    direction = None

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = 'left'
    if keys[pygame.K_RIGHT]:
        direction = 'right'
    if keys[pygame.K_UP]:
        direction = 'up'
    if keys[pygame.K_DOWN]:
        direction = 'down'

    snake.move(direction)
    if GUI:
        snake.draw()
        pygame.display.flip()
    if snake.ended:
        running = False
    clock.tick(FPS)


pygame.quit()
