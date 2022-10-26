from animacoes.Animacao import Animacao
from GameConfig import GameConfig
import pygame

class AnimacaoPronta(Animacao):
    iiDelay = 120

    def __init__(self, pos=[], imageVector=None, aiWidth=180, aiHeight=180):
        self.iiWidth        = aiWidth
        self.iiHeight       = aiHeight
        self.iiNumeroFrames = len(imageVector)

        self.Img = imageVector
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
