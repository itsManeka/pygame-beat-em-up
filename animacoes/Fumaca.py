from animacoes.Animacao import Animacao
from GameConfig import GameConfig
import pygame

class Fumaca(Animacao):
    iiDelay = 120
    iiNumeroFrames = 4
    iiWidth = 180
    iiHeight = 180

    def __init__(self, pos=[]):
        self.Img = Animacao.cropImage(GameConfig.DIR_ANIMACOES + "fumaca", self)
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
