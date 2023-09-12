import pygame as pg
from bloco import PlayerRect
from coletaveis import Moeda
import random

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_RESOLUTION = DISPLAY_WIDTH, DISPLAY_HEIGHT

pg.init()

#fonte para o score
font = pg.font.Font(None, 36)
score = 0

screen = pg.display.set_mode(DISPLAY_RESOLUTION)
fundo = pg.transform.scale(
    pg.image.load('images/espaco.jpg'),
    DISPLAY_RESOLUTION
)
screen.blit(fundo, (0, 0))
pg.display.update()

pg.display.set_caption('Teste de movimentacao retangulo (teclado_wasd)')

bloco = PlayerRect((255, 0, 0), 30, 30)
moeda_group = pg.sprite.Group()  # Crie um grupo de sprites para as moedas

clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
            # fecha no botão de quit da janela ou apertando ESC
            running = False
            break

    # atualiza a tela e o usuário
    screen.blit(fundo, (0, 0))
    bloco.draw(screen)
    bloco.update()

    # Crie uma nova moeda e adicione-a ao grupo de sprites de moedas
    if random.randint(0, 100) < 0.01:  # Adicione uma moeda com uma probabilidade de 0.01%
        moeda = Moeda((255, 255, 0), 10, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        moeda.rect.x = random.randint(0, DISPLAY_WIDTH - moeda.rect.width)
        moeda.rect.y = random.randint(0, DISPLAY_HEIGHT - moeda.rect.height)
        moeda_group.add(moeda)


    # Atualize e desenhe as moedas
    moeda_group.update()
    moeda_group.draw(screen)

    # se chegar em uma extremidade da tela -> vai para a extremidade oposta
    if not 0 < bloco.rect.x < DISPLAY_WIDTH:
        bloco.rect.x = DISPLAY_WIDTH if bloco.rect.x < 0 else 0
    if not 0 < bloco.rect.y < DISPLAY_HEIGHT:
        bloco.rect.y = DISPLAY_HEIGHT if bloco.rect.y < 0 else 0

    # Verifique a colisão entre o jogador e as moedas
    hits = pg.sprite.spritecollide(bloco, moeda_group, True)
    score += len(hits)

    score_text = font.render("SCORE: " + str(score), True, (255, 200, 100))
    screen.blit(score_text, (50, 50))

    pg.display.update()
    clock.tick(60)




pg.quit()
