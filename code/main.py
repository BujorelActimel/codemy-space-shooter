import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

# main loop
while running:
    # evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # desenam
    pass

pygame.quit()