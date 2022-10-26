import pygame
from os import path
from GameConfig import GameConfig

class Animacao(pygame.sprite.Sprite):

    iiLastUpdate = 0
    iiFrame = 0
    iiNumeroFrames = 4
    done = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()

    @staticmethod
    def cropImage(imgFile, obj, crop=None):
        imagePath =  (imgFile + GameConfig.IMAGE_TYPE)
        imgVector = []

        if not path.exists(imagePath):
            print('Não foi possível encontrar o arquivo ', imagePath)

        else:
            img = pygame.image.load(imagePath)
            obj.iiNumeroFrames = int(img.get_width() / obj.iiWidth)
            for i in range(obj.iiNumeroFrames):
                imgCropped = img.subsurface(i*obj.iiWidth, 0, obj.iiWidth, obj.iiHeight)
                if crop:
                    imgCropped = pygame.transform.scale(imgCropped, (crop[0], crop[1]))
                imgVector.append(imgCropped)

        return imgVector

    def update(self):
        pass

    def __updateFrame__(self, time):
        if((time - self.iiLastUpdate) >= self.iiDelay):
            self.iiFrame += 1

            if (self.iiFrame >= self.iiNumeroFrames):
                self.done = True
                self.iiFrame = 0
                
            self.image = self.Img[self.iiFrame]
            self.iiLastUpdate = time

    def getRect(self):
        return self.rect

    def isDone(self):
        return self.done
