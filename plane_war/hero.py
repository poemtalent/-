import pygame
from pygame.sprite import Sprite
import os.path as path

import setting
from bullet import HeroBullet
import info


class Hero(Sprite):
    def __init__(self):
        super().__init__()
        image = pygame.image.load(path.join(setting.img_folder,"me1.png"))
        self.image = pygame.transform.scale(image,(50,61))
        self.rect = self.image.get_rect()
        self.rect.center = (setting.SCREEN_WIDTH / 2,setting.SCREEN_HEIGHT - 40)
        self.bus = info.DataBus()
        self.last_shoot_time = pygame.time.get_ticks()


    def update(self, *args):
        speed = 10

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            if self.rect.x > 0:
                self.rect.x -= speed

        if keystate[pygame.K_RIGHT]:
            if self.rect.x < setting.SCREEN_WIDTH - self.rect.width:
                self.rect.x += speed

        #自动射击
        self.shoot()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > 200:
            bullet = HeroBullet(self.rect.centerx,self.rect.top)
            self.bus.music.play_shoot_music()
            self.bus.add_sprite(bullet)
            self.bus.add_hero_bullte(bullet)
            self.last_shoot_time = now

