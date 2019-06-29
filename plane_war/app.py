import pygame
import sys
import os.path as path
import setting
import time

from info import DataBus
from npc import EnermyFactory,Button

class App:

    def start(self):
        pygame.init()
        pygame.mixer.init()

        screen = pygame.display.set_mode((400,600))
        pygame.display.set_caption("飞机大战")
        bus = DataBus()
        clock = pygame.time.Clock()
        bg_img = pygame.image.load(path.join(setting.img_folder,"background.png")).convert()
        screen.blit(bg_img,(0,0))

        bus.music.play_bgm()

        ef = EnermyFactory()

        # 让绘制的结果，一次显现
        pygame.display.flip()

        while True:
            clock.tick(40)
            screen.blit(bg_img, (0, 0))
            if not bus.is_game_over:
                # 生成敌人
                ef.generate_enermy()

                bus.all_sprites.update()
                # 碰撞检测
                bus.game_helper.collision()

            if bus.is_game_over:
                bus.game_helper.draw_game_over_view()

            bus.all_sprites.draw(screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()




App().start()
