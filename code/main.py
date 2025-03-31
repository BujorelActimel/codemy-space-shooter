import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("codemy-space-shooter")

running = True

player_surface = pygame.Surface((100, 200))
player_surface.fill('orange')

cursor_surface = pygame.Surface((5, 5))

x = 100
# increment = 0.1

# main loop
while running:
    # evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         if increment == 0:
        #             increment = 0.1
        #         else:
        #             increment = 0

    # desenam
    display_surface.fill('steelblue4')

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # display_surface.blit(player_surface, (x, 200))
    # x += increment
    display_surface.blit(cursor_surface, (mouse_x, mouse_y))

    pygame.display.update()

pygame.quit()