import pygame
from random import randint
from time import sleep

dimensoes = (720, 950)  # Define as dimensões da janela do jogo
STILL = 0
JUMPING = 1
FALLING = 2
CLIMBING = 3
RUN = False
# Inicializa o Pygame e carrega os recursos necessários
def inicializa():
    pygame.init()  # Inicializa o Pygame
    
    # Cria a janela do jogo e preenche com preto
    window = pygame.display.set_mode(dimensoes, vsync=True, flags=pygame.SCALED)
    window.fill((0, 0, 0))
    pygame.display.set_caption('First game')  # Define o título da janela

    # Carrega as imagens do campo de estrelas e da nave espacial
    assets = {}
    assets['background'] = pygame.image.load('assets/img/background.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], dimensoes)

    assets['ponte'] = pygame.image.load('assets/img/bridge.png') 
    assets['ponte'] = pygame.transform.scale(assets['ponte'], (90, 50))

    assets['coracao'] = pygame.image.load('assets/images/heart_5.png')
    assets['coracao'] = pygame.transform.scale(assets['coracao'], (20, 20))

    assets['gorila'] = pygame.image.load('assets/images/dk/dk2.png')
    assets['gorila'] = pygame.transform.scale(assets['gorila'],(100,100))

    assets['fire_ball'] = pygame.image.load('assets/images/Fire-Ball.gif')
    assets['fire_ball'] = pygame.transform.scale(assets['fire_ball'],(30,30))

    mario = {
        'climbing1': pygame.transform.scale(pygame.image.load('assets/images/mario/climbing1.png'),(60,60)),
        'climbing2': pygame.transform.scale(pygame.image.load('assets/images/mario/climbing2.png'),(60,60)),
        'jumping': pygame.transform.scale(pygame.image.load('assets/images/mario/jumping.png'),(60,60)),
        'running': pygame.transform.scale(pygame.image.load('assets/images/mario/running.png'),(60,60)),
        'standing': pygame.transform.scale(pygame.image.load('assets/images/mario/standing.png'),(60,60)),
    }
    mario['running_reverse'] = pygame.transform.flip(mario['running'], True, False)

    retangulos = {
    'retangulo': pygame.Rect((0, 312), (665, 29)),
    'retangulo1': pygame.Rect((52, 405), (665, 29)),
    'retangulo2': pygame.Rect((0, 528), (665, 29)),
    'retangulo3': pygame.Rect((52, 650), (665, 29)),
    'retangulo4': pygame.Rect((0, 777), (665, 20)),
    'retangulo5': pygame.Rect((0, 895), (720, 29)),
    'retangulo6': pygame.Rect((282, 211), (153, 28)),
    }

    fire_ball = []
    for i in range(6):
        fire_ball.append({
        'pos_fire_ball': [list(retangulos.values())[i].x, list(retangulos.values())[i].y - list(retangulos.values())[i].height],
        'vel_fire_ball': [180 if i % 2 == 0 else -180,0],
        'fire_ball_rect': assets['fire_ball'].get_rect(),
        'cont': 0
        })

    escadas = {
    # 'escada': pygame.Rect((203, 120), (28, 203)),
    # 'escada1': pygame.Rect((254, 120), (28, 203)),
    'escada2': pygame.Rect((410, 214), (28, 110)),
    'escada3': pygame.Rect((623, 319), (28, 100)),
    'escada4': pygame.Rect((71, 412), (28, 83)),
    'escada5': pygame.Rect((595, 530), (28, 83)),
    'escada6': pygame.Rect((99, 655), (28, 83)),
    # 'escada7': pygame.Rect((554, 772), (28, 73))
    'escada7': pygame.Rect((554, 775), (38, 80))

    }

    # Inicializa o estado do jogo
    state = {
        't0': -1,   # Tempo inicial
    }
    state['mario'] = mario['standing']
    state['rect_mario'] = state['mario'].get_rect()
    state['pos_mario'] = [0, 840]
    state['vel_mario'] = [0, 0]
    state['g'] = 2
    state['estado'] = STILL
    state['fire_ball'] = fire_ball
    state['vidas'] = 90


    return window, assets, state, retangulos, escadas, mario

def colisao_plataforma(state, window, assets, mario, retangulos):
    for plataforma in retangulos.values():
        if (state['pos_mario'][1] < plataforma.y):
            # print('cond1')
            if (
                (plataforma.y - 8 <= state['pos_mario'][1] + 60)  and 
                (state['pos_mario'][1] + 60 <= plataforma.y + 8)
            ):
                # print('cond2')
                # print('colisao')
                return True
    return False
    
def colisao_escada(state, window, assets, mario, escadas):
    for escada in escadas.values():
        retangulo = pygame.Rect((state['pos_mario'][0],state['pos_mario'][1]),(60,60))
        col_esc = pygame.Rect.colliderect(retangulo, escada)
        if col_esc:
            return True
    return False

def mov_fire_ball(window, assets, fire_ball, retangulos):
    col = fire_ball['fire_ball_rect'].collidelist(list(retangulos.values()))
    if col != -1:
        fire_ball['cont'] = 0
    elif fire_ball['cont'] == 0:
        fire_ball['cont'] += 1
        fire_ball['vel_fire_ball'][0] *= -1

def coli_jog_fog(window, assets, fire_ball):
    col = pygame.Rect.colliderect(state['rect_mario'], fire_ball['fire_ball_rect'])
    if col:
        print('bateu')
        state['vidas'] -= 30

# def pulo(window, assets, retangulos, escadas):
#     col_plat = colisao_plataforma(state, window, assets, mario, retangulos)
#     col_esc = colisao_escada(state, window, assets, mario, escadas)
#     if col_plat:
#         if not col_esc:
#             state['vel_']
# Recebe eventos do Pygame
def recebe_eventos(state, window, mario ):

    for fire_ball in state['fire_ball']:
        fire_ball['fire_ball_rect'].x, fire_ball['fire_ball_rect'].y = fire_ball['pos_fire_ball']

    # state['pos_mario'][0] += state['velocidade_mario'][0]
    # state['pos_mario'][1] += state['velocidade_mario'][1]

    # Calculo do fps
    t1 = pygame.time.get_ticks()
    t0 = state['t0']
    dt = (t1 - t0) / 1000
    fps = 1 / dt  # Calcula a taxa de quadros por segundo (FPS)
    state['t0'] = t1
    state['fps'] = fps
    state['t2'] = 0

    # Atualiza a posição da jogador baseada na velocidade
    posicao_x = state['pos_mario'][0]
    posicao_y = state['pos_mario'][1]
    v_x = state['vel_mario'][0]
    v_y = state['vel_mario'][1]
    g = state['g'] 
    prox_posicao_x = posicao_x + (v_x * dt)
    prox_posicao_y = posicao_y + (v_y * dt) + ((g / 2) * (dt ** 2))
    state['pos_mario'][0] = prox_posicao_x
    state['pos_mario'][1] = prox_posicao_y

    for fire_ball in state['fire_ball']:
        # Atualiza a posição do fire_ball
        pos_x_fire_ball = fire_ball['pos_fire_ball'][0]
        pos_y_fire_ball = fire_ball['pos_fire_ball'][1]
        v_x_fire_ball = fire_ball['vel_fire_ball'][0]
        # print(v_x_fire_ball)
        v_y_fire_ball = fire_ball['vel_fire_ball'][1]
        prox_pos_x_fire_ball = pos_x_fire_ball + (v_x_fire_ball * dt)
        prox_pos_y_fire_ball = pos_y_fire_ball + (v_y_fire_ball * dt)
        fire_ball['pos_fire_ball'][0] = prox_pos_x_fire_ball
        fire_ball['pos_fire_ball'][1] = prox_pos_y_fire_ball


        mov_fire_ball(window, assets, fire_ball, retangulos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o evento QUIT foi acionado, retorna False
            return False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if colisao_plataforma(state, window, assets, mario, retangulos):
                    state['mario'] = mario['running_reverse']
                    state['estado'] = 'RUNNING'
                    state['vel_mario'][0] -= 145                    
            elif event.key == pygame.K_RIGHT:
                
                if colisao_plataforma(state, window, assets, mario, retangulos):
                    state['mario'] = mario['running']
                    state['vel_mario'][0] += 145

        
            if event.key == pygame.K_UP:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['mario'] = mario['climbing1']
                    state['estado'] = CLIMBING
                    state['vel_mario'][1] -= 80
                    state['vel_mario'][0] = 0
            if event.key == pygame.K_DOWN:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['mario'] = mario['climbing1']
                    state['estado'] = CLIMBING
                    state['vel_mario'][1] += 80
                    state['vel_mario'][0] = 0
            if event.key == pygame.K_SPACE:
                if state['estado'] == STILL:
                    if not colisao_escada(state, window, assets, mario, escadas):
                        # state['pos_mario'][1] -= 45
                        # print('entra')
                        state['estado'] = JUMPING
                        state['vel_mario'][1] -= 80
                        if state['estado'] == JUMPING:
                            state['vel_mario'][1] += 80
                        # sleep(1)
                        # state['vel_mario'][1] += 50
                        # state['mario'] = mario['standing']
                    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                if colisao_plataforma(state, window, assets, mario, retangulos):
                    state['mario'] = mario['standing']
                    state['vel_mario'][0] += 145
            elif event.key == pygame.K_RIGHT:
                if colisao_plataforma(state, window, assets, mario, retangulos):
                    state['mario'] = mario['standing']
                    state['vel_mario'][0] -= 145

            if event.key == pygame.K_UP:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['vel_mario'][1] += 80 
            if event.key == pygame.K_DOWN:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['vel_mario'][1] -= 80

     # Atualiza a posição da jogador baseada na velocidade
    posicao_x = state['pos_mario'][0]
    posicao_y = state['pos_mario'][1]
    
    if not colisao_escada(state, window, assets, mario, escadas):
        state['vel_mario'][1] += state['g']

    if state['vel_mario'][1] > 0:
        state['estado'] = FALLING

    if colisao_plataforma(state, window, assets, mario, retangulos) and state['estado'] == FALLING and not colisao_escada(state, window, assets, mario, escadas):
        state['vel_mario'][1] = 0
        state['estado'] = STILL
    
    v_x = state['vel_mario'][0]
    v_y = state['vel_mario'][1]
    # g = state['g'] 
    # prox_posicao_x = posicao_x + (v_x * dt)
    # prox_posicao_y = posicao_y + (v_y * dt) + ((g / 2) * (dt ** 2))
    prox_posicao_x = posicao_x + (v_x * dt)
    prox_posicao_y = posicao_y + (v_y*dt)
    
    state['pos_mario'][0] = prox_posicao_x
    state['pos_mario'][1] = prox_posicao_y

    # if state['vel_mario'][1] > 0:
    #     state['estado'] = FALLING

    # if state['pos_mario'][1]+60 >= 895:
    #     state['pos_mario'][1] = 895 - 60
    #     state['vel_mario'][1] = 0
    #     state['estado'] = STILL
    # if v_y != 2:
    #     print(posicao_x,v_y)
    # if state['estado'] == JUMPING:
    #     state['vel_mario'][1] += state['g']  # Aplicar a aceleração devido à gravidade
    #     if state['pos_mario'][1] >= 840:  # Ajuste a altura do chão conforme necessário
    #         state['pos_mario'][1] = 840
    #         state['estado'] = STILL 

    # if not colisao_escada(state, window, assets, mario, escadas):
    #     state['vel_mario'][1] = m pro

    if state['pos_mario'][0] < 0:
        state['pos_mario'][0] = 0
    elif state['pos_mario'][0] > 650:
        state['pos_mario'][0] = 650

    if state['pos_mario'][1] < 0:
        state['pos_mario'][1] = 0
    elif state['pos_mario'][1] > 880:
        state['pos_mario'][1] = 880

    # state['rect_mario'].x,state['rect_mario'].y = state['pos_mario']



    return True



def desenha(window, assets, state, retangulos, escadas, mario ):
    
    # Desenha as plataformas
    for retangulo in retangulos.values():
        pygame.draw.rect(window, 'red', retangulo)

    # Desenha as escadas
    for escada in escadas.values():
        pygame.draw.rect(window, 'blue', escada)

    # Desenha o background
    window.blit(assets['background'], (0, 0))

    # Desenha as vidas
    vidas = state['vidas']
    print(vidas)
    for i in range(0, vidas, 30):
        window.blit(assets['coracao'], (i + 25, 35))

    # Desenha o fire_ball
    for fire_ball in state['fire_ball']:
        window.blit(assets['fire_ball'], fire_ball['pos_fire_ball'])

    # window.blit(assets['gorila'],(0,215))   # Desenha o gorila
    window.blit(state['mario'],state['pos_mario'])  # Desenha o jogador

    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state, retangulos, escadas, mario):
    
    while recebe_eventos(state, window, mario):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        desenha(window, assets, state, retangulos, escadas, mario)

if __name__ == '__main__':
    
    w, assets, state, retangulos, escadas, mario = inicializa()  # Inicializa o Pygame e carrega os recursos necessários
    game_loop(w, assets, state, retangulos, escadas, mario)  # Inicia o loop principal do jogo
