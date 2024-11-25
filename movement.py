import pygame


def handle_input(player, grid):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.change_direction('left')
    if keys[pygame.K_RIGHT]:
        player.change_direction('right')
    if keys[pygame.K_UP]:
        player.change_direction('up')
    if keys[pygame.K_DOWN]:
        player.change_direction('down')
