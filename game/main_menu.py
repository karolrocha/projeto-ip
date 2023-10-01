from funcs import *
from classes_telas.tela_jogo import * 

pg.init()

# Configuração da tela
fullscreen = False  

screen = pg.display.set_mode(DISPLAY_RESOLUTION)
background_img = pg.transform.scale(
    pg.image.load('images/background_castle_(resize).jpg'),
    DISPLAY_RESOLUTION
)
pg.display.set_caption('Menu')
gamescreen = Level(screen, background_img)

opcoes = ["Iniciar", "Configurações", "Sair"]
selecionado = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if selecionado == 0:
                    try:
                        gamescreen.run()
                    finally:
                        pass
                elif selecionado == 1:
                    pass
                elif selecionado == 2:
                    pg.quit()
                    sys.exit()
            elif event.key == pg.K_UP:
                selecionado = (selecionado - 1) % len(opcoes)
            elif event.key == pg.K_DOWN:
                selecionado = (selecionado + 1) % len(opcoes)
            elif event.key == pg.K_F11:
                # Alternar entre tela cheia e janela
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pg.display.set_mode(DISPLAY_RESOLUTION, pg.FULLSCREEN)
                else:
                    screen = pg.display.set_mode(DISPLAY_RESOLUTION)
    
    # Preencher a tela de fundo
    screen.fill(COR_FUNDO)
    
    # Criar texto para o menu
    for i, opcao in enumerate(opcoes):
        cor = COR_TEXTO if i == selecionado else (100, 100, 100)
        texto = FONT_TEXT.render(opcao, True, cor)
        texto_rect = texto.get_rect()
        texto_rect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + i * 50)
        
        # Desenhar o texto na tela
        screen.blit(texto, texto_rect)
    
    # Atualizar a tela
    pg.display.update()
