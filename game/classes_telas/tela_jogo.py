import sys
sys.path.append('game')

from funcs import *
from player import Player
from plataforma import Platform
from coletaveis import *
# from classes_telas.telaGO import mostrar_game_over

class Level():
    def __init__(self,screen,background_img):
        self.screen = screen
        self.image = background_img
        self.group_sprites = Group()

        self.player = Player()

    def update(self,player):    # Atualiza infos do display
        hits = pg.sprite.spritecollide(player, Moeda.group, True)
        player.score += len(hits)

        hits = pg.sprite.spritecollide(player, JumpBoost.group, True)
        player.botas += len(hits)

        moeda_imagem = pg.image.load('images/moeda.png')
        moeda_imagem = pg.transform.scale(moeda_imagem, (35, 35))
        self.screen.blit(moeda_imagem, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-677))

        botas_imagem = pg.image.load('images/bota.png')
        botas_imagem = pg.transform.scale(botas_imagem, (38, 38))
        self.screen.blit(botas_imagem, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-625))

        font = pg.font.Font(None, 36)
        score_text = font.render(str(player.score), True, (255, 255, 255))
        botas_text = font.render(str(player.botas), True, (255, 255, 255))
        self.screen.blit(score_text, (DISPLAY_WIDTH-70, DISPLAY_HEIGHT-672))
        self.screen.blit(botas_text, (DISPLAY_WIDTH-70, DISPLAY_HEIGHT-620))

    def reset(self):
        for group_type in self.group_sprites:
            for sprite in group_type.group:
                sprite.kill()
        self.player = Player()
        Relogio.contador = Timer()

    def run(self):
        clock = pg.time.Clock()

        for coord in START_PLAT:
            Platform.group.add(Platform('images/plataforma.jpg', coord))

        pg.display.set_caption('Medieval Jump')
        running = True
        while running:
            clock.tick(60)
            self.screen.blit(self.image,(0,0))
            self.group_sprites.add(Platform.group, Moeda.group, JumpBoost.group, Relogio.group)

            # Eventos
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]): 
                    #fecha no botao de quit da janela ou apertando ESC
                    running = False
                    self.reset()

            # Quando o tempo acabar volta para o menu
            # if Relogio.contador.time <= -0.5:
            #     running = False
            #     mostrar_game_over()
            
            # Updates
            self.player.update(Platform.group)
            self.group_sprites.update(self.player)
            Relogio.contador.update()
            Relogio.contador.draw(self.screen)
            self.update(self.player)
            
            # Display atualizado
            self.player.draw(self.screen)
            self.group_sprites.draw(self.screen)
            
            
            pg.display.flip()
