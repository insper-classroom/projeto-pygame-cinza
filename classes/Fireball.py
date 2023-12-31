import pygame
from constantes import *

class Fireball(pygame.sprite.Sprite):
    def __init__(self, grupos, image, x, y, vel):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y - 15
        self.vel = vel
        self.count = 0
        self.grupos = grupos
        grupos['fire_ball'].add(self)
        grupos['all_sprites'].add(self)
  
    def update(self):
        self.rect.x += self.vel

        if self.rect.left < 0:
            self.vel *= -1
            self.rect.left = 0
            
        elif self.rect.right >= DIMENSOES[0]:
            self.vel *= -1
            self.rect.right = DIMENSOES[0] - 1