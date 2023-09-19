from funcs import *
from player import Player
from cenario import *
from coletaveis import *

class Level():
    def __init__(self,screen,background_img):
        self.screen = screen
        self.image = background_img

    def run(self,player,score,font):
        dt = 0 #segundos
        clock = pg.time.Clock()

        # dados do player
        player = Player('images/hero.png')


        # setando as plataformas iniciais
        plat_group = pg.sprite.Group()
        for coord in START_PLAT:
            plat_group.add(Platform('images/plataforma.jpg', coord))


        moeda_group = pg.sprite.Group()  # Crie um grupo de sprites para as moedas

        pg.display.set_caption('Jogo')
        running = True
        while running:
            self.screen.blit(self.image,(0,0))
            keys=pg.key.get_pressed()
            
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
            self.screen.blit(score_text, (50, 50))

            plat_group.draw(self.screen)
            moeda_group.draw(self.screen)
            player.draw(self.screen)

            pg.display.flip()
            dt += clock.tick(60)/1000