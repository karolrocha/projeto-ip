import pygame
import sys

pygame.init()

# configurações da janela
largura, altura = 800, 600
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tela de Game Over")
cor_fundo = (0, 0, 0)
cor_texto = (255, 255, 255)
fonte = pygame.font.Font(None, 36)

def mostrar_game_over():
    texto_game_over = fonte.render("Game Over", True, cor_texto)
    texto_instrucao = fonte.render("Pressione ESC para sair", True, cor_texto)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        janela.fill(cor_fundo)
        janela.blit(texto_game_over, (largura // 2 - texto_game_over.get_width() // 2, altura // 2 - texto_game_over.get_height() // 2))
        janela.blit(texto_instrucao, (largura // 2 - texto_instrucao.get_width() // 2, altura // 2 + 50))

        pygame.display.flip()

if __name__ == "__main__":
    mostrar_game_over()
