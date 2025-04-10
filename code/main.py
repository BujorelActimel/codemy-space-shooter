import pygame
from random import randint

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True

player_surface = pygame.image.load("images/player.png").convert_alpha()
star_surface = pygame.image.load("images/star.png").convert_alpha()

x = 100
star_count = 20

random_x = [randint(0, WINDOW_WIDTH) for _ in range(star_count)]
random_y = [randint(0, WINDOW_HEIGHT) for _ in range(star_count)]

# main loop
while running:
    # evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # desenam
    display_surface.fill('steelblue4')

    for i in range(star_count):
        display_surface.blit(star_surface, (random_x[i], random_y[i]))
        
    display_surface.blit(player_surface, (x, 200))

    x += 0.1

    pygame.display.update()

pygame.quit()