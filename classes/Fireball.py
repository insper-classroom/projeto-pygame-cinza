import pygame

class Fireball(pygame.sprite.Sprite):
    def __init__(self, image, grupos, x, y):
        super().__init__()
        self.image = image
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 85
        self.highest_y = self.rect.bottom
        self.grupos['all_sprites'].add(self)

    