import pygame as pg
import random
import math

class Moeda(pg.sprite.Sprite):
    def __init__(self, color, radius, screen_width, screen_height):
        super().__init__()
        self.image = pg.Surface((2 * radius, 2 * radius), pg.SRCALPHA)
        pg.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 2 * radius)
        self.rect.y = random.randint(0, screen_height - 2 * radius)


    def update(self):
        pass
