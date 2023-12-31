from funcs import *

class Timer(Sprite):
    def __init__(self, bottomright: tuple=DISPLAY_RESOLUTION):
        super().__init__()

        image = load('images/relogio.png')
        self.image = pg.transform.scale(image, (64,64))
        self.rect = self.image.get_rect()
        self.rect.bottomright = bottomright
        
        self.color = (255,255,255)

        self.time = 60
        self.bonus = False
        self.count = pg.time.get_ticks()/1000

        # sempre inicia com 1 min
        min, seg = 1, 0
        self.fonte = pg.font.Font(None, 40)
        self.fonte.set_bold(True)
        self.text = self.fonte.render(f'{min}:{seg}0', True, self.color)
    
    def update(self):
        now = pg.time.get_ticks()/1000
        if now - self.count >= 1:
            self.time -= 1
            self.count = now
            min = self.time//60
            seg = self.time%60

            if seg < 10: seg = f'0{seg}'

            if self.bonus:
                self.text = self.fonte.render(f'+10s  {min}:{seg}', True, self.color)
                self.bonus = False
            else:
                self.text = self.fonte.render(f'{min}:{seg}', True, self.color)

    def draw(self,screen):
        # generaliza pra quando o texto atualiza (o bottomright sempre se mantem o mesmo)
        text_rect = self.text.get_rect()
        text_rect.bottomright = (DISPLAY_WIDTH-self.rect.width,DISPLAY_HEIGHT)

        screen.blit(self.text,text_rect)
        screen.blit(self.image, self.rect)