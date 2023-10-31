import pygame
from random import randint

dimensoes = (720, 950)  # Define as dimensões da janela do jogo
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
    


    assets['gorila'] = pygame.image.load('assets/images/dk/dk2.png')
    assets['gorila'] = pygame.transform.scale(assets['gorila'],(100,100))

    assets['barril1'] = pygame.image.load('assets/images/barrels/barrel.png')
    assets['barril1'] = pygame.transform.scale(assets['barril1'],(30,30))

    mario = {
        'climbing1': pygame.transform.scale(pygame.image.load('assets/images/mario/climbing1.png'),(60,60)),
        'climbing2': pygame.transform.scale(pygame.image.load('assets/images/mario/climbing2.png'),(60,60)),
        'hammer_jump': pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_jump.png'),(60,60)),
        'hammer_overhead': pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_overhead.png'),(60,60)),
        'hammer_stand': pygame.transform.scale(pygame.image.load('assets/images/mario/hammer_stand.png'),(60,60)),
        'jumping': pygame.transform.scale(pygame.image.load('assets/images/mario/jumping.png'),(60,60)),
        'running': pygame.transform.scale(pygame.image.load('assets/images/mario/running.png'),(60,60)),
        'standing': pygame.transform.scale(pygame.image.load('assets/images/mario/standing.png'),(60,60))
    }
    mario['running_reverse'] = pygame.transform.flip(mario['running'], True, False)

    
    barril = {
        'pos_barril' : [100,295],
        'vel_barril': [0,0],
        'barril_rect': assets['barril1'].get_rect()
    }

    # for player in mario:
    #     state['rect_mario'] = player.get_rect()
    
    # # assets['new_back'].set_colorkey((255,27,84))

    # # Defina a cor da plataforma (R, G, B)
    # platform_color = (255,27,84)  # Azul, por exemplo

    # # Crie uma máscara vazia do mesmo tamanho que a imagem
    # assets['mask'] = pygame.mask.Mask((assets['background'].get_width(), assets['background'].get_height()))

    # # Percorra cada pixel na imagem
    # for x in range(assets['background'].get_width()):
    #     for y in range(assets['background'].get_height()):
    #         # Verifique se a cor do pixel corresponde à cor da plataforma
    #         if assets['background'].get_at((x, y))[:3] == platform_color:
    #             # Se corresponder, adicione este pixel à máscara
    #             assets['mask'].set_at((x, y), 1)

    # assets['new_back'] = assets['mask'].to_surface()




    retangulos = {
    'retangulo': pygame.Rect((0, 312), (665, 29)),
    'retangulo1': pygame.Rect((52, 405), (665, 29)),
    'retangulo2': pygame.Rect((0, 528), (665, 29)),
    'retangulo3': pygame.Rect((52, 650), (665, 29)),
    'retangulo4': pygame.Rect((0, 777), (665, 20)),
    'retangulo5': pygame.Rect((0, 895), (720, 29)),
    'retangulo6': pygame.Rect((282, 211), (153, 28))

    }

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
    state['g'] = 9.80665



    return window, assets, state, retangulos, escadas, mario, barril

def colisao_plataforma(state, window, assets, mario, retangulos):
    for plataforma in retangulos.values():
        if (state['pos_mario'][1] < plataforma.y):
            print('cond1')
            if (
                (plataforma.y - 8 <= state['pos_mario'][1] + 60)  and 
                (state['pos_mario'][1] + 60 <= plataforma.y + 8)
            ):
                print('cond2')
                print('colisao')
                return True
    return False
    
def colisao_escada(state, window, assets, mario, escadas):
    for escada in escadas.values():
    #    if (state['pos_mario'][0] >= escada.x and
    #        state['pos_mario'][0] <= escada.x + escada.width
    #        ):
    #         print('cond1 escada')
    #         if (
    #             (state['pos_mario'][1] > escada.y and state['pos_mario'][1] - escada.y < 100) or 
    #             (state['pos_mario'][1] > escada.y and state['pos_mario'][1] - escada.y < 100 and state['pos_mario'][1] + 60 == escada.y - escada.height) 
    #         ):
    #             print('cond2 escada')
    #             return True

        col_esc = pygame.Rect.colliderect(state['rect_mario'], escada)
        if col_esc:
            print('colisao escada')
            return True
    return False

def mov_barril(window, assets, barril, retangulos):
    
    barril['vel_barril'][0] = 90
    print(barril['vel_barril'][0])
    return barril['vel_barril'][0]
        
    
# Recebe eventos do Pygame
def recebe_eventos(state, window, mario, barril):

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

    # Atualiza a posição do barril
    pos_x_barril = barril['pos_barril'][0]
    pos_y_barril = barril['pos_barril'][1]
    v_x_barril = barril['vel_barril'][0]
    # print(v_x_barril)
    v_y_barril = barril['vel_barril'][1]
    prox_pos_x_bar = pos_x_barril + (v_x_barril * dt)
    prox_pos_y_bar = pos_y_barril + (v_y_barril * dt)
    barril['pos_barril'][0] = prox_pos_x_bar
    barril['pos_barril'][1] = prox_pos_y_bar



    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o evento QUIT foi acionado, retorna False
            return False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if colisao_plataforma(state, window, assets, mario, retangulos):
                    state['mario'] = mario['running_reverse']
                    state['vel_mario'][0] -= 145                    
            elif event.key == pygame.K_RIGHT:
                
                mov_barril(window, assets, barril, retangulos)
                if colisao_plataforma(state, window, assets, mario, retangulos):
                    state['mario'] = mario['running']
                    state['vel_mario'][0] += 145

        
            if event.key == pygame.K_UP:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['mario'] = mario['climbing1']
                    state['vel_mario'][1] -= 145  
            if event.key == pygame.K_DOWN:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['mario'] = mario['climbing1']
                    state['vel_mario'][1] += 90 

            if event.key == pygame.K_SPACE:
                state['vel_mario'][1] += 90
                    # if retangulos['retangulo5'].y > escadas['escada7'].y + escadas['escada7'].height:
                    #     state['vel_mario'][1] = 0
                    # for plataforma in retangulos.values():
                    #     for escada in escadas.values():
                    #         if colisao_plataforma(state, window, assets, mario, retangulos):
                    #             if plataforma.y > escada.y + escada.height:
                    #     # for plataforma in retangulos:
                    #     #     if 
                    #                 state['vel_mario'][1] = 0
                    
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
                    state['vel_mario'][1] += 145  
            if event.key == pygame.K_DOWN:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['vel_mario'][1] -= 90 

    if not colisao_escada(state, window, assets, mario, escadas):
        state['vel_mario'][1] = 0

    if state['pos_mario'][0] < 0:
        state['pos_mario'][0] = 0
    elif state['pos_mario'][0] > 650:
        state['pos_mario'][0] = 650

    if state['pos_mario'][1] < 0:
        state['pos_mario'][1] = 0
    elif state['pos_mario'][1] > 880:
        state['pos_mario'][1] = 880

    state['rect_mario'].x,state['rect_mario'].y = state['pos_mario']



    return True



def desenha(window, assets, state, retangulos, escadas, mario, barril):
    
    # Desenha as plataformas
    for retangulo in retangulos.values():
        pygame.draw.rect(window, 'red', retangulo)

    # Desenha as escadas
    for escada in escadas.values():
        pygame.draw.rect(window, 'blue', escada)

    # Desenha o background
    window.blit(assets['background'], (0, 0))

    # Desenha o barril
    # print(barril['pos_barril'])
    window.blit(assets['barril1'], barril['pos_barril'])

    window.blit(assets['gorila'],(0,215))   # Desenha o gorila
    window.blit(state['mario'],state['pos_mario'])  # Desenha o jogador

    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state, retangulos, escadas, mario, barril):
    
    while recebe_eventos(state, window, mario, barril):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        desenha(window, assets, state, retangulos, escadas, mario, barril)

if __name__ == '__main__':
    
    w, assets, state, retangulos, escadas, mario, barril = inicializa()  # Inicializa o Pygame e carrega os recursos necessários
    game_loop(w, assets, state, retangulos, escadas, mario, barril)  # Inicia o loop principal do jogo
