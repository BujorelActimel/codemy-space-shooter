import pygame
from random import randint

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True
clock = pygame.time.Clock()

player_surface = pygame.image.load("images/player.png").convert_alpha()
player_rect = player_surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) 

meteor_surface = pygame.image.load("images/meteor.png").convert_alpha()
meteor_rect = meteor_surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

star_surface = pygame.image.load("images/star.png").convert_alpha()

direction = pygame.math.Vector2(1, -1)
speed = 500

star_count = 20

random_x = [randint(0, WINDOW_WIDTH) for _ in range(star_count)]
random_y = [randint(0, WINDOW_HEIGHT) for _ in range(star_count)]

# main loop
while running:
    dt = clock.tick() / 1000
    # print(clock.get_fps())

    # evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: # daca cineva a apast o tasta
            if event.key == pygame.K_1:
                print(1)
            if event.key == pygame.K_RETURN:
                player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            

    # desenam
    display_surface.fill(pygame.Color(25, 8, 33))

    for i in range(star_count):
        display_surface.blit(star_surface, (random_x[i], random_y[i]))
        
    display_surface.blit(meteor_surface, meteor_rect)
    display_surface.blit(player_surface, player_rect)

    # if player_rect.top < 0:
    #     player_rect.top = 0
    #     direction.y *= -1

    # if player_rect.bottom > WINDOW_HEIGHT:
    #     player_rect.bottom = WINDOW_HEIGHT
    #     direction.y *= -1
    
    # if player_rect.left < 0:
    #     player_rect.left = 0
    #     direction.x *= -1

    # if player_rect.right > WINDOW_WIDTH:
    #     player_rect.right = WINDOW_WIDTH
    #     direction.x *= -1

    # player_rect.center += direction * speed * dt

    pygame.display.update()

pygame.quit()