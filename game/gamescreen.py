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

    def update(self,player):    # Atualiza infos do display

        moeda_imagem = pg.image.load('images/moeda.png')
        moeda_imagem = pg.transform.scale(moeda_imagem, (35, 35))
        moeda_rect = moeda_imagem.get_rect()
        self.screen.blit(moeda_imagem, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-677))

        botas_imagem = pg.image.load('images/bota.png')
        botas_imagem = pg.transform.scale(botas_imagem, (38, 38))
        bota_rect = botas_imagem.get_rect()
        self.screen.blit(botas_imagem, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-625))

        font = pg.font.Font(None, 36)
        score_text = font.render(str(player.score), True, (255, 255, 255))
        botas_text = font.render(str(player.botas), True, (255, 255, 255))
        
        score_rect = score_text.get_rect(bottomright=(DISPLAY_WIDTH-moeda_rect.width-15, 70+moeda_rect.height))
        botas_rect = botas_text.get_rect(bottomright=(DISPLAY_WIDTH-bota_rect.width-15, 120+bota_rect.height))
        
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
                self.frame = 0
            center = self.rect.center

            # Atualiza imagem atual
            self.image = self.sprites[self.frame]
            
            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

        self.screen.blit(self.image, (0,0))

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
