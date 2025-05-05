import pygame
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True
clock = pygame.time.Clock()

# player_surface = pygame.image.load("images/player.png").convert_alpha()
# player_rect = player_surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)) 
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

meteor_surface = pygame.image.load("images/meteor.png").convert_alpha()
meteor_rect = meteor_surface.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

star_surface = pygame.image.load("images/star.png").convert_alpha()

direction = pygame.math.Vector2()
speed = 300

star_count = 20

random_x = [randint(0, WINDOW_WIDTH) for _ in range(star_count)]
random_y = [randint(0, WINDOW_HEIGHT) for _ in range(star_count)]

# main loop
while running:
    dt = clock.tick() / 1000

    # evenimente
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    all_sprites.update()

    display_surface.fill(pygame.Color(25, 8, 33))
    all_sprites.draw(display_surface)


    pygame.display.update()

pygame.quit()