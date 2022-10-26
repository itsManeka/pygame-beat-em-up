from Objeto import Objeto
from GameConfig import GameConfig
import pygame

class Projetil(Objeto):

    speedX = 1

    def __init__(self, img, xy, direcao='R'):

        self.direcao = direcao
        Objeto.__init__(self, GameConfig.DIR_PROJETEIS + img)

        self.setX(xy[0])
        self.setY(xy[1])

        self.rect.x = xy[0]
        self.rect.y = xy[1]

        if direcao == 'L':
            self.speedX *= -1
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self):
        self.increaseX(self.speedX)

    def setSpeedX(self, x):
        if self.direcao == 'L':
            x *= -1
        self.speedX = x

    def getRect(self):
        return self.image.get_rect()

    def getImage(self):
        return self.image

    def setAtk(self, atk):
        self.atk = atk

    def getAtk(self):
        return self.atk
