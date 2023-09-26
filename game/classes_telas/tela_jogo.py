from funcs import *
from player import Player
from cenario import *
from coletaveis import *

class Level():
    def __init__(self,screen,background_img):
        self.screen = screen
        self.image = background_img

    def run(self,player,score,font, tempo, botas):
        dt = 0 #segundos
        clock = pg.time.Clock()
        cont = 0

        # dados do player
        player = Player('images/hero.png')


        # setando as plataformas iniciais
        plat_group = pg.sprite.Group()
        for coord in START_PLAT:
            plat_group.add(Platform('images/plataforma.jpg', coord))


        moeda_group = pg.sprite.Group()  # Crie um grupo de sprites para as moedas
        tempoextra_group = pg.sprite.Group()
        puloduplo_group = pg.sprite.Group()

        pg.display.set_caption('Jogo')
        running = True
        while running:
            self.screen.blit(self.image,(0,0))
            keys=pg.key.get_pressed()

            # contagem regressiva
            cont += 1
            if cont//60 == cont/60:
                tempo -= 1
            
            # Eventos
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]): 
                    #fecha no botao de quit da janela ou apertando ESC
                    running = False
                    pg.quit()
                    sys.exit()

            # Quando o tempo acabar volta para o menu
            if tempo <= -0.5:
                running = False
                break

            player.update(plat_group)
            plat_group.update(player,moeda_group, tempoextra_group, puloduplo_group)
            moeda_group.update(player)
            tempoextra_group.update(player)
            puloduplo_group.update(player)

            hits = pg.sprite.spritecollide(player, moeda_group, True)
            score += len(hits)

            hits = pg.sprite.spritecollide(player, tempoextra_group, True)
            tempo += (len(hits)*10)

            hits = pg.sprite.spritecollide(player, puloduplo_group, True)
            botas += len(hits)

            # Display atualizado
            score_text = font.render("MOEDAS: " + str(score), True, (200, 200, 100))
            botas_text = font.render("BOTAS: " + str(botas), True, (200, 200, 100))
            tempo_text = font.render("TEMPO: " + str(tempo), True, (200, 200, 100))
            self.screen.blit(score_text, (50, 50))
            self.screen.blit(botas_text, (50, 100))
            self.screen.blit(tempo_text, (50, 150))

            plat_group.draw(self.screen)
            moeda_group.draw(self.screen)
            tempoextra_group.draw(self.screen)
            puloduplo_group.draw(self.screen)
            player.draw(self.screen)

            pg.display.flip()
            dt += clock.tick(60)/1000
