import pygame
import sprite1

all_sprites = pygame.sprite.Group()
hero = sprite1.Hero()
all_sprites.add(hero)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()


