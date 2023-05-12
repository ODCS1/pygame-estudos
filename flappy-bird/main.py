import pygame as pg
import os
import random as r

# Criação das constantes
TELA_LARGURA = 500
TELA_ALTURA = 800

IMAGEM_CANO = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'pipe.png')))
IMAGEM_CHAO = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'base.png')))
IMAGEM_FUNDO = pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bg.png')))
IMAGENS_PASSARO = [
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird1.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird2.png'))),
    pg.transform.scale2x(pg.image.load(os.path.join('assets', 'bird3.png')))
]

pg.font.init()
FONT_PONTOS = pg.font.SysFont('arial', 50)


# Criando as classes

class Passaro:
    IMGS = IMAGENS_PASSARO
    # Animações da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5
    
    # Configurações iniciais
    def __init__(self, x, y):
      self.x = x
      self.y = y
      self.angulo = 0
      self.velocidade = 0
      self.altura = self.y
      self.tempo = 0
      self.contagem_imagem = 0
      self.imagem = self.IMGS[0]

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y

    def mover(self):
        # Calcular o deslocamento
        self.tempo += 1
        # Equação horária do espaço M.U.V.
        deslocamento = (1.5 * self.tempo) + (self.velocidade * self.tempo)

        # Restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= -2
        
        # Definir a posição
        self.y = deslocamento

        # Ângulo do passáro
        if deslocamento < 0 or self.y < (self.altura + 50):
          if self.angulo < self.ROTACAO_MAXIMA:
              self.angulo = self.ROTACAO_MAXIMA
          else:
              if self.angulo > -90:
                  self.angulo -= self.VELOCIDADE_ROTACAO

    def desenhar(self):
        # Definir qual imagem o passáro vai usar
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO * 4:
            self.imagem = self.IMGS[1]
        elif self.imagem < self.TEMPO_ANIMACAO + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0

        # Se o passáro estiver caindo, não bate asa

         
        




class Cano:
    pass

class Chao:
    pass
