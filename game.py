import pygame
from random import randint

dimensoes = (720, 950)  # Define as dimensões da janela do jogo
STILL = 0
JUMPING = 1
FALLING = 2
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
    'retangulo4': pygame.Rect((0, 774), (665, 29)),
    'retangulo5': pygame.Rect((0, 895), (720, 29)),
    'retangulo6': pygame.Rect((282, 210), (153, 28))

    }

    escadas = {
    'escada': pygame.Rect((203, 120), (28, 203)),
    'escada1': pygame.Rect((254, 120), (28, 203)),
    'escada2': pygame.Rect((410, 214), (28, 110)),
    'escada3': pygame.Rect((623, 319), (28, 100)),
    'escada4': pygame.Rect((71, 412), (28, 125)),
    'escada5': pygame.Rect((595, 535), (28, 125)),
    'escada6': pygame.Rect((99, 658), (28, 125)),
    'escada7': pygame.Rect((554, 781), (28, 125))
    }

    # Inicializa o estado do jogo
    state = {
        't0': -1,   # Tempo inicial
    }
    state['rect_mario'] = mario['standing'].get_rect()
    state['pos_mario'] = [0, 840]
    state['vel_mario'] = [0, 0]
    state['g'] = 2
    state['mario'] = mario['standing']
    state['estado'] = STILL
    



    return window, assets, state, retangulos, escadas, mario

def colisao_plataforma(state, window, assets, mario, retangulos):
    for plataforma in retangulos.values():
        if (state['pos_mario'][1] < plataforma.y        ):
            print('cond1')
            if plataforma.y - 5 <= state['pos_mario'][1] + 60 <= plataforma.y + 10:
                print('cond2')
                print('colisao')
                return True
    return False
    
def colisao_escada(state, window, assets, mario, escadas):
    for escada in escadas.values():
        retangulo = pygame.Rect((state['pos_mario'][0],state['pos_mario'][1]),(60,60))
        col_esc = pygame.Rect.colliderect(retangulo, escada)
        if col_esc:
            print('colisao escada')
            return True
    return False
        
    
# Recebe eventos do Pygame
def recebe_eventos(state, window, mario):

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
                    state['estado'] = 'CLIMBING'
                    state['vel_mario'][1] -= 145  
            if event.key == pygame.K_DOWN:  
                if colisao_escada(state, window, assets, mario, escadas):
                    state['mario'] = mario['climbing1']
                    state['estado'] = 'CLIMBING'
                    state['vel_mario'][1] += 145 
            if event.key == pygame.K_SPACE:
                if state['estado'] == STILL:
                    if not colisao_escada(state, window, assets, mario, escadas):
                        # state['pos_mario'][1] -= 45
                        # print('entra')
                        # state['estado'] = JUMPING
                        state['vel_mario'][1] -= 100
                
                    
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
                if colisao_escada(state, window, assets, mario, escadas):
                    if event.key == pygame.K_DOWN:  
                        state['vel_mario'][1] -= 145 


     # Atualiza a posição da jogador baseada na velocidade
    posicao_x = state['pos_mario'][0]
    posicao_y = state['pos_mario'][1]
    if not colisao_escada(state, window, assets, mario, escadas):
        print('aqui')
        state['vel_mario'][1] += state['g']
    
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

    if state['pos_mario'][1]+60 >= 895:
        state['pos_mario'][1] = 895 - 60
        state['vel_mario'][1] = 0
        state['estado'] = STILL
    # if v_y != 2:
    #     print(posicao_x,v_y)
    # if state['estado'] == JUMPING:
    #     state['vel_mario'][1] += state['g']  # Aplicar a aceleração devido à gravidade
    #     if state['pos_mario'][1] >= 840:  # Ajuste a altura do chão conforme necessário
    #         state['pos_mario'][1] = 840
    #         state['estado'] = STILL 

    # if not colisao_escada(state, window, assets, mario, escadas):
    #     state['vel_mario'][1] = 0

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



def desenha(window, assets, state, retangulos, escadas, mario):
    window.blit(assets['background'], (0, 0))
    
    # Desenha as plataformas
    for retangulo in retangulos.values():
        pygame.draw.rect(window, 'red', retangulo)

    # Desenha as escadas
    for escada in escadas.values():
        pygame.draw.rect(window, 'blue', escada)

    # Desenha o background

    window.blit(assets['gorila'],(0,215))
    window.blit(state['mario'],state['pos_mario'])

    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state, retangulos, escadas, mario):
    
    while recebe_eventos(state, window, mario):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        desenha(window, assets, state, retangulos, escadas, mario)

if __name__ == '__main__':
    
    w, assets, state, retangulos, escadas, mario = inicializa()  # Inicializa o Pygame e carrega os recursos necessários
    game_loop(w, assets, state, retangulos, escadas, mario)  # Inicia o loop principal do jogo
