import pygame
from GameConfig import GameConfig
from configparser import ConfigParser
import sys

class Estagio(object):

    LEVEL_FINAL = "fim"

    iiX = 0
    iiY = 0
    isLevelDir = 'levels/'
    isLevel = ''

    ivlevelOpcoes = ['nome', 'background', 'margin-top', 'margin-bottom']

    def __init__(self, level):
        self.isLevel = level
        self.iiProximoLevel = 0
        self.loadLevel(self.isLevel)
        # self.iiWidth = self.ioBg.get_width()

    def getBg(self):
        return self.ioBg

    def update(self):
        pass

    def getRect(self):
        return [self.iiX, self.iiY]

    def getLevel(self):
        return self.isLevel

    def scrollRight(self, ilScrollAmount):
        self.iiX -= ilScrollAmount

        if self.iiX * -1 < self.iiWidth - GameConfig.WIDTH:
            return True
        else:
            self.iiX = (self.iiWidth - GameConfig.WIDTH) * -1
            return False

    def scrollLeft(self, ilScrollAmount):
        self.iiX += ilScrollAmount
        if self.iiX > 0:
            self.iiX = 0
            return False
        else: return True

    def loadLevel(self, levelFile):
        level = ConfigParser()
        level.read(GameConfig.DIR_LEVEL + levelFile)
        self.nome = level.get('level', 'nome')
        bgFile = level.get('level', 'background')
        self.ioBg = pygame.image.load(GameConfig.DIR_BACKGROUND + bgFile)

        self.iiMarginLeft = int(level.get('level', 'margin-left'))
        self.iiMarginRight = int(level.get('level', 'margin-right'))
        self.iiMarginTop = int(level.get('level', 'margin-top'))
        self.iiMarginBottom = level.get('level', 'margin-bottom')
        self.iiProximoLevel = level.get('level', 'proximo')

        if self.iiMarginBottom == "bottom":
            self.iiMarginBottom = self.ioBg.get_height()
        else: self.iiMarginBottom = int(self.iiMarginBottom)

        self.iiWidth = self.ioBg.get_width()
        self.iiMarginRight = GameConfig.WIDTH - self.iiMarginRight

    def getMarginRight(self):
        return self.iiMarginRight

    def getMarginLeft(self):
        return self.iiMarginLeft

    def getMarginTop(self):
        return self.iiMarginTop

    def getMarginBottom(self):
        return self.iiMarginBottom

    def getProximoLevel(self):
        return self.iiProximoLevel

    def getWidth(self):
        return self.iiWidth

    def endLevel(self):
        return (self.iiX * -1 >= self.iiWidth - GameConfig.WIDTH)

    def getNome(self):
        return self.nome