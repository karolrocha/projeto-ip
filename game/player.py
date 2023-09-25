from funcs import *

class Player(Sprite):
    def __init__(self, img, pos: tuple=(0,DISPLAY_HEIGHT)):
        super().__init__() 

        image = pg.image.load(img)
        self.image = pg.transform.scale(image, (80,100))

        self.rect = self.image.get_rect(topleft=pos)
        self.center = self.rect.center
        self.highest_y = 0

        self.state = FALLING
        self.vx = 15 # pxs/tick
        self.vy = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def jump(self):
        if self.state == STILL:
            self.vy -= JUMP_SIZE  # no primeiro tick JUMP_SIZE move o sprite 30pxs para cima
            self.state = JUMPING
            
    def double_jump(self):
        if self.state == STILL:
            self.vy -= 1.5*JUMP_SIZE  # no primeiro tick JUMP_SIZE move o sprite 30pxs para cima
            self.state = JUMPING

    def get_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.vx 
        if keys[pg.K_d]:
            self.rect.x += self.vx  
        if keys[pg.K_SPACE]: 
            self.jump()
        if keys[pg.K_e]: 
            self.double_jump()
        
    def update(self,plat_group):
        self.get_input() 

        # Eixo X
        # Se chegar em uma extremidade da tela -> vai para a extremidade oposta 
        if not -self.rect.width < self.rect.x < DISPLAY_WIDTH:
            self.rect.x = DISPLAY_WIDTH if self.rect.x < 0 else 0
        
        # Eixo y
        if self.state!=FALLING:
            self.highest_y=self.rect.bottom

        self.vy += GRAVITY
        self.rect.y += self.vy
        
        if self.vy > 0: 
            self.state = FALLING
            collisions = pg.sprite.spritecollide(self, plat_group, False)
            for platform in collisions:
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top  # atualiza a altura no mapa
                    self.highest_y = self.rect.bottom   
                    self.vy = 0 
                    self.state = STILL

        # Colisao com o chao (da pra substituir por alguma outra base se quiser)
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.vy = 0
            self.state = STILL