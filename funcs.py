##### bibliotecas ########
import pygame as pg
import random as rd

from os import path 
from pygame.sprite import Sprite
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

class Player(Sprite):
    def __init__(self,img,pos):
        super().__init__() 

        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (80,100))

        self.rect = self.image.get_rect(center=pos)
        self.center = self.rect.center
        
        self.state = STILL
        self.vx = 15 # pxs/tick
        self.vy = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def jump(self):
        if self.state == STILL:
            self.vy -= JUMP_SIZE  # no primeiro tick JUMP_SIZE move o sprite 30pxs para cima
            self.state = JUMPING

    def update(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_a]:
            self.rect.x -= self.vx 
        if keys[pg.K_d]:
            self.rect.x += self.vx   

        self.vy += GRAVITY
        if self.vy>0:
            self.state = FALLING
        self.rect.y += self.vy

        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.vy = 0
            self.state = STILL



        # if keys[pg.K_w]:
        #     self.rect.y -= self.vx
        # if keys[pg.K_s]:  
        #     self.rect.y += self.vx

