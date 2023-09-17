from funcs import *

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