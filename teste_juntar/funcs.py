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

GRAVITY = 2
# velocidade inicial no pulo
JUMP_SIZE = 30
# altura do chão
GROUND = DISPLAY_HEIGHT

# estados 
STILL = 0
JUMPING = 1
FALLING = -1
        
class Platform(Sprite):
    def __init__(self,color):
        super().__init__()
        self.image = pg.Surface((300,15), pg.SRCALPHA)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = 640
        self.rect.y = 540
        self.group = Group()
        
    def update(self):
        pass
    def draw(self, screen):
        screen.blit(self.image,self.rect)
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
    