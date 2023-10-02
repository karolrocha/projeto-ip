from funcs import *
from contador import Timer

class Relogio(Sprite):
    group = Group()
    contador = Timer()

    def __init__(self, img, tempo_extra: int=10):
        super().__init__()
        image = load(img)
        self.image = pg.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()

        self.t_extra = tempo_extra 

    def coletar(self):
        self.contador.bonus = True
        self.contador.time += self.t_extra
        self.kill()

    def update(self, player):
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy

        if self.rect.y>=GROUND:
            self.kill()

        for relogio in self.group:
            if player.rect.colliderect(relogio.rect):
                relogio.coletar()

    def draw(self,screen):
        screen.blit(self.image, self.rect)

class Moeda(Sprite):
    group = Group()

    def __init__(self, img):
        super().__init__()
        image = load(img)
        self.image = pg.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        
    def update(self, player):
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy

        if self.rect.y>=GROUND: 
            self.kill()

        hits = pg.sprite.spritecollide(player, Moeda.group, True)
        player.score += len(hits)

    def draw(self,screen):
        screen.blit(self.image, self.rect)

class JumpBoost(Sprite):
    group = Group()

    def __init__(self, img):
        super().__init__()
        image = load(img)
        self.image = pg.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
    
    def update(self, player):
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy
        
        if self.rect.y>=GROUND: 
            self.kill()

        hits = pg.sprite.spritecollide(player, JumpBoost.group, True)
        player.botas += len(hits)
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)