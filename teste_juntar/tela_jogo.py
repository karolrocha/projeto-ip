from funcs import *

class Level():
    def __init__(self,screen,background_img):
        self.screen = screen
        self.image = background_img

    def run(self):
        self.screen.blit(self.image,(0,0))