import pygame
from random import randint

dimensoes = (720, 950)  # Define as dimensões da janela do jogo

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
    'escada': pygame.Rect((203, 120), (28, 193)),
    'escada1': pygame.Rect((254, 120), (28, 193)),
    'escada2': pygame.Rect((410, 237), (28, 75)),
    'escada3': pygame.Rect((623, 341), (28, 65)),
    'escada4': pygame.Rect((71, 435), (28, 95)),
    'escada5': pygame.Rect((595, 555), (28, 95)),
    'escada6': pygame.Rect((99, 678), (28, 95)),
    'escada7': pygame.Rect((554, 802), (28, 95))
    }

    # Inicializa o estado do jogo
    state = {
        't0': -1,   # Tempo inicial
    }



    return window, assets, state, retangulos, escadas
    
# Recebe eventos do Pygame
def recebe_eventos(state, window):

    # Calculo do fps
    t1 = pygame.time.get_ticks()
    t0 = state['t0']
    dt = (t1 - t0) / 1000
    fps = 1 / dt  # Calcula a taxa de quadros por segundo (FPS)
    state['t0'] = t1
    state['fps'] = fps




    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se o evento QUIT foi acionado, retorna False
            return False



    return True



def desenha(window, assets, state, retangulos, escadas):
    

    for retangulo in retangulos.values():
        pygame.draw.rect(window, 'red', retangulo)
    
    # window.blit(assets['new_back'], (0, 0))
    # # window.blit(assets['ponte'], (0, 0))

    for escada in escadas.values():
        pygame.draw.rect(window, 'blue', escada)

    window.blit(assets['background'], (0, 0))
    window.blit(assets['gorila'],(0,215))

    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state, retangulos, escadas):
    
    while recebe_eventos(state, window):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        desenha(window, assets, state, retangulos, escadas)

if __name__ == '__main__':
    
    w, assets, state, retangulos, escadas = inicializa()  # Inicializa o Pygame e carrega os recursos necessários
    game_loop(w, assets, state, retangulos, escadas)  # Inicia o loop principal do jogo
