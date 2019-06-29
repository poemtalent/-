import pygame
import hero

from tool import Music,GameHelper
from npc import Button


class DataBus:
    instance = None

    def __new__(cls, *args, **kwargs):
        if DataBus.instance is None:
            DataBus.instance = super().__new__(cls)
            DataBus.instance.reset()

        return DataBus.instance

    def reset(self):
        self.all_sprites = pygame.sprite.Group()
        self.score = 0
        self.is_game_over = False
        self.hero_bullets = pygame.sprite.Group()
        self.enermy_bullets = pygame.sprite.Group()
        self.enermys = pygame.sprite.Group()
        self.music = Music()
        self.game_helper = GameHelper()
        # self.game_over_button = Button("gameover.png")
        # self.game_over_button_clicked = False

        #初始化英雄
        self._init_hero()

    def _init_hero(self):
        self.hero = hero.Hero()
        self.add_sprite(self.hero )

    def add_sprite(self,sprite):
        self.all_sprites.add(sprite)

    def remove_sprite(self,sprite):
        self.all_sprites.remove(sprite)

    def add_hero_bullte(self,hreo_bullet):
        self.hero_bullets.add(hreo_bullet)

    def add_enermy(self,enermy):
        self.enermys.add(enermy)

    def add_socre(self,score):
        self.score += score
        print("当前得分：%d" % self.score )
