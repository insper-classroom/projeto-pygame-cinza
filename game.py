import pygame
from random import randint

dimensoes = (1680, 1050)  # Define as dimensões da janela do jogo

# Inicializa o Pygame e carrega os recursos necessários
def inicializa():
    pygame.init()  # Inicializa o Pygame
    
    # Cria a janela do jogo e preenche com preto
    window = pygame.display.set_mode(dimensoes, vsync=True, flags=pygame.SCALED)
    window.fill((0, 0, 0))
    pygame.display.set_caption('First game')  # Define o título da janela

    # Carrega as imagens do campo de estrelas e da nave espacial
    assets = {}
    assets['starfield'] = pygame.image.load('assets/img/starfield.png')
    assets['starfield'] = pygame.transform.scale(assets['starfield'], dimensoes)
    assets['ponte'] = pygame.image.load('assets/img/bridge.png') 
    assets['ponte'] = pygame.transform.scale(assets['ponte'], (90, 50))



    # Inicializa o estado do jogo
    state = {
        't0': -1,   # Tempo inicial
    }



    return window, assets, state
    
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



def desenha(window, assets, state):
    
    window.blit(assets['starfield'], (0, 0))
    window.blit(assets['ponte'], (0, 0))
    
    pygame.display.update()  # Atualiza a tela

# Loop principal do jogo
def game_loop(window, assets, state):
    
    while recebe_eventos(state, window):  # Continua recebendo eventos e desenhando na tela até que o usuário feche a janela do jogo
        desenha(window, assets, state)

if __name__ == '__main__':
    
    w, assets, state = inicializa()  # Inicializa o Pygame e carrega os recursos necessários
    game_loop(w, assets, state)  # Inicia o loop principal do jogo
