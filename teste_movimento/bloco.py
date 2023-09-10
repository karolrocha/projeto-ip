import pygame as pg
class PlayerRect():
    def __init__(self, color, width, height, x: int=0, y: int=0):
        self.x = x
        self.y = y
        self.speed = 5 # px/s 
        self.width = width
        self.height = height
        self.color = color

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
    
    # x cresce da esquerda para a direita e y cresce de cima para baixo
    # canto superior esquerdo da tela = origem
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]: self.x -= self.speed
        if keys[pg.K_d]: self.x += self.speed
        if keys[pg.K_w]: self.y -= self.speed
        if keys[pg.K_s]: self.y += self.speed 
