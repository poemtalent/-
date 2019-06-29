import random
import pygame

from pygame.sprite import Sprite
import os.path as path

import setting
import info


class CommonEnermy(Sprite):

    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.image.load(path.join(setting.img_folder,"enemy1.png"))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self, *args):
        speed = 5
        self.rect.y += speed

        if self.rect.y > setting.SCREEN_HEIGHT:
            self.kill()

class EnermyFactory:
    def __init__(self):
        self.bus = info.DataBus()
        # 上一次普通敌军生成时间
        self.last_common_time = pygame.time.get_ticks()

    def generate_common_enermy(self):
        x = random.randint(26,setting.SCREEN_WIDTH-26)
        y = -30
        common_enermy = CommonEnermy(x,y)
        self.bus.add_sprite(common_enermy)
        self.bus.add_enermy(common_enermy)



    def generate_enermy(self):
        now = pygame.time.get_ticks()
        if now - self.last_common_time > 800:
            self.generate_common_enermy()
            self.last_common_time = now


class Explosion(Sprite):
    animations = dict()

    def __init__(self,who,center):
        super().__init__()
        self.animation = []
        self.load()

        if who == "enermy":
            self.animation = Explosion.animations['emermy_anim']

        #
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        # 上一帧图片的显示时间
        self.last_frame_time = pygame.time.get_ticks()


    def load(self):
        # 加载敌军爆炸图片资源
        if Explosion.animations.get("emermy_anim") is None:
            enemy_explosion_res = []
            for i in range(0, 4):
                filename = 'enemy1_down{}.png'.format(i+1)
                img = pygame.image.load(path.join(setting.img_folder, filename))
                enemy_explosion_res.append(img)
            Explosion.animations['emermy_anim'] = enemy_explosion_res


    def update(self, *args):
        now = pygame.time.get_ticks()
        if now - self.last_frame_time > 100:
            if self.frame == len(self.animation) - 1:
                self.kill()
            else:
                self.frame += 1
                self.image = self.animation[self.frame]


class Button(Sprite):

    def __init__(self,img_name,offset_y):
        super().__init__()
        self.image = pygame.image.load(path.join(setting.img_folder, img_name))
        self.rect = self.image.get_rect()
        self.rect.center = setting.SCREEN_WIDTH / 2, (setting.SCREEN_HEIGHT / 2) + offset_y




    @staticmethod
    def check_click(button):
        pressed = pygame.mouse.get_pressed()
        if pressed == (1, 0, 0):
            print("左键点击")
            pos = pygame.mouse.get_pos()
            button_x = pos[0]
            button_y = pos[1]

            if button.rect.left < button_x < button.rect.right and button.rect.top < button_y < button.rect.bottom :
                return True

            return False



