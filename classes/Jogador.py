import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, imagens, grupos, x, y, vidas):
        super().__init__()
        self.imagens = imagens
        self.image = imagens['standing']
        self.rect = self.image.get_rect()
        self.grupos = grupos
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 0
        self.vidas = vidas
        self.state = STILL
        self.dt = 0
        self.grupos['all_sprites'].add(self)

    def colisao_escada(self):
        colisoes = pygame.sprite.spritecollide(self, self.grupos['escadas'], False)
        if colisoes:
            return True
        else:
            return False


    def update(self):
        if not self.colisao_escada():
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

        now = pygame.time.get_ticks()

        if now - self.dt > 2000:
            colisoes_fire_ball = pygame.sprite.spritecollide(self, self.grupos['fire_ball'], False)
            if colisoes_fire_ball:
                self.dt = now
                print('antes:', self.vidas)
                self.vidas -= 1
                print('depois:', self.vidas)

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo e não estiver na escada
        if self.state == STILL:
            if not self.colisao_escada():
                self.vel_y -= JUMP_SIZE
                self.state = JUMPING