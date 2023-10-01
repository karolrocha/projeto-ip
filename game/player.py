from funcs import *
# from classes_telas.telaGO import mostrar_game_over

img_dir = 'images/Hero Knight/'

# processa os arquivos das imagens
# Recebe: Lista com os nomes dos arquivos de imagens e o diretorio 
# Retorna: Dicionario (direção esquerda ou direita) -> Dicionario (sheet_nome) -> Lista -> superficies (frames do spritesheet)
def load_sprites(sheet_list: list, img_dir: str):  
    sprites = {RIGHT: {}, LEFT: {}}

    for sheet_name in sheet_list:
        sheet = load(img_dir+sheet_name).convert_alpha()
        sqr_side = sheet.get_height()
        frame_num = sheet.get_width()//sqr_side

        for num in range(frame_num):
            frame = sheet.subsurface((num*(sqr_side)+70, 60), (50, 55))     # cada frame tem aprox 55x55 (pxs)
            image_right = pg.transform.scale(frame, (90,90))       # virado para direita (padrão do arquivo)
            image_left = pg.transform.flip(image_right, flip_x=True, flip_y=False)   # virado para esquerda

            if sheet_name not in sprites[RIGHT]:
                sprites[RIGHT][sheet_name]=[image_right]  
                sprites[LEFT][sheet_name]=[image_left]
            else:
                sprites[RIGHT][sheet_name].append(image_right)
                sprites[LEFT][sheet_name].append(image_left)
        
    return sprites


class Player(Sprite):
    def __init__(self, sheets: list=SHEETS_PLAYER, pos: tuple=(0,DISPLAY_HEIGHT)):
        super().__init__() 

        self.vx = 12 # pxs/tick
        self.vy = 0
        self.direction = RIGHT
        self.state = RUNNING

        self.sprites = load_sprites(sheets, img_dir)

        # Define a animacao inicial (primeiro frame de Idle.png virado para a direita)
        self.frame = 0  
        inic_animation = self.sprites[self.direction][self.state]
        self.image = inic_animation[self.frame]
        self.last_update= pg.time.get_ticks()
        
        self.rect = self.image.get_rect(topleft=pos)
        self.highest_y = 0

        self.chao = 0
        self.score = 0
        self.botas = 0
        
    def draw(self, screen):
        frame_ticks = 100   # Tempo de troca do frame em milissegundos

        now = pg.time.get_ticks()

        # Troca o frame se ja estiver na hora
        if now - self.last_update >= frame_ticks:
            self.last_update = now
            self.frame += 1
            
            # Atualiza animacao atual
            animation = self.sprites[self.direction][self.state]

            if self.frame >= len(animation):
                self.frame = 0
            
            center = self.rect.center
            # Atualiza imagem atual
            self.image = animation[self.frame]

            # Atualiza os detalhes de posicionamento
            self.rect = self.image.get_rect()
            self.rect.center = center

        screen.blit(self.image, self.rect)

    def jump(self):
        if self.state in (IDLE,RUNNING):
            self.vy -= JUMP_SIZE 
            self.state = JUMPING
            
    def double_jump(self):
        if self.state in (IDLE,RUNNING) and self.botas > 0:
            self.vy -= 1.5*JUMP_SIZE 
            self.state = JUMPING
            self.botas = self.botas - 1

    def get_input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.direction = LEFT
            self.rect.x -= self.vx 

        if keys[pg.K_d]:
            self.direction = RIGHT
            self.rect.x += self.vx  

        if keys[pg.K_SPACE]: 
            self.jump()
        if keys[pg.K_e]: 
            self.double_jump()
        
        return keys
    
    def update(self,plat_group):
        keys = self.get_input() 

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

                    if keys[pg.K_a] or keys[pg.K_d]:
                        self.state = RUNNING
                    else:
                        self.state = IDLE 

        # Colisao com o chao (da pra substituir por alguma outra base se quiser)
        if self.rect.bottom > GROUND:
            self.rect.bottom = GROUND
            self.vy = 0
            if keys[pg.K_a] or keys[pg.K_d]:
                self.state = RUNNING
            else:
                self.state = IDLE 
            self.apoio = True

        if self.rect.bottom == GROUND:
            self.chao +=1

        # if self.chao > 120:
        #     mostrar_game_over()
