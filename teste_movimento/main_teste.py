import pygame as pg
from bloco import PlayerRect
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_RESOLUTION = DISPLAY_WIDTH,DISPLAY_HEIGHT

pg.init()

screen = pg.display.set_mode(DISPLAY_RESOLUTION, )
fundo = pg.transform.scale(
    pg.image.load('images/espaco.jpg'),
    DISPLAY_RESOLUTION
    )
screen.blit( fundo, (0,0))
pg.display.update()

pg.display.set_caption('Teste de movimentacao retangulo (teclado_wasd)')

bloco = PlayerRect((255, 0, 0), 30, 30)

clock = pg.time.Clock()
running = True 
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]): 
            #fecha no botao de quit da janela ou apertando ESC
            running = False
            break      
    
    #atualiza a tela e o usuario
    screen.blit(fundo, (0,0))
    bloco.draw(screen)
    bloco.update()

    # se chegar em uma extremidade da tela -> vai para a extremidade oposta
    if not 0<bloco.x<DISPLAY_WIDTH:
        bloco.x = DISPLAY_WIDTH if bloco.x<0 else 0
    if not 0<bloco.y<DISPLAY_HEIGHT:
        bloco.y = DISPLAY_HEIGHT if bloco.y<0 else 0
    
    pg.display.update()
    clock.tick(60)

pg.quit()
