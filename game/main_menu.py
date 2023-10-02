from funcs import *
from classes_telas.tela_jogo import * 

pg.init()

# Configuração da tela
SCREEN = pg.display.set_mode(DISPLAY_RESOLUTION)
pg.display.set_caption('Menu')

img_dir = 'images/background/background_menu/'
def load_sprites(dir: str):  # dim = 1000x750 
    bg_images = []
    for i in range(1,4):
        image = load(dir+f'layer_{i}.png').convert_alpha()
        height = image.get_height()
        ratio = 1000/320
        image = pg.transform.scale(image, (1000, int(height*ratio)))
        bg_images.append(image)

    layer_2 = pg.transform.scale(bg_images[1], (1000,500))
    bg_images[1] = layer_2
    return bg_images
  
class Menu(Sprite):
    def __init__(self, screen: pg.surface.Surface):
        super().__init__()
        
        self.screen = screen
        self.sprites = load_sprites(img_dir)
        self.last_update = pg.time.get_ticks()
        
        self.scroll = 0

        self.gamescreen = Level(screen)

    def draw(self):
        for i, img in enumerate(self.sprites):
            if i!=2:
                self.screen.blit(img, (0,i*250))

        width = self.sprites[2].get_width()
        for i in range(3):
            self.screen.blit(self.sprites[2],(i*width + self.scroll, 657))

        self.scroll -= 1
        if abs(self.scroll)>width:
            self.scroll=0

    def loop(self):
        opcoes = ["Iniciar", "Sair"]
        selecionado = 0
        clock = pg.time.Clock()

        while True:
            clock.tick(60)
            self.draw()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        if selecionado == 0:
                            try:
                                self.gamescreen.run()
                            finally:
                                pass
                        elif selecionado == 1:
                            pg.quit()
                            sys.exit()
                    elif event.key == pg.K_UP:
                        selecionado = (selecionado - 1) % len(opcoes)
                    elif event.key == pg.K_DOWN:
                        selecionado = (selecionado + 1) % len(opcoes)
            
            # Criar texto para o menu
            for i, opcao in enumerate(opcoes):
                cor = COR_TEXTO if i == selecionado else (100, 100, 100)
                texto = FONT_TEXT.render(opcao, True, cor)
                texto_rect = texto.get_rect()
                texto_rect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2 + i * 50)
                
                # Desenhar o texto na tela
                self.screen.blit(texto, texto_rect)
            
            # Atualizar a tela
            pg.display.update()


main = Menu(SCREEN)
try:
    main.loop()
finally:
    pg.quit()

