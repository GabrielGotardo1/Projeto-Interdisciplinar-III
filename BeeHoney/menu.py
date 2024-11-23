from obj import Obj
import pygame

class Menu:
    def __init__(self, image):
        # Cria o fundo do menu inicial
        self.bg = Obj(image, 0, 0)
        self.change_scene = False  # Controla a troca de cena

    def draw(self, window):
        # Desenha o fundo do menu
        self.bg.draw(window)

    def event(self, event):
        # Se a tecla Enter for pressionada, inicia o jogo
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.change_scene = True

class GameOver(Menu):
    def __init__(self, image):
        super().__init__(image)  # Reutiliza o menu para a tela de Game Over
