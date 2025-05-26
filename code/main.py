import pygame
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
        self.direction = pygame.Vector2()
        self.speed = 300
        
        # cooldown
        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown_duration = 400

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        self.rect.center += self.direction * self.speed * dt

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

        self.direction = self.direction.normalize() if self.direction else self.direction

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(self.rect.center, laser_image, all_sprites)
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

        if not self.can_shoot:
            if pygame.time.get_ticks() - self.shoot_time >= self.cooldown_duration:
                self.can_shoot = True

class Star(pygame.sprite.Sprite):
    def __init__(self, image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(center = pos)
        self.speed = 700

    def update(self, dt):
        self.rect.centery -= self.speed * dt
        if self.rect.bottom <= 0:
            self.kill()
        if pygame.sprite.spritecollide(self, meteor_sprites, True):
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, image, groups):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(midbottom = (randint(0, WINDOW_WIDTH), 0))
        self.speed = 300
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)

    def update(self, dt):
        self.rect.center += self.speed * self.direction * dt
        if self.rect.top >= WINDOW_HEIGHT:
            self.kill()


class Text(pygame.sprite.Sprite):
    def __init__(self, text, groups):
        super().__init__(groups)
        self.image = font.render(text, True, (255, 0, 0))
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))


def display_score():
    '''
    luati timpul curent
    transformati in string
    creati un font
    creati suprfata din font
    creati rect din suprafata
    si dupa blit jos in mijloc
    '''
    pass


# game init
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 600 # depinde de ecran
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("codemy-space-shooter")
running = True
clock = pygame.time.Clock()
font = pygame.font.Font("images/Oxanium-Bold.ttf", 60)

#import
star_image = pygame.image.load("images/star.png").convert_alpha()
laser_image = pygame.image.load("images/laser.png").convert_alpha()
meteor_image = pygame.image.load("images/meteor.png").convert_alpha()


# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
for _ in range(20):
    Star(star_image, all_sprites)
player = Player(all_sprites)


# custom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)
alive = True

# main loop
while running:
    dt = clock.tick() / 1000

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(meteor_image, (all_sprites, meteor_sprites))
            
    # update 
    all_sprites.update(dt)

    if pygame.sprite.spritecollide(player, meteor_sprites, False):
        alive = False
        player.kill()

    # draw
    display_surface.fill("#3a2e3f")
    if not alive:
        Text("Ai pierdut!", all_sprites)
    else:
        display_score()
    
    all_sprites.draw(display_surface)



    pygame.display.update()


pygame.quit()