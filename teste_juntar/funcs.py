##### bibliotecas ########
import pygame as pg
import random as rd

from os import path 
from pygame.sprite import Sprite, Group
from pygame.image import load
#####################

# janela
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DISPLAY_RESOLUTION = DISPLAY_WIDTH,DISPLAY_HEIGHT

# Parâmetros para balancear/alterar a jogabilidade:
#   - Condicional de 'update()' em 'Platform()' -> [...] 'player.rec.y < (parâmetro)*DISPLAY_HEIGHT: [...]'
#   - JUMP_SIZE
#   - GRAVITY
#   - Plataformas iniciais
#   - os fatores randômicos da formação de novas plataformas
#   - Frenquencia de aparecimento de moedas em :
#      'Platform()' -> 'update()'-> 'if rd.randint(0,800) < 1: ...'

GRAVITY = 2
# velocidade inicial no pulo
JUMP_SIZE = 30
# altura do chão
GROUND = DISPLAY_HEIGHT

# estados 
STILL = 0
JUMPING = 1
FALLING = -1
        
# plataformas iniciais
START_PLAT=[
            [.7*DISPLAY_WIDTH, .8*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .65*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .5*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .2*DISPLAY_HEIGHT],
            [.1*DISPLAY_WIDTH, .05*DISPLAY_HEIGHT],
            [.7*DISPLAY_WIDTH, .35*DISPLAY_HEIGHT],
            [.1*DISPLAY_WIDTH, -200]
            ]


class Platform(Sprite):
    def __init__(self, img, pos: list=[.4*DISPLAY_WIDTH,DISPLAY_HEIGHT-100]):
        
        super().__init__()
        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (250, 30))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, player, moeda_group):   # remove ou acrescenta plataformas 
        
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy 
        
        if self.rect.y > DISPLAY_HEIGHT:    # Saiu da tela
            self.rect.y = rd.randint(-50,-10)  # 50-10 pxs acima da tela
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
    

class Moeda(Sprite):
    def __init__(self, img, radius, screen_width, screen_height):
        super().__init__()
        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, screen_width - 2 * radius)
        self.rect.y = rd.randint(0, screen_height - 2 * radius)

    def update(self, player):
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy
             
    def draw(self,screen):
        pass