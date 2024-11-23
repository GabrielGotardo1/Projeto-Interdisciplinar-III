import pygame  # Biblioteca gráfica

class Obj:
    def __init__(self, image, x, y):
        # Cria um grupo e um sprite para o objeto
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image)
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

        # Controla a animação
        self.frame = 1
        self.tick = 0

    def draw(self, window):
        # Desenha o objeto na janela
        self.group.draw(window)

    def anim(self, image, tick, frames):
        # Gera a animação do objeto trocando as imagens dos frames
        self.tick += 1
        if self.tick == tick:
            self.tick = 0
            self.frame += 1
        if self.frame == frames:
            self.frame = 1
        self.sprite.image = pygame.image.load("assets/" + image + str(self.frame) + ".png")


class Bee(Obj):
    def __init__(self, image, x, y):
        # Inicializa a classe base Obj e configura sons e atributos da abelha
        super().__init__(image, x, y)

        # Carrega efeitos sonoros para quando a abelha ganha pontos ou perde vida
        pygame.mixer.init()
        self.sound_pts = pygame.mixer.Sound("assets/sounds/score.ogg")  # Som ao ganhar pontos
        self.sound_block = pygame.mixer.Sound("assets/sounds/bateu.ogg")  # Som ao colidir com aranha

        # Atributos de vida e pontuação
        self.life = 3  # Número inicial de vidas da abelha
        self.pts = 0  # Pontuação inicial da abelha

    def move_bee(self, event):
        # Move a abelha para a posição do mouse, permitindo controle fácil pelo jogador
        if event.type == pygame.MOUSEMOTION:
            # Ajusta a posição da abelha para ficar centralizada no cursor
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def colision(self, group, name):
        # Verifica colisão entre a abelha e outros objetos
        colision = pygame.sprite.spritecollide(self.sprite, group, True)

        if name == "Flower" and colision:
            # Aumenta a pontuação se colidir com uma flor
            self.pts += 1
            self.sound_pts.play()  # Toca som de pontuação
        elif name == "Spider" and colision:
            # Reduz uma vida se colidir com uma aranha
            self.life -= 1
            self.sound_block.play()  # Toca som de colisão
            

class Text:
    def __init__(self, size, text):
        # Configura a fonte e renderiza o texto inicial
        self.font = pygame.font.SysFont("Arial bold", size)  # Fonte em negrito
        self.render = self.font.render(text, False, (255, 255, 255))  # Texto branco

    def draw(self, window, x, y):
        # Desenha o texto na janela na posição especificada
        window.blit(self.render, (x, y))

    def update_text(self, update):
        # Atualiza o texto renderizado, útil para atualizar a pontuação ou vidas
        self.render = self.font.render(update, False, (255, 255, 255))

