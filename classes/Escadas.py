import pygame
from classes.Jogador import Jogador
from constantes import *

class Escada(pygame.sprite.Sprite):
    def __init__(self, grupos, escada):
        super().__init__()
        self.rect = escada
        grupos['escadas'].add(self)

    def colisao_escada(self):
        colisoes = pygame.sprite.spritecollide(self, self.grupos['escadas'], False)
        for colisao in colisoes:
            self.state = CLIMBING