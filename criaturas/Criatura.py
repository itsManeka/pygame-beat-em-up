import pygame
import sys, pdb
from animacoes.Animacao import Animacao
from projetil.Projetil import Projetil

from GameConfig import GameConfig

class Criatura(pygame.sprite.Sprite):
    iiHp = 0
    iiMp = 0
    iiAtk = 0
    iiDef = 0
    iiAgi = 0
    iiEsp = 0
    iiX = 0
    iiY = 0
    iiHeight = 180
    iiWidth = 180
    isNome = ''
    iiDirecaoX = 'R'
    iiImage = ''
    iiVelX = 1
    iiVelY = 1
    iiPersonagemRepo = "img/personagens/"
    iiMiscRepo = "img/misc/"
    iiCriatura = ''
    iiRunning = False
    iiImageState = []
    iiFrame = 0
    iiAtaqueUsado = 0
    iiTipoAnimacao = 0
    iiDelay = 120
    iiLastUpdate = 0
    ioVetorAtual = []
    ibTrocaImagemAutomatico = True
    ibVivo = True
    imgHP = None
    imgHPBar = None
    iiQtdProjeteis = 6

    def __init__(self, criatura, isNome = 'Personagem Desconhecido', iiHp=0, iiMp=0, iiAtk=0, iiDef=0, iiAgi=0, iiEsp=0, iiX=0, iiY=0, iiHeight=180, iiWidth=180, crop=None):
        pygame.sprite.Sprite.__init__(self)
        self.iiCriatura = criatura

        self.isNome     = isNome
        self.iiHp       = iiHp
        self.iiMp       = iiMp
        self.iiAtk      = iiAtk
        self.iiDef      = iiDef
        self.iiAgi      = iiAgi
        self.iiEsp      = iiEsp
        self.iiX        = iiX
        self.iiY        = iiY
        self.iiHeight   = iiHeight
        self.iiWidth    = iiWidth

        self.ibAtacando = False
        self.ibAtacandoProjetil = False
        self.ibExecutandoAnimacao = False

        self.paradoRVetor           = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/paradoR", self, crop)
        self.paradoLVetor           = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/paradoL", self, crop)
        self.ataque1LVetor          = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/ataque1L", self, crop)
        self.ataque1RVetor          = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/ataque1R", self, crop)
        self.correndoLVetor         = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/correndoL", self, crop)
        self.correndoRVetor         = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/correndoR", self, crop)
        self.ataqueProjetilLVetor   = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/ataque2L", self, crop)
        self.ataqueProjetilRVetor   = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/ataque2R", self, crop)
        self.atingidoLVetor         = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/atingidoL", self, crop)
        self.atingidoRVetor         = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/atingidoR", self, crop)
        self.derrotadoLVetor        = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/derrotadoL", self, crop)
        self.derrotadoRVetor        = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/derrotadoR", self, crop)
        self.dormindoLVetor         = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/dormindoL", self, crop)
        self.dormindoRVetor         = Animacao.cropImage(GameConfig.DIR_PERSONAGENS + criatura + "/dormindoR", self, crop)

        self.imgHP              = pygame.image.load(self.iiMiscRepo + "HP.png")
        self.imgHP              = pygame.transform.scale(self.imgHP, (1, 8))
        self.imgHPBar           = pygame.image.load(self.iiMiscRepo + "HPBar.png")
        self.imgHPBar           = pygame.transform.scale(self.imgHPBar, (self.iiHp, 8))
        self.imgQtdProjeteis    = pygame.image.load(self.iiMiscRepo + "SwordIcon.png")
        self.imgQtdProjeteis    = pygame.transform.scale(self.imgQtdProjeteis, (20, 20)) 

        self.projetil = None
        self.ioVetorAtual = self.paradoRVetor
        self.image = self.paradoRVetor[self.iiFrame]
        self.rect = self.image.get_rect()

    def getHeight(self):
        return self.rect.height

    def getWidth(self):
        return self.rect.width

    def getRight(self):
        return self.rect.right

    def getLeft(self):
        return self.rect.left

    def getTop(self):
        return self.rect.top

    def getBottom(self):
        return self.rect.bottom

    def setBottom(self, y):
        self.rect.bottom = y

    def getCenterX(self):
        return self.rect.centerx

    def getCenterY(self):
        return self.rect.centery

    def getX(self):
        return self.rect.x

    def getProjetil(self):
        return self.projetil

    def getCriatura(self):
        return self.iiCriatura

    def getNome(self):
        return self.isNome

    
    def getFrameAtaqueConsideravel(self):
        return (len(self.ioVetorAtual) / 3)

    def setProjetil(self, projetil):
        self.projetil = projetil

    def setX(self, x):
        if self.ibAtacando or not self.ibVivo:
            return

        if x > self.rect.x:
            self.iiDirecaoX = 'R'
            if self.ibTrocaImagemAutomatico:
                #self.__setImageFrame__(self.paradoRVetor)
                #self.__setImageFrame__(self.correndoRVetor)
                pass
        elif x < self.rect.x:
            self.iiDirecaoX = 'L'
            if self.ibTrocaImagemAutomatico:
                #self.__setImageFrame__(self.paradoLVetor)
                #self.__setImageFrame__(self.correndoLVetor)
                pass
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def increaseX(self, x):
        self.setX(self.rect.x + x)

    def setTrocaImagemAutomatico(self, abTrueFalse):
        self.ibTrocaImagemAutomatico = abTrueFalse

    def getTrocaImagemAutomatico(self):
        return self.ibTrocaImagemAutomatico

    def increaseY(self, y):
        self.setY(self.rect.y + y)

    def setRunning(self, trueOrFalse):
        self.iiRunning = trueOrFalse

        if self.ibAtacando or self.ibAtacandoProjetil or self.ibExecutandoAnimacao:
            return

        if trueOrFalse:
            if self.iiDirecaoX == 'L':
                self.iiImageState = self.correndoLVetor
            elif self.iiDirecaoX == 'R':
                self.iiImageState = self.correndoRVetor
        else:
            if self.iiDirecaoX == 'L':
                self.iiImageState = self.paradoLVetor
            elif self.iiDirecaoX == 'R':
                self.iiImageState = self.paradoRVetor
        self.__setImageFrame__(self.iiImageState)

    def updateCriatura(self):
        if self.ibAtacando or self.ibAtacandoProjetil:
            self.executaAtaque(self.iiAtaqueUsado, True)

        if self.ibExecutandoAnimacao:
            self.executaAnimacao(self.iiTipoAnimacao, True)

        self.__updateFrame__(pygame.time.get_ticks()) 

    def ataque(self, aiAtaqueIndice):
        lbPermiteAtaque = (self.isAtacando() and self.isFrameAtaqueConsideravel() or
                           not self.isAtacando())

        if lbPermiteAtaque:
            self.executaAtaque(aiAtaqueIndice) 

    def executaAtaque(self, aiAtaqueIndice, abPorAnimacao = False):
        if not abPorAnimacao:
            self.iiFrame = 0
            self.iiAtaqueUsado = aiAtaqueIndice

            if (aiAtaqueIndice != GameConfig.ATAQUE_PROJETIL): 
                self.ibAtacando = True
            else:
                self.ibAtacandoProjetil = True

        if (self.iiAtaqueUsado == GameConfig.ATAQUE_NORMAL):
            if (self.iiDirecaoX == 'L'):
                self.iiImageState = self.ataque1LVetor

            if (self.iiDirecaoX == 'R'):
                self.iiImageState = self.ataque1RVetor

        elif (self.iiAtaqueUsado == GameConfig.ATAQUE_FORTE):
            pass

        elif (self.iiAtaqueUsado == GameConfig.ATAQUE_PROJETIL):
            if (self.iiDirecaoX == 'L'):
                self.iiImageState = self.ataqueProjetilLVetor

            if (self.iiDirecaoX == 'R'):
                self.iiImageState = self.ataqueProjetilRVetor

        else:
            pass

        self.__setImageFrame__(self.iiImageState)

        if (self.iiFrame >= (len(self.ioVetorAtual) - 1)):
            self.ibAtacando = False
            self.ibAtacandoProjetil = False
            self.iiAtaqueUsado = 0
            self.iiFrame = 0

    def stopAtaque(self):
        self.ibAtacando = False
        self.iiAtaqueUsado = 0
        self.iiFrame = 0        

    def morre(self):
        self.ibVivo = False

    def getY(self):
        return self.rect.y

    def getImage(self):
        return self.image

    def getRect(self):
        return self.rect

    def getDirecao(self):
        return self.iiDirecaoX

    def isRunnig(self):
        return self.iiRunning

    def setImage(self, img):
        self.image = pygame.image.load(img).convert_alpha()

    def isVivo(self):
        return self.ibVivo

    def isFrameAtaqueConsideravel(self):
        return (self.iiFrame == self.getFrameAtaqueConsideravel())

    def isAtacando(self):
        return self.ibAtacando

    def getHP(self):
        return self.iiHp

    def getAtk(self):
        return self.iiAtk

    def danoHP(self, dano):
        self.executaAnimacao(GameConfig.TIPO_ANIMACAO_ATINGIDO)
        self.iiHp -= dano
        if self.iiHp <= 0:
            self.morre()

    def addHP(self, hp):
        self.iiHp += hp

    def desenhaDados(self, screen):
        #-- Qtd Projeteis
        liQtdProjeteisH = self.imgQtdProjeteis.get_rect().height
        liQtdProjeteisW = self.imgQtdProjeteis.get_rect().width
        liQtdProjeteisX = self.getLeft()
        liQtdProjeteisY = (self.getTop() - (liQtdProjeteisH * 2))
        
        screen.blit(self.imgQtdProjeteis, (liQtdProjeteisX, liQtdProjeteisY))

        #-- Barra de HP
        liHPBarX = (self.getCenterX() - (self.imgHPBar.get_rect().width / 2))
        liHPBarY = (liQtdProjeteisY - (self.imgHPBar.get_rect().height))

        screen.blit(self.imgHPBar, (liHPBarX, liHPBarY))
        for x in range(self.iiHp):
            screen.blit(self.imgHP, (x + liHPBarX, liHPBarY))

        #-- Textos
        if pygame.font:
            #-- Nome
            fonte       = pygame.font.Font(None, 15)
            texto       = fonte.render(self.isNome, 1, (255,255,255))
            posXTexto   = (self.getCenterX() - (texto.get_rect().width / 2))
            posYTexto   = (liHPBarY - (texto.get_rect().height))
            screen.blit(texto, (posXTexto, posYTexto))

            #-- Textos QtdProjeteis
            fonte       = pygame.font.Font(None, 20)
            texto       = fonte.render((str(self.iiQtdProjeteis) + 'x'), 1, (255,255,255))
            posXTexto   = (liQtdProjeteisX + liQtdProjeteisW) 
            posYTexto   = liQtdProjeteisY
            screen.blit(texto, (posXTexto, posYTexto))

    def __setImageFrame__(self, imageFrame):
        self.ioVetorAtual = imageFrame

        if(self.iiFrame >= (len(self.ioVetorAtual) - 1)) and not self.ibAtacando and not self.ibAtacandoProjetil and not self.ibExecutandoAnimacao:
            self.iiFrame = 0

        self.image = imageFrame[self.iiFrame]

    def __updateFrame__(self, time):
        if((time - self.iiLastUpdate) >= self.iiDelay):
            self.iiFrame += 1

            if (self.iiFrame >= len(self.ioVetorAtual)):
                self.iiFrame = 0

            self.iiLastUpdate = time

    def lancaProjetil(self, img, direcao):
        projetil = None

        if self.iiQtdProjeteis > 0:
            self.executaAtaque(GameConfig.ATAQUE_PROJETIL)
            projetil = Projetil(img + ".png",  (self.getCenterX(), self.getCenterY()), direcao)
            projetil.setAtk(self.iiAtk)
            projetil.setSpeedX(self.iiVelX * 1.5)
            self.iiQtdProjeteis -= 1

        return projetil

    def setAtk(self, atk):
        self.iiAtk = atk

    def setVelX(self, x):
        self.iiVelX = x

    def setVelY(self, y):
        self.iiVelY = y

    def getVelX(self):
        return self.iiVelX

    def getVelY(self):
        return self.iiVelY

    def adicionaProjetil(self):
        self.iiQtdProjeteis += 1

    def setHeight(self, height):
        self.iiHeight = height

    def setWidth(self, width):
        self.iiWidth = width

    def executaAnimacao(self, aiTipoAnimacao, abContinuaAnimacao=False):
        if not abContinuaAnimacao:
            self.iiFrame = 0
            self.iiTipoAnimacao = aiTipoAnimacao
            self.ibExecutandoAnimacao = True

        if (aiTipoAnimacao == GameConfig.TIPO_ANIMACAO_ATINGIDO):
            if (self.iiDirecaoX == 'L'):
                self.iiImageState = self.atingidoLVetor

            if (self.iiDirecaoX == 'R'):
                self.iiImageState = self.atingidoRVetor

        elif (aiTipoAnimacao == GameConfig.TIPO_ANIMACAO_DORMINDO):
            if (self.iiDirecaoX == 'L'):
                self.iiImageState = self.dormindoLVetor

            if (self.iiDirecaoX == 'R'):
                self.iiImageState = self.dormindoRVetor

        else:
            pass

        self.__setImageFrame__(self.iiImageState)

        if (self.iiFrame >= (len(self.ioVetorAtual) - 1)):
            if self.iiTipoAnimacao != GameConfig.TIPO_ANIMACAO_DORMINDO:
                self.ibExecutandoAnimacao = False
                self.iiTipoAnimacao = 0
            self.iiFrame = 0

    def stopAnimacao(self):
        self.ibExecutandoAnimacao = False
        self.iiTipoAnimacao = 0
        self.iiFrame = 0

    def getVetorDerrotado(self):
        if (self.iiDirecaoX == 'L'):
            vetor = self.derrotadoLVetor

        if (self.iiDirecaoX == 'R'):
            vetor = self.derrotadoRVetor

        return vetor