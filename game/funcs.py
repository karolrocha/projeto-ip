##### bibliotecas ########
import pygame as pg
import random as rd
import sys

from pygame.sprite import Sprite, Group
from pygame.image import load
#####################
pg.font.init()

# janela
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 750
DISPLAY_RESOLUTION = DISPLAY_WIDTH,DISPLAY_HEIGHT
GAME_BG_IMG = 'game_sheet.png'

FONTE_PATH = 'fonte/The Centurion .ttf'
BRANCO = (255, 255, 255)

# plataformas iniciais
START_PLAT=[
            [.2*DISPLAY_WIDTH, .8*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .65*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .45*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, .2*DISPLAY_HEIGHT],
            [.1*DISPLAY_WIDTH, .05*DISPLAY_HEIGHT],
            [.7*DISPLAY_WIDTH, .35*DISPLAY_HEIGHT],
            [.4*DISPLAY_WIDTH, -70]
            ]

GRAVITY = 2
# velocidade inicial no pulo
JUMP_SIZE = 27
# altura do chão
GROUND = DISPLAY_HEIGHT

# estados definidos juntos dos arquivos dos sprites 
IDLE = 'Idle.png'
JUMPING = 'Jump.png'
FALLING = 'Fall.png'
RUNNING = 'Run.png'
DEAD = 'Death.png'
SHEETS_PLAYER = [IDLE,RUNNING,FALLING,JUMPING,DEAD]
# virado para:
LEFT = 'left'
RIGHT = 'right'
