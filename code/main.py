import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("codemy-space-shooter")

running = True

player_surface = pygame.Surface((100, 200))
player_surface.fill('orange')

x = 100

# main loop
while running:
    # evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # desenam
    display_surface.fill('steelblue4')

    display_surface.blit(player_surface, (x, 200))
    x += 0.1

    pygame.display.update()

pygame.quit()