import pygame
from random import randint
from time import sleep
from classes.Plataformas import Plataforma
from classes.Jogador import Jogador
from classes.Escadas import Escada
from classes.Fireball import Fireball
from constantes import *

# Inicializa o Pygame e carrega os recursos necessários
def inicializa():
    pygame.init()  # Inicializa o Pygame
    
    # Cria a janela do jogo e preenche com preto
    window = pygame.display.set_mode(DIMENSOES, vsync=True, flags=pygame.SCALED)
    window.fill((0, 0, 0))
    pygame.display.set_caption('First game')  # Define o título da janela

    # Inicializa o estado do jogo
    state = {
        't0': -1,   # Tempo inicial
    }
   
    state['grupos'] = {
        'plataformas': pygame.sprite.Group(),
        'escadas': pygame.sprite.Group(),
        'all_sprites': pygame.sprite.Group(),
        'fire_ball': pygame.sprite.Group()
    }
    state['vidas'] = 3

    # Carrega os assets do jogo
    assets = {}
    assets['background'] = pygame.image.load('assets/img/background.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], DIMENSOES)

    assets['ponte'] = pygame.image.load('assets/img/bridge.png') 
    assets['ponte'] = pygame.transform.scale(assets['ponte'], (90, 50))
    
    assets['coracao'] = pygame.image.load('assets/images/heart.png')
    assets['coracao'] = pygame.transform.scale(assets['coracao'], (30, 30))


    assets['gorila'] = pygame.image.load('assets/images/dk/dk2.png')
    assets['gorila'] = pygame.transform.scale(assets['gorila'],(100,100))

    assets['fire_ball'] = pygame.image.load('assets/images/fireball.png')
    assets['fire_ball'] = pygame.transform.scale(assets['fire_ball'],(30,30))

    # Imagens usadas para o jogador
    mario = {
        'climbing1': pygame.transform.scale(pygame.image.load('assets/images/mario/climbing1.png'),(60,60)),
        'climbing2': pygame.transform.scale(pygame.image.load('assets/images/mario/climbing2.png'),(60,60)),
        'jumping': pygame.transform.scale(pygame.image.load('assets/images/mario/jumping.png'),(60,60)),
        'running': pygame.transform.scale(pygame.image.load('assets/images/mario/running.png'),(60,60)),
        'standing': pygame.transform.scale(pygame.image.load('assets/images/mario/standing.png'),(60,60)),
    }
    mario['running_reverse'] = pygame.transform.flip(mario['running'], True, False)
    state['mario'] = mario['standing']
    state['rect_mario'] = state['mario'].get_rect()
    state['pos_mario'] = [0, 840]
    state['vel_mario'] = [0, 0]
    state['estado'] = STILL

    # Instancia o Jogador
    state['jogador'] = Jogador(mario, state['grupos'], state['pos_mario'][0], state['pos_mario'][1], state['vidas'])
    state['clock'] =  pygame.time.Clock()

    # Plataformas do jogo
    retangulos = {
    'retangulo': pygame.Rect((0, 312), (665, 29)),
    'retangulo1': pygame.Rect((52, 405), (665, 29)),
    'retangulo2': pygame.Rect((0, 528), (665, 29)),
    'retangulo3': pygame.Rect((52, 650), (665, 29)),
    'retangulo4': pygame.Rect((0, 777), (665, 20)),
    'retangulo5': pygame.Rect((0, 895), (720, 29)),
    'retangulo6': pygame.Rect((282, 211), (153, 28)),
    }

    # Escadas do jogo
    escadas = {
    'escada2': pygame.Rect((410, 214), (28, 110)),
    'escada3': pygame.Rect((623, 319), (28, 100)),
    'escada4': pygame.Rect((71, 412), (28, 83)),
    'escada5': pygame.Rect((595, 530), (28, 83)),
    'escada6': pygame.Rect((99, 655), (28, 83)),
    'escada7': pygame.Rect((554, 775), (38, 80))
    }

    # Bolas de fogo
    for i in range(5):
        Fireball(
            state['grupos'], assets['fire_ball'], list(retangulos.values())[i].x, 
            list(retangulos.values())[i].y - list(retangulos.values())[i].height,
            1 if i % 2 == 0 else -1
            )
    

    # Instancia Plataforma
    for retangulo in retangulos.values():
        Plataforma(state['grupos'], retangulo)

    # Instancia Escada
    for escada in escadas.values():
        Escada(state['grupos'], escada)

    return window, assets, state, retangulos, escadas, mario


# Recebe eventos do Pygame
def recebe_eventos(state, window, mario, assets, retangulos, escadas):

    # Calculo do fps
    t1 = pygame.time.get_ticks()
    t0 = state['t0']
    dt = (t1 - t0) / 1000
    fps = 1 / dt  # Calcula a taxa de quadros por segundo (FPS)
    state['t0'] = t1
    state['fps'] = fps
    state['t2'] = 0

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o evento QUIT foi acionado, retorna False
            return False
        
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                state['jogador'].state = RUN
                state['jogador'].image = mario['running_reverse']
                state['jogador'].vel_x -= VEL_X

            elif event.key == pygame.K_RIGHT:
                    state['jogador'].state = RUN
                    state['jogador'].image = mario['running']
                    state['jogador'].vel_x += VEL_X

            if event.key == pygame.K_UP:  
                if state['jogador'].colisao_escada():
                    state['jogador'].image = mario['climbing1']
                    state['jogador'].state = CLIMBING
                    state['jogador'].vel_y -= VEL_X
                    # state['vel_mario'][0] = 0

            if event.key == pygame.K_DOWN:  
                if state['jogador'].colisao_escada():
                    state['mario'] = mario['climbing1']
                    state['jogador'].state = CLIMBING
                    state['jogador'].vel_y += 80
                    state['jogador'].vel_x = 0

            if event.key == pygame.K_SPACE:
                if state['jogador'].state == STILL:
                    state['jogador'].jump()


        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                    state['jogador'].vel_x = 0
                    state['jogador'].image = mario['standing']
                    state['jogador'].state = STILL

            elif event.key == pygame.K_RIGHT:
                    state['jogador'].vel_x = 0
                    state['jogador'].image = mario['standing']
                    state['jogador'].state = STILL

            if event.key == pygame.K_UP:  
                if state['jogador'].colisao_escada():
                    state['jogador'].vel_y = 0 
                    state['jogador'].image = mario['standing']
                    state['jogador'].state = STILL

            if event.key == pygame.K_DOWN:  
                if state['jogador'].colisao_escada():
                    state['jogador'].vel_y = 0
                    state['jogador'].image = mario['standing']
                    state['jogador'].state = STILL

    state['grupos']['all_sprites'].update()

    return True


def desenha(window, assets, state, retangulos, escadas, mario ):
    

    # Desenha as escadas
    for escada in escadas.values():
        pygame.draw.rect(window, 'blue', escada)

    # Desenha o background
    window.blit(assets['background'], (0, 0))

    
    # Desenha os corações
    for i in range(0, 30 * state['jogador'].vidas, 30):
        window.blit(assets['coracao'], (i, 20))

    # Desenha o jogador
    state['grupos']['all_sprites'].draw(window)  

    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state, retangulos, escadas, mario):
    
    while recebe_eventos(state, window, mario, assets, retangulos, escadas):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        state['clock'].tick(60)
        desenha(window, assets, state, retangulos, escadas, mario)

if __name__ == '__main__':
    
    w, assets, state, retangulos, escadas, mario = inicializa()  # Inicializa o Pygame e carrega os recursos necessários
    game_loop(w, assets, state, retangulos, escadas, mario)  # Inicia o loop principal do jogo
