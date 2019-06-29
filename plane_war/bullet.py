import pygame
from pygame.sprite import Sprite
import os.path as path

import setting

class HeroBullet(Sprite):

    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load(path.join(setting.img_folder,"bullet2.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, *args):
        self.rect.y -= 10

        if self.rect.bottom < 0:
            self.kill()

