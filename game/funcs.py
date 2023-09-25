##### bibliotecas ########
import pygame as pg
import random as rd
import sys

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