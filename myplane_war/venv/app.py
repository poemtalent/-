import pygame
import sys
import os

import settings
import sprite1
import database
import tools

# 只是起到初始化的作用，无程序逻辑。但是这两句话必须有。
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((settings.GameForm.WIDTH, settings.GameForm.HEIGHT))    # 显示游戏框
pygame.display.set_caption("李诗才的飞机大战") # 左上角显示游戏名字

clock = pygame.time.Clock() # 用于控制游戏循环一次所需要的时间
bg_img = pygame.image.load(os.path.join(settings.image_folder, 'background.png'))

# all_sprites = pygame.sprite.Group()
# hero = sprite.Hero()
# all_sprites.add(hero)
# mobs = pygame.sprite.Group()
# bullets = pygame.sprite.Group()

# for i in range(8):
#     mob = sprite.Mob()
#     all_sprites.add(mob)
#     mobs.add(mob)
tools.creat_enemys()
# 让游戏循环
while True:
    clock.tick(settings.FPS) # 控制游戏每秒循环的次数

    # 事件监测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 看是否满足退出程序的条件
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame. K_SPACE:
                database.hero.shoot()
    tools.bullet_hits()
    if tools.hero_hits():
        sys.exit(0)
    screen.blit(bg_img, (0, 0))
    database.all_sprites.update()
    database.all_sprites.draw(screen)

    pygame.display.flip()
