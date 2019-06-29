import sprite1
import database
import pygame
def creat_enemys():
    for i in range(8):
        creat_enemy()

def creat_enemy():
    m = sprite1.Mob()
    database.all_sprites.add(m)
    database.mobs.add(m)

def bullet_hits():
    hits = pygame.sprite.groupcollide(database.mobs, database.bullets, True, True)
    for hit in hits:
        creat_enemy()

def hero_hits():
    hits = pygame.sprite.spritecollide(database.hero, database.mobs, False)
    return hits