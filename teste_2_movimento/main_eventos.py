from funcs import *

pg.init()
# pg.mixer.init() -> adicionar som se precisar

# tela e superficie 
screen = pg.display.set_mode(DISPLAY_RESOLUTION)
background_img = pg.transform.scale(
    pg.image.load('images/background_castle_(resize).jpg'),
    DISPLAY_RESOLUTION
    )

# dados do player
player_pos = pg.math.Vector2(DISPLAY_WIDTH/2,0)
player = Player('images/hero.png',player_pos)
height_p = player.rect.height
width_p = player.rect.width


all_sprites = pg.sprite.Group()
all_sprites.add(player)

pg.display.set_caption('Teste de movimentacao retangulo (teclado_wasd)')

clock = pg.time.Clock()
dt = 0 #segundos
delta_y = 0

running = True 
while running:
    keys=pg.key.get_pressed()
    
    # Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and keys[pg.K_ESCAPE]): 
            #fecha no botao de quit da janela ou apertando ESC
            running = False
            break 

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()

    # (Eixo X) Se chegar em uma extremidade da tela -> vai para a extremidade oposta 
    if not -width_p < player.rect.x < DISPLAY_WIDTH:
        player.rect.x = DISPLAY_WIDTH if player.rect.x < 0 else 0

    # Updates
    all_sprites.update()

    # Display atualizado
    screen.blit(background_img, (0,0)) 
    all_sprites.draw(screen)
    
    pg.display.flip()

    dt = clock.tick(60)/1000

pg.quit()
