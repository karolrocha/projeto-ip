from funcs import pg,rd,Sprite,DISPLAY_HEIGHT,DISPLAY_WIDTH,FALLING,Moeda


class Platform(Sprite):
    def __init__(self, img, pos: list=[.4*DISPLAY_WIDTH,DISPLAY_HEIGHT-100]):
        
        super().__init__()
        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (150, 30))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, player, moeda_group):   # remove ou acrescenta plataformas 
        
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy 
        
        if self.rect.y > DISPLAY_HEIGHT:    # Saiu da tela
            self.rect.y = rd.randint(-40,-10)  # 30-10 pxs acima da tela
            self.rect.x = rd.randint(0,DISPLAY_WIDTH-self.rect.width)  # garante que vai aparecer totalmente dentro da tela 
        
        # aparecimento de moedas em plataformas
        if rd.randint(0,10000) < 1: 
            for _ in range(rd.randint(1,3)):
                moeda = Moeda('images/moeda.png', 10, DISPLAY_WIDTH, DISPLAY_HEIGHT)
                moeda.rect.x = rd.randrange(self.rect.x,self.rect.x+self.rect.width)
                moeda.rect.y = self.rect.y-moeda.rect.height
                moeda_group.add(moeda)

    def draw(self, screen):
        pass 