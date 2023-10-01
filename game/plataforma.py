from funcs import *
from coletaveis import *


class Platform(Sprite):
    group = Group()

    def __init__(self, img, pos: list=[.4*DISPLAY_WIDTH,DISPLAY_HEIGHT-100]):
        
        super().__init__()
        image = load(img)
        self.image = pg.transform.scale(image, (150, 30))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # itens da plataforma
        self.moedas = Group()
        self.relogios = Group()
        self.djumps = Group()

    def plat_coin(self):    # aparecimento de moedas em plataformas

        for _ in range(rd.randint(1,2)):
            moeda = Moeda('images/moeda.png')
            moeda.rect.x = rd.randrange(self.rect.x,self.rect.x+self.rect.width)
            moeda.rect.y = self.rect.y-moeda.rect.height-10
            Moeda.group.add(moeda)
            self.moedas.add(moeda)
        
    def plat_clock(self):   # aparecimento de tempo extra em plataformas

        relogio = Relogio('images/relogio.png')
        relogio.rect.x = rd.randrange(self.rect.x,self.rect.x+self.rect.width)
        relogio.rect.y = self.rect.y-relogio.rect.height-10
        Relogio.group.add(relogio)
        self.relogios.add(relogio)

    def plat_djump(self):   # aparecimento de pulo duplo em plataformas

        for _ in range(rd.randint(1,3)):
            pulo = JumpBoost('images/bota.png')
            pulo.rect.x = rd.randrange(self.rect.x,self.rect.x+self.rect.width)
            pulo.rect.y = self.rect.y-pulo.rect.height-10
            JumpBoost.group.add(pulo)

    def repos_plat(self):  # metodo recursivo pra reposicionar plataformas que se sobrepoem

        if self in self.group:
            self.remove(self.group)

        collisions = pg.sprite.spritecollideany(self, self.group)
        if collisions is not None:
            self.rect.y = rd.randint(-40,-10) 
            self.rect.x = rd.randint(0,DISPLAY_WIDTH-self.rect.width)  
            self.repos_plat()
            
        self.add(self.group)

    def update(self, player):   # remove ou acrescenta plataformas 
        
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy 
        
        if self.rect.y > DISPLAY_HEIGHT:    # Saiu da tela
            self.rect.y = rd.randint(-40,-10) 
            self.rect.x = rd.randint(0,DISPLAY_WIDTH-self.rect.width)  
            self.repos_plat()   # checa se colidiu e reposiciona caso necessario

        # geradores de itens
        if rd.randint(0,2500)<1: # botas
            self.plat_djump()
        if rd.randint(0,2100)<1 and len(self.relogios)<1:  # relogios
            self.plat_clock()
        if rd.randint(0,10)<1 and self.rect.y<0 and len(self.moedas)<3:  # moedas
            self.plat_coin()

    def draw(self, screen):
        screen.blit(self.image, self.rect)