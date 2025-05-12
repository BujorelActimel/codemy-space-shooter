import pygame
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.speed = 300
        self.direction = pygame.Vector2()

        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time > self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        just_presed_keys = pygame.key.get_just_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        self.rect.center += self.direction * self.speed * dt

        self.direction = self.direction.normalize() if self.direction else self.direction

        if just_presed_keys[pygame.K_SPACE] and self.can_shoot:
            # print("shoot")
            Laser(laser_surf, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        self.laser_timer()


class Laser(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = pos)
        self.speed = 500

    def update(self, dt):
        self.rect.centery -= self.speed * dt
        if self.rect.bottom < 0:
            self.kill()
        if pygame.sprite.spritecollide(self, meteor_sprites, True):
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom = (randint(0, WINDOW_WIDTH), 0))
        self.speed = 300
        self.direction = pygame.Vector2(uniform(-0.5, 0.5),1)

    def update(self, dt):
        self.rect.center += self.speed * self.direction * dt
        if self.rect.top > WINDOW_HEIGHT:
            self.kill() 


class Star(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))


# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True
clock = pygame.time.Clock()


# import
laser_surf = pygame.image.load("images/laser.png").convert_alpha()
meteor_surf = pygame.image.load("images/meteor.png").convert_alpha()
star_surf = pygame.image.load("images/star.png").convert_alpha()


# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
for i in range(20):
    Star(star_surf, all_sprites)
player = Player(all_sprites)


# custom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)


# main loop
while running:
    dt = clock.tick() / 1000

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            # print("meteor")
            Meteor(meteor_surf, (all_sprites, meteor_sprites))
    
    # update         
    all_sprites.update(dt)

    # draw game
    display_surface.fill(pygame.Color(25, 8, 33))
    all_sprites.draw(display_surface)

    pygame.display.update()


pygame.quit()