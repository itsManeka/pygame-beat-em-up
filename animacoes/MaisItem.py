from animacoes.Animacao import Animacao
from GameConfig import GameConfig
import pygame

class MaisItem(Animacao):
    iiDelay = 120
    iiNumeroFrames = 3
    iiWidth = 20
    iiHeight = 40

    def __init__(self, pos=[]):
        self.Img = Animacao.cropImage(GameConfig.DIR_ANIMACOES + "MaisItem", self)
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
