import sys
from classes_telas.telaGO import mostrar_game_over
sys.path.append('game')

from funcs import *
from player import Player
from cenario import *
from coletaveis import *

class Level():
    def __init__(self,screen,background_img):
        self.screen = screen
        self.image = background_img

    def run(self,player,font):
        dt = 0 #segundos
        clock = pg.time.Clock()
        timer = Timer()
        
        # dados do player
        player = Player('images/hero.png')


        # setando as plataformas iniciais
        plat_group = pg.sprite.Group()
        for coord in START_PLAT:
            plat_group.add(Platform('images/plataforma.jpg', coord))


        moeda_group = pg.sprite.Group()  # Crie um grupo de sprites para as moedas
        # tempoextra_group = pg.sprite.Group()
        puloduplo_group = pg.sprite.Group()

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
                    pg.quit()
                    sys.exit()

            # Quando o tempo acabar volta para o menu
            if timer.time <= -0.5:
                running = False
                mostrar_game_over()

            player.update(plat_group)
            plat_group.update(player, moeda_group, timer, puloduplo_group)
            moeda_group.update(player)
            Relogio.clock_group.update(player)
            puloduplo_group.update(player)
            timer.update()

            hits = pg.sprite.spritecollide(player, moeda_group, True)
            player.score += len(hits)

            hits = pg.sprite.spritecollide(player, puloduplo_group, True)
            player.botas += len(hits)

            # Display atualizado
            moeda_imagem = pg.image.load('images/moeda.png')
            moeda_imagem = pg.transform.scale(moeda_imagem, (35, 35))
            self.screen.blit(moeda_imagem, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-677))

            botas_imagem = pg.image.load('images/bota.png')
            botas_imagem = pg.transform.scale(botas_imagem, (38, 38))
            self.screen.blit(botas_imagem, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-625))

            score_text = font.render(str(player.score), True, (255, 255, 255))
            botas_text = font.render(str(player.botas), True, (255, 255, 255))
            self.screen.blit(score_text, (DISPLAY_WIDTH-70, DISPLAY_HEIGHT-672))
            self.screen.blit(botas_text, (DISPLAY_WIDTH-70, DISPLAY_HEIGHT-620))

            plat_group.draw(self.screen)
            moeda_group.draw(self.screen)
            Relogio.clock_group.draw(self.screen)
            puloduplo_group.draw(self.screen)
            player.draw(self.screen)
            timer.draw(self.screen)

            pg.display.flip()
            dt += clock.tick(60)/1000
