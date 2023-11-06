import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, imagens, grupos, x, y):
        super().__init__()
        self.imagens = imagens
        self.image = imagens['standing']
        self.rect = self.image.get_rect()
        self.grupos = grupos
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.state = STILL
        self.grupos['all_sprites'].add(self)

    def update(self):
        self.vel_y += G

        if self.vel_y > 0:
            self.state = FALLING

        self.rect.y += self.vel_y

        colisoes = pygame.sprite.spritecollide(self, self.grupos['plataformas'], False)

        for plataforma in colisoes:
            if self.vel_y > 0:
                self.rect.bottom = plataforma.rect.top
                self.vel_y = 0
                self.state = STILL
            
        self.rect.x += self.vel_x
    
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= DIMENSOES[0]:
            self.rect.right = DIMENSOES[0] - 1

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        print('cond1')
        if self.state == STILL:
            print('cond2')
            self.vel_y -= JUMP_SIZE
            self.state = JUMPING