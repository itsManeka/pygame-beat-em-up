import pygame

class Objeto(pygame.sprite.Sprite):

    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()

    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def increaseX(self, x):
        self.setX(self.rect.x + x)

    def getImg(self):
        return self.image

    def getRect(self):
        return self.rect

    def getLeft(self):
        return self.getX()
