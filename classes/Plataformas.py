import pygame

class Plataforma(pygame.sprite.Sprite):
    def __init__(self, grupos, retangulo):
        super().__init__()
        self.rect = retangulo
        grupos['plataformas'].add(self)
