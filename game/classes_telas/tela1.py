import pygame
from funcs import *
from classes_telas.tela_jogo import *

# Inicialização do Pygame
pygame.init()

# Definições de tela
tela = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Menu Inicial")

# Cores
COR_FUNDO = (0, 0, 0)
COR_TEXTO = (255, 255, 255)

# Fonte do texto
FONTE = pygame.font.Font(None, 36)

def menu():
    opcoes = ["Iniciar", "Configurações", "Sair"]
    selecionado = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selecionado == 0:
                        pass
                        # jogo.run()
                    elif selecionado == 1:
                        pass
                        # configuracoes()
                    elif selecionado == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif event.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
        # Preencher a tela de fundo
        tela.fill(COR_FUNDO)
        
        # Criar texto para o menu
        for i, opcao in enumerate(opcoes):
            cor = COR_TEXTO if i == selecionado else (100, 100, 100)
            texto = FONTE.render(opcao, True, cor)
            texto_rect = texto.get_rect()
            texto_rect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + i * 50)
            
            # Desenhar o texto na tela
            tela.blit(texto, texto_rect)
        
        # Atualizar a tela
        pygame.display.update()

# def jogo():
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return 

# def configuracoes():
#     pass

# if __name__ == "__main__":
#     menu()
