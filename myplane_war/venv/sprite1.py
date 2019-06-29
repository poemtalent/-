import pygame
import os
import random

import settings


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        hero_image = pygame.image.load(os.path.join(settings.image_folder, 'me1.png'))
        self.image = pygame.transform.scale(hero_image, (50, 60))
        # self.image = hero_image
        self.rect = self.image.get_rect()
        self.rect.center = (settings.GameForm.WIDTH / 2, settings.GameForm.HEIGHT - 30)
        self.speedy = 5

    def update(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.rect.x -= self.speedy
            if self.rect.x < 0:
                self.rect.x = 0

        if keystate[pygame.K_RIGHT]:
            self.rect.x += self.speedy
            if self.rect.x > 400 - 50:
                self.rect.x = 400 - 50

        if keystate[pygame.K_UP]:
            self.rect.y -= self.speedy
            if self.rect.y < 0:
                self.rect.y = 0

        if keystate[pygame.K_DOWN]:
            self.rect.y += self.speedy
            if self.rect.y > 600 - 60:
                self.rect.y = 600 - 60
        # print('({}, {})'.format(self.rect.x, self.rect.y))

    def shoot(self):
        import database
        bullet = Bullet(self.rect.centerx, self.rect.top)
        # database.all_sprites.add(bullet)
        database.bullets.add(bullet)
        database.all_sprites.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface((30, 40))
        # self.image.fill(settings.BLUE)
        enemy_img = pygame.image.load(os.path.join \
                                          (settings.image_folder, 'enemy{}.png'.format(random.randint(1, 2))))
        self.image = pygame.transform.scale(enemy_img, (50, 60))
        # self.image = enemy_img
        self.image.set_colorkey(settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.width = 50
        self.rect.height = 60
        self.rect.x = random.randrange(settings.GameForm.WIDTH - self.rect.width)
        self.rect.y = -40
        self.speedx = random.randrange(-4, 4)
        self.speedy = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > settings.GameForm.HEIGHT:
            self.rect.x = random.randrange(settings.GameForm.WIDTH - self.rect.width)
            self.rect.y = -40
            self.speedy = random.randint(3, 8)

        self.rect.x += self.speedx
        if self.rect.x < 0 or self.rect.x > settings.GameForm.WIDTH - 30:
            self.speedx = -self.speedx


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        bullet_image = pygame.image.load \
            (os.path.join(settings.image_folder, 'bullet1.png'))
        self.image = bullet_image
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.bottom += self.speedy
        if self.rect.bottom < 0:
            self.kill()