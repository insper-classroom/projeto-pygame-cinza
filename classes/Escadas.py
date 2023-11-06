import pygame

class Escada(pygame.sprite.Sprite):
    def __init__(self, grupos, escada):
        super().__init__()
        self.rect = escada
        grupos['escadas'].add(self)