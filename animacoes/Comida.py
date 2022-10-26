from animacoes.Animacao import Animacao
from GameConfig import GameConfig
import pygame

class Comida(Animacao):
    iiDelay = 90
    iiNumeroFrames = 3
    iiWidth = 48
    iiHeight = 32
    isTipo = GameConfig.TIPO_ITEM_VIDA

    def __init__(self, pos=[]):
        self.Img = Animacao.cropImage(GameConfig.DIR_ANIMACOES + "comida", self)
        self.image = self.Img[self.iiFrame]
        Animacao.__init__(self)
        self.rect.x, self.rect.y = pos[0], pos[1]

    def update(self, keys):
        super().__updateFrame__(pygame.time.get_ticks())

    def getImage(self):
        return self.image

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def getTipo(self):
        return self.isTipo
