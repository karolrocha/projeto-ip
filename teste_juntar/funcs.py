##### bibliotecas ########
import pygame as pg
import random as rd

from os import path 
from pygame.sprite import Sprite, Group
from pygame.image import load
#####################

# janela
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 720
DISPLAY_RESOLUTION = DISPLAY_WIDTH,DISPLAY_HEIGHT

# Parâmetros para balancear/alterar a jogabilidade:
#   - Condicional de 'update()' em 'Platform()' -> [...] 'player.rec.y < (parâmetro)*DISPLAY_HEIGHT: [...]'
#   - JUMP_SIZE
#   - GRAVITY
#   - Plataformas iniciais
#   - os fatores randômicos da formação de novas plataformas

GRAVITY = 2
# velocidade inicial no pulo
JUMP_SIZE = 28
# altura do chão
GROUND = DISPLAY_HEIGHT

# estados 
STILL = 0
JUMPING = 1
FALLING = -1
        
# plataformas iniciais
START_PLAT=[
            [.7*DISPLAY_WIDTH, .8*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .7*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .5*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .3*DISPLAY_HEIGHT],
            [.1*DISPLAY_WIDTH, .1*DISPLAY_HEIGHT],
            [.7*DISPLAY_WIDTH, .4*DISPLAY_HEIGHT],
            [.1*DISPLAY_WIDTH, -200]
            ]


class Platform(Sprite):
    def __init__(self, 
                 pos: list=[.4*DISPLAY_WIDTH,DISPLAY_HEIGHT-100], 
                 color: tuple=(128,128,128) 
                 ):
        
        super().__init__()
        self.image = pg.Surface((250,15), pg.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self, player):   # remove ou acrescenta plataformas 
        
        if player.state!=FALLING and player.rect.y < .4*DISPLAY_HEIGHT:
            self.rect.y -= player.vy 
        
        if self.rect.y > DISPLAY_HEIGHT:    # Saiu da tela
            self.rect.y = rd.randint(-50,-10)  # 50-10 pxs acima da tela
            self.rect.x = rd.randint(0,DISPLAY_WIDTH-self.rect.width)  # garante que vai aparecer totalmente dentro da tela 

    def draw(self, screen):
        pass 
    

class Moeda(Sprite):
    def __init__(self, color, radius, screen_width, screen_height):
        super().__init__()
        self.image = pg.Surface((2 * radius, 2 * radius), pg.SRCALPHA)
        pg.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, screen_width - 2 * radius)
        self.rect.y = rd.randint(0, screen_height - 2 * radius)

    def update(self):
        pass
    def draw(self,screen):
        pass

def new_coins(moeda_group):
    if rd.randint(0, 100) < 0.01:  # Adicione uma moeda com uma probabilidade de 0.01%
        moeda = Moeda((255, 255, 0), 10, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        moeda.rect.x = rd.randint(0, DISPLAY_WIDTH - moeda.rect.width)
        moeda.rect.y = rd.randint(0, DISPLAY_HEIGHT - moeda.rect.height)
        moeda_group.add(moeda)
    return moeda_group
    