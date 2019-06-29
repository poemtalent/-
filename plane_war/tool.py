import pygame
import os.path as path
import sys

import setting
import info
from npc import Explosion,Button

class Music:
    """
    音乐播放类
    """

    singleton = None

    def __new__(cls, *args, **kwargs):
        if Music.singleton is None:
            Music.singleton = super().__new__(cls, *args, **kwargs)
            Music.singleton.initial()
        return Music.singleton

    def initial(self):
        pygame.mixer.init()
        self.die_music = pygame.mixer.Sound(path.join(setting.snd_folder, "enemy1_down.wav"))
        self.bgm = pygame.mixer.Sound(path.join(setting.snd_folder, "game_music.ogg"))
        self.shoot_music = pygame.mixer.Sound(path.join(setting.snd_folder, "bullet.wav"))
        self.enermy_die_music = pygame.mixer.Sound(path.join(setting.snd_folder, "enemy1_down.wav"))

        self.set_config()

    def set_config(self):
        """
        配置声音
        :return:
        """
        self.bgm.set_volume(0.5)

    def play_die_music(self):
        self.die_music.play()

    def play_bgm(self):
        self.bgm.play(loops=-1)

    def play_shoot_music(self):
        self.shoot_music.play()

    def play_enmery_die_music(self):
        self.enermy_die_music.play()


class GameHelper:
    def __init__(self):
        self.bus = info.DataBus()

    def collision(self):
        '''
        全局碰撞检测
        :return:
        '''

        # 子弹和敌军的碰撞检测
        hits = pygame.sprite.groupcollide(self.bus.hero_bullets, self.bus.enermys, True, True)
        if hits:
            self.handle_collision_bullet_enermy(hits)

        # 敌军与我们碰撞
        enermys = self.bus.enermys.sprites()
        for e in enermys:
            if pygame.sprite.collide_rect(self.bus.hero,e):
                self.bus.is_game_over = True
                print("游戏结束....")



    def handle_collision_bullet_enermy(self,hits):
        # 加分
        self.bus.add_socre(10 * len(hits))
        # 敌人死亡声音
        self.bus.music.play_die_music()

        # 敌人爆炸动画
        for b, e in hits.items():
            for eson in e:
                explosion = Explosion('enermy', eson.rect.center)
                self.bus.add_sprite(explosion)

    def draw_game_over_view(self):
        self.bus.all_sprites.empty()
        game_over_button = Button("gameover.png", -40)
        begin_button = Button("again.png",40)
        self.bus.all_sprites.add(game_over_button)
        self.bus.all_sprites.add(begin_button)

        if Button.check_click(game_over_button):
            sys.exit()

        if Button.check_click(begin_button):
            self.bus.reset()
            self.bus.is_game_over = False

