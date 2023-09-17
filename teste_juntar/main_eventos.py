from funcs import *
from tela_jogo import Level
from player import Player

pg.init()

#fonte para o score
font = pg.font.Font(None, 36)
score = 0

# tela de jogo 
screen = pg.display.set_mode(DISPLAY_RESOLUTION)
background_img = pg.transform.scale(
    pg.image.load('images/background_castle_(resize).jpg'),
    DISPLAY_RESOLUTION
    )
gamescreen = Level(screen,background_img)


clock = pg.time.Clock()
dt = 0   #segundos

# dados do player
player = Player('images/hero.png')


# setando as plataformas iniciais
plat_group = pg.sprite.Group()
for coord in START_PLAT:
    plat_group.add(Platform('images/plataforma.jpg', coord))


moeda_group = pg.sprite.Group()  # Crie um grupo de sprites para as moedas
moeda = Moeda('images/moeda.png', 10, DISPLAY_WIDTH, DISPLAY_HEIGHT)

pg.display.set_caption('Teste')


running = True 
while running:
    keys=pg.key.get_pressed()
    gamescreen.run()
    
    # Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]): 
            #fecha no botao de quit da janela ou apertando ESC
            running = False
            break 

    player.update(plat_group)
    plat_group.update(player,moeda_group)
    moeda_group.update(player)

    hits = pg.sprite.spritecollide(player, moeda_group, True)
    score += len(hits)

    # Display atualizado
    score_text = font.render("Moedas: " + str(score), True, (200, 200, 100))
    screen.blit(score_text, (50, 50))

    plat_group.draw(screen)
    moeda_group.draw(screen)
    player.draw(screen)

    pg.display.flip()
    dt += clock.tick(60)/1000

pg.quit()
