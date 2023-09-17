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
    def __init__(self, img, x, y):
        super().__init__()
        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (150, 15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.group = Group()
        
    def update(self):
        pass
    def draw(self, screen):
        screen.blit(self.image,self.rect)
        pass 

class Moeda(Sprite):
    def __init__(self, img, radius, screen_width, screen_height):
        super().__init__()
        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = rd.randint(0, screen_width - 2 * radius)
        self.rect.y = rd.randint(0, screen_height - 2 * radius)

    def update(self):
        pass
    def draw(self,screen):
        pass

def new_coins(moeda_group):  
    if rd.randint(0, 1500) < 1:  # Adicione uma moeda com uma probabilidade de 5/1000
        moeda = Moeda('images\moeda.png', 10, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        moeda.rect.x = rd.randint(0, DISPLAY_WIDTH - moeda.rect.width)
        moeda.rect.y = rd.randint(0, DISPLAY_HEIGHT - moeda.rect.height)
        moeda_group.add(moeda)
    return moeda_group
    