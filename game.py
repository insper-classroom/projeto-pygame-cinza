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
    pygame.display.set_caption('Donkey Fire')  # Define o título da janela


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

    state['vidas'] = 4

    state['estado_tela'] = 0

    state['restart'] = False

    state['princesa'] = STILL


    # Carrega os assets do jogo
    assets = {}

    assets['background'] = pygame.transform.scale(pygame.image.load('assets/img/background.png').convert_alpha(), DIMENSOES)

    assets['ponte'] = pygame.transform.scale(pygame.image.load('assets/img/bridge.png'), (90, 50))
    
    assets['coracao'] = pygame.transform.scale(pygame.image.load('assets/images/heart.png'), (30, 30))

    assets['princesa1'] = pygame.transform.scale(pygame.image.load('assets/images/peach/peach1.png'), (60, 60))

    assets['princesa2'] = pygame.transform.scale(pygame.image.load('assets/images/peach/peach2.png'), (60, 60))

    assets['pos_princesa'] = (282, 150)

    assets['fire_ball'] = pygame.transform.scale(pygame.image.load('assets/images/fireball.png'), (30, 30))

    assets['welcome'] = pygame.transform.scale(pygame.image.load('assets/images/welcome.png').convert_alpha(), DIMENSOES)

    assets['win'] = pygame.transform.scale(pygame.image.load('assets/images/win_screen.png').convert_alpha(), DIMENSOES)

    assets['game_over'] = pygame.transform.scale(pygame.image.load('assets/images/game_over.png').convert_alpha(), DIMENSOES)

    assets['dormes'] = pygame.transform.scale(pygame.image.load('assets/images/dormes.png').convert_alpha(), DIMENSOES)

    assets['barril'] = pygame.transform.scale(pygame.image.load('assets/images/barril.png').convert_alpha(), (70, 100))

    assets['fogo'] = pygame.transform.scale(pygame.image.load('assets/images/fire.png').convert_alpha(), (100, 50))

    # Carrega e toca a música de fundo
    assets['background_music'] = 'assets/snd/Battle.mp3'
    pygame.mixer.music.load(assets['background_music'])
    pygame.mixer.music.play()


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
    state['jogador'] = Jogador(mario, state['grupos'], state['pos_mario'][0], state['pos_mario'][1], state['vidas'], state['estado_tela'])
    state['clock'] =  pygame.time.Clock()

    # Plataformas do jogo
    retangulos = {
    'retangulo1': pygame.Rect((0, 312), (665, 10)),
    'retangulo2': pygame.Rect((52, 405), (665, 10)),
    'retangulo3': pygame.Rect((0, 528), (665, 10)),
    'retangulo4': pygame.Rect((52, 650), (665, 10)),
    'retangulo5': pygame.Rect((0, 773), (665, 10)),
    'retangulo6': pygame.Rect((0, 895), (720, 10)),
    'retangulo7': pygame.Rect((282, 209), (153, 5)),
    }

    # Escadas do jogo
    escadas = {
    'escada1': pygame.Rect((414, 214), (15, 110)),
    'escada3': pygame.Rect((628, 319), (15, 100)),
    'escada4': pygame.Rect((76, 412), (15, 83)),
    'escada5': pygame.Rect((600, 530), (15, 83)),
    'escada6': pygame.Rect((104, 655), (15, 83)),
    'escada7': pygame.Rect((559, 775), (15, 80))
    }

    # Bolas de fogo
    for i in range(1, 5):
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

def re_inicializa():

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

    state['estado_tela'] = 0

    state['restart'] = False

    state['princesa'] = STILL


    # Carrega os assets do jogo
    assets = {}

    assets['background'] = pygame.transform.scale(pygame.image.load('assets/img/background.png').convert_alpha(), DIMENSOES)

    assets['ponte'] = pygame.transform.scale(pygame.image.load('assets/img/bridge.png'), (90, 50))
    
    assets['coracao'] = pygame.transform.scale(pygame.image.load('assets/images/heart.png'), (30, 30))

    assets['princesa1'] = pygame.transform.scale(pygame.image.load('assets/images/peach/peach1.png'), (60, 60))

    assets['princesa2'] = pygame.transform.scale(pygame.image.load('assets/images/peach/peach2.png'), (60, 60))

    assets['pos_princesa'] = (282, 150)

    assets['fire_ball'] = pygame.transform.scale(pygame.image.load('assets/images/fireball.png'), (30, 30))

    assets['welcome'] = pygame.transform.scale(pygame.image.load('assets/images/welcome.png').convert_alpha(), DIMENSOES)

    assets['win'] = pygame.transform.scale(pygame.image.load('assets/images/win_screen.png').convert_alpha(), DIMENSOES)

    assets['game_over'] = pygame.transform.scale(pygame.image.load('assets/images/game_over.png').convert_alpha(), DIMENSOES)

    assets['dormes'] = pygame.transform.scale(pygame.image.load('assets/images/dormes.png').convert_alpha(), DIMENSOES)

    assets['barril'] = pygame.transform.scale(pygame.image.load('assets/images/barril.png').convert_alpha(), (70, 100))
    
    assets['fogo'] = pygame.transform.scale(pygame.image.load('assets/images/fire.png').convert_alpha(), (100, 50))

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
    state['jogador'] = Jogador(mario, state['grupos'], state['pos_mario'][0], state['pos_mario'][1], state['vidas'], state['estado_tela'])
    state['clock'] =  pygame.time.Clock()

    # Plataformas do jogo
    retangulos = {
    'retangulo1': pygame.Rect((0, 312), (665, 10)),
    'retangulo2': pygame.Rect((52, 405), (665, 10)),
    'retangulo3': pygame.Rect((0, 528), (665, 10)),
    'retangulo4': pygame.Rect((52, 650), (665, 10)),
    'retangulo5': pygame.Rect((0, 773), (665, 10)),
    'retangulo6': pygame.Rect((0, 895), (720, 10)),
    'retangulo7': pygame.Rect((282, 209), (153, 5)),
    }

    # Escadas do jogo
    escadas = {
    'escada1': pygame.Rect((414, 214), (15, 110)),
    'escada3': pygame.Rect((628, 319), (15, 100)),
    'escada4': pygame.Rect((76, 412), (15, 83)),
    'escada5': pygame.Rect((600, 530), (15, 83)),
    'escada6': pygame.Rect((104, 655), (15, 83)),
    'escada7': pygame.Rect((559, 775), (15, 80))
    }

    # Bolas de fogo
    for i in range(1, 5):
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

    return assets, state, retangulos, escadas, mario



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

            if event.key == pygame.K_q :
                return False

            if event.key == pygame.K_p:
                state['estado_tela'] = 1

            if (event.key == pygame.K_r and state['jogador'].vidas == 0) or (event.key == pygame.K_r and state['estado_tela'] == 3):
                state['restart'] = True
                return False

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

    if state['jogador'].vidas == 0:
        state['estado_tela'] = 2

    print(state['jogador'].rect.y)
    
    if state['jogador'].rect.y <= 151:
            state['princesa'] == HAPPY
            if state['jogador'].rect.x < 347:
                state['estado_tela'] = 3
    
    if state['jogador'].rect.y > 835:
        state['estado_tela'] = 4
    
    return True


def desenha(window, assets, state, retangulos, escadas, mario ):
    
    # Tela de apresentação
    window.blit(assets['welcome'], (0, 0))

    # Tela principal do jogo
    if state['estado_tela'] == 1:
        # Desenha as escadas
        for escada in escadas.values():
            pygame.draw.rect(window, 'blue', escada)

        for plataforma in retangulos.values():
            pygame.draw.rect(window, 'blue', plataforma)

        # Desenha o background
        window.blit(assets['background'], (0, 0))

        
        # Desenha os corações
        for i in range(0, 30 * state['jogador'].vidas, 30):
            window.blit(assets['coracao'], (i, 20))

        window.blit(assets['barril'], (0, 212))

        for i in range(0, 270, 30):
            window.blit(assets['fogo'], (70 + i, 265))

        # Desenha todas as sprites
        state['grupos']['all_sprites'].draw(window)  

        # Desenha a princesa
        if state['princesa'] == STILL:
            window.blit(assets['princesa1'], assets['pos_princesa'])
        elif state['princesa'] == HAPPY:
            window.blit(assets['princesa2'], assets['pos_princesa'])
        

    # Tela de Game Over
    if state['estado_tela'] == 2:
        window.blit(assets['game_over'], (0, 0))

    # Tela de vitória
    if state['estado_tela'] == 3:
        window.blit(assets['win'], (0, 0))

    if state['estado_tela'] == 4:
        window.blit(assets['dormes'], (0, 0))


    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state, retangulos, escadas, mario):
    
    while recebe_eventos(state, window, mario, assets, retangulos, escadas):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        state['clock'].tick(60)
        desenha(window, assets, state, retangulos, escadas, mario)

if __name__ == '__main__':
    
    jogando = True
    w, assets, state, retangulos, escadas, mario = inicializa()  # Inicializa o Pygame e carrega os recursos necessários

    while jogando:
        game_loop(w, assets, state, retangulos, escadas, mario)  # Inicia o loop principal do jogo
        jogando = state['restart']
        assets, state, retangulos, escadas, mario = re_inicializa()
