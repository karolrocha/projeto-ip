from funcs import *
from tela_jogo import Level
from player import Player

pg.init()
# pg.mixer.init() -> adicionar som se precisar

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
dt = 0 #segundos


# dados do player
player = Player('images/hero.png',(DISPLAY_WIDTH/2, DISPLAY_HEIGHT))
height_p = player.rect.height
width_p = player.rect.width

plataforma1 = Platform('images\plataforma.jpg', 150, 650 )
plataforma2 = Platform('images\plataforma.jpg', 300, 500 )
plataforma3 = Platform('images\plataforma.jpg', 450, 350 )
plataforma4 = Platform('images\plataforma.jpg', 600, 200 )
plataforma5 = Platform('images\plataforma.jpg', 750, 50 )
plat_group = pg.sprite.Group()
plat_group.add(plataforma1, plataforma2, plataforma3, plataforma4, plataforma5)

moeda_group = pg.sprite.Group()  # Crie um grupo de sprites para as moedas
moeda = Moeda('images\moeda.png', 10, DISPLAY_WIDTH, DISPLAY_HEIGHT)

all_sprites = pg.sprite.Group()

pg.display.set_caption('Teste')


running = True 
while running:
    keys=pg.key.get_pressed()

    # Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and keys[pg.K_ESCAPE]): 
            #fecha no botao de quit da janela ou apertando ESC
            running = False
            break 
    
    # Updates
    all_sprites.add(plat_group)
    all_sprites.add(new_coins(moeda_group))
    hits = pg.sprite.spritecollide(player, moeda_group, True)
    score += len(hits)
    
    # player.update([collidables, etc.])
    player.update(plat_group)
    all_sprites.update()
    
    # Display atualizado
    gamescreen.run()
    score_text = font.render("Moedas: " + str(score), True, (255, 200, 100))
    screen.blit(score_text, (50, 50))

    player.draw(screen)
    all_sprites.draw(screen)
    
    pg.display.flip()
    dt += clock.tick(60)/1000

pg.quit()
