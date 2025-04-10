import pygame
from random import randint

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True

player_surface = pygame.image.load("images/player.png").convert_alpha()
player_rect = player_surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) 

meteor_surface = pygame.image.load("images/meteor.png").convert_alpha()
meteor_rect = meteor_surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

star_surface = pygame.image.load("images/star.png").convert_alpha()

direction = 1
speed = 0.4

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
    display_surface.fill(pygame.Color(25, 8, 33))

    for i in range(star_count):
        display_surface.blit(star_surface, (random_x[i], random_y[i]))
        
    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(player_surface, player_rect)

    print(player_rect.right)

    # if player_rect.right >= WINDOW_WIDTH or player_rect.left <= 0:
    #     direction *= -1
    
    player_rect.x += direction * speed

    if player_rect.x > WINDOW_WIDTH:
        player_rect.right = 0

    pygame.display.update()

pygame.quit()