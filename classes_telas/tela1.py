import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definições de tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu Inicial")

# Cores
cor_fundo = (0, 0, 0)
cor_texto = (255, 255, 255)

# Fonte do texto
fonte = pygame.font.Font(None, 36)

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
                        jogo()
                    elif selecionado == 1:
                        configuracoes()
                    elif selecionado == 2:
                        pygame.quit()
                        sys.exit()
                elif event.key == pygame.K_UP:
                    selecionado = (selecionado - 1) % len(opcoes)
                elif event.key == pygame.K_DOWN:
                    selecionado = (selecionado + 1) % len(opcoes)
        
        # Preencher a tela de fundo
        tela.fill(cor_fundo)
        
        # Criar texto para o menu
        for i, opcao in enumerate(opcoes):
            cor = cor_texto if i == selecionado else (100, 100, 100)
            texto = fonte.render(opcao, True, cor)
            texto_rect = texto.get_rect()
            texto_rect.center = (largura // 2, altura // 2 + i * 50)
            
            # Desenhar o texto na tela
            tela.blit(texto, texto_rect)
        
        # Atualizar a tela
        pygame.display.update()

def jogo():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 

def configuracoes():
    pass

if __name__ == "__main__":
    menu()
