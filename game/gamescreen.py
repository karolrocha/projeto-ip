img_dir = 'images/background/'

from funcs import *
from player import Player
from plataforma import Platform
from coletaveis import *

def load_sprites(dir: str, sheet: str):  # dim = 1000x750 
    sprites = []
    bg = load(dir+sheet).convert_alpha()
    frames = bg.get_width()//1000

    for num in range(frames):
        image = bg.subsurface((num*1000,0), (1000,750))
        sprites.append(image)

    return sprites

class Level(Sprite):
    def __init__(self, screen: pg.surface.Surface):
        super().__init__()

        self.screen = screen
        self.sprites = load_sprites(img_dir,GAME_BG_IMG)
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.image = self.sprites[self.frame]
        self.rect = self.image.get_rect()
        self.scroll = 0

        self.group_sprites = Group()
        self.player = Player()

        # self.update_go = pg.time.get_ticks()

    def update(self):    # Atualiza infos do display
        timer_rect = Relogio.contador.rect

        moeda_imagem = pg.image.load('images/moeda.png')
        moeda_imagem = pg.transform.scale(moeda_imagem, (35, 35))
        moeda_rect = moeda_imagem.get_rect()

        botas_imagem = pg.image.load('images/bota.png')
        botas_imagem = pg.transform.scale(botas_imagem, (38, 38))
        bota_rect = botas_imagem.get_rect()
        
        font = pg.font.Font(None, 30)
        score_text = font.render(str(self.player.score), True, (255, 255, 255))
        botas_text = font.render(str(self.player.botas), True, (255, 255, 255))

        moeda_rect.bottomleft = (timer_rect.x+20, timer_rect.y - 15)
        bota_rect.bottomleft = (moeda_rect.x, moeda_rect.y - 15)

        self.screen.blit(moeda_imagem, moeda_rect)
        self.screen.blit(botas_imagem, bota_rect)

        score_rect = score_text.get_rect(topright=(moeda_rect.x-10, moeda_rect.y+5))
        botas_rect = botas_text.get_rect(topright=(bota_rect.x-10, bota_rect.y+5))
        
        self.screen.blit(score_text, score_rect)
        self.screen.blit(botas_text, botas_rect)
    
    def draw(self):
        # ANIMACAO 
        frame_ticks = 100   # Tempo de troca do frame em milissegundos
        now = pg.time.get_ticks()

        # Troca o frame se ja estiver na hora
        if now - self.last_update >= frame_ticks:
            self.last_update = now
            self.frame += 1

            if self.frame >= len(self.sprites):
                self.frame = 0 if self.player.state!=DEAD else len(self.sprites)-1

            center = self.rect.center

            # Atualiza imagem atual
            self.image = self.sprites[self.frame]
            
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

        self.screen.blit(self.image, (0,0))

    def gameover(self):
        msg1 = 'GameOver'
        msg2 = 'Aperte  ESC  para voltar ao menu'
        fonte = pg.font.Font(FONTE_PATH,45)
        
        texto1 = fonte.render(msg1, True, BRANCO)
        texto2 = fonte.render(msg2, True, BRANCO)
        txt1_rect = texto1.get_rect(center=(DISPLAY_WIDTH//2, 200))
        txt2_rect = texto2.get_rect(center=(DISPLAY_WIDTH//2, 250))
        
        self.screen.blit(texto1, txt1_rect)
        self.screen.blit(texto2, txt2_rect)
            
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

            self.draw()
            self.group_sprites.add(Platform.group, Moeda.group, JumpBoost.group, Relogio.group)

            # Eventos
            for event in pg.event.get():
                if event.type == pg.QUIT or (event.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]): 
                    #fecha no botao de quit da janela ou apertando ESC
                    running = False
                    self.reset()

            # Quando o tempo acabar volta para o menu
            if Relogio.contador.time <= 0:
                running = False
                self.gameover()

            # Updates
            if self.player.state!=DEAD:
                self.player.update(Platform.group)  
                self.group_sprites.update(self.player)
                Relogio.contador.update()
            else:
                self.gameover()

            self.update()    
            Relogio.contador.draw(self.screen)
            
            # Display atualizado
            self.player.draw(self.screen)
            self.group_sprites.draw(self.screen)
            
            pg.display.flip()
