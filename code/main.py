import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))


# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True
clock = pygame.time.Clock()


# sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


# main loop
while running:
    dt = clock.tick() / 1000

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    all_sprites.update()
    display_surface.fill(pygame.Color(25, 8, 33))
    all_sprites.draw(display_surface)

    pygame.display.update()


pygame.quit()