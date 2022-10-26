import pygame
import pdb
from criaturas.Criatura import Criatura
from GameConfig import GameConfig

class Inimigo(Criatura):
    ibAcordado = False
    ibPodeAtacar = True
    ibPodeAtacarProjetil = False 
    iiMaxDelayAtaque = 30
    iiCountDelayAtaque = 0
    iiMaxDelayAtaqueProjetil = 30
    iiCountDelayAtaqueProjetil = 0
    ibRecebeuDano = False
    ibJogadorRecebeuDano = False
    iiPontos = 10

    def __init__(self, estagio):
        self.setProjetil(None)
        self.ioEstagio  = estagio
        pass

    def setAcordado(self, abAcordado):
        self.ibAcordado = abAcordado

    def setInimigo(self, criatura, asNome, aiHp=0, aiMp=0, aiAtk=0, aiDef=0, aiAgi=0, aiEsp=0, aiX=0, aiY=0, aiHeight=180, aiWidth=180, crop=None):
        Criatura.__init__(self, criatura, asNome, aiHp, aiMp, aiAtk, aiDef, aiAgi, aiEsp, aiX, aiY, aiHeight, aiWidth, crop)
        self.inicia()

    def setJogador(self, aoJogador):
        self.ioJogador = aoJogador

    def setMaxDelayAtaque(self, aiMaxDelay):
        self.iiMaxDelayAtaque = aiMaxDelay

    def setMaxDelayAtaqueProjetil(self, aiMaxDelay):
        self.iiMaxDelayAtaqueProjetil = aiMaxDelay

    def setPodeAtacar(self, abPodeAtacar):
        self.ibPodeAtacar = abPodeAtacar

    def setPontos(self, pontos):
        self.iiPontos = pontos

    def getPontos(self):
        return self.iiPontos

    def isAcordado(self):
        return self.ibAcordado

    def inicia(self):
        self.executaAnimacao(GameConfig.TIPO_ANIMACAO_DORMINDO)

    def update(self):
        if not self.isAcordado():
            self.verificaProximidadeJogador()

        self.verificaAtaque()
        self.verificaAtacouJogador()

        super(Inimigo, self).update()

    def verificaProximidadeJogador(self):
        lbProximoPelaDireita    = (self.ioJogador.getDirecao() == 'R' and
                                   self.ioJogador.getRight() >= self.getLeft() - 50)
        lbProximoPelaEsquerda   = (self.ioJogador.getDirecao() == 'L' and
                                   self.ioJogador.getLeft() <= self.getRight() + 50)
        if lbProximoPelaDireita or lbProximoPelaEsquerda:
            self.setAcordado(True)
            self.stopAnimacao()

    def verificaAtacouJogador(self):
        lbPosicaoYCorrespondente = (self.getCenterY() <= self.ioJogador.getBottom()) and (self.getCenterY() >= self.ioJogador.getTop())
        lbAtaqueDireita = (self.getRight() >= self.ioJogador.getLeft()) and (self.getDirecao() == 'R') and (self.getRight() <= self.ioJogador.getRight())
        lbAtaqueEsquerda = (self.getLeft() <= self.ioJogador.getRight()) and (self.getDirecao() == 'L') and (self.getLeft() >= self.ioJogador.getLeft())

        if not self.isAtacando():
            self.ibJogadorRecebeuDano = False

        if self.isAtacando() and not self.ibJogadorRecebeuDano:
            if lbPosicaoYCorrespondente and (lbAtaqueEsquerda or lbAtaqueDireita):
                self.ibJogadorRecebeuDano = True
                self.ioJogador.danoHP(self.getAtk())
                if (self.ioJogador.getHP() <= 0):
                    self.ioJogador.morre()

    def verificaAtaque(self):
        lbPosicaoYCorrespondente = (self.ioJogador.getCenterY() <= self.getBottom()) and (self.ioJogador.getCenterY() >= self.getTop())
        lbAtaqueDireita = (self.ioJogador.getRight() >= self.getLeft()) and (self.ioJogador.getDirecao() == 'R') and (self.ioJogador.getRight() <= self.getRight())
        lbAtaqueEsquerda = (self.ioJogador.getLeft() <= self.getRight()) and (self.ioJogador.getDirecao() == 'L') and (self.ioJogador.getLeft() >= self.getLeft())

        if not self.ioJogador.isAtacando():
            self.ibRecebeuDano = False

        if self.ioJogador.isAtacando() and not self.ibRecebeuDano and self.ioJogador.isFrameAtaqueConsideravel():
            if lbPosicaoYCorrespondente and (lbAtaqueEsquerda or lbAtaqueDireita):
                self.ibRecebeuDano = True
                self.ioJogador.stopAtaque()
                self.stopAnimacao()
                self.setAcordado(True)
                self.danoHP(self.ioJogador.getAtk())
                if (self.getHP() <= 0):
                    self.morre()

    def perseguir(self):
        lbRunning = False

        if self.isAcordado():
            velY = self.getVelY()

            diff = self.getBottom() - self.ioJogador.getBottom()

            # if diff >= self.getVelY(): self.setBottom(self.ioJogador.getBottom())

            if self.getRight() < (self.ioJogador.getLeft() + 50):
                self.setX(self.getX() + self.getVelX())
                lbRunning = True

            elif (self.getLeft() + 50) > self.ioJogador.getRight():
                self.setX(self.getX() - self.getVelX())
                lbRunning = True

            if self.getBottom() < self.ioJogador.getBottom():
                if diff > self.getVelY(): velY = 1
                self.setY(self.getY() + velY)

            elif self.getBottom() > self.ioJogador.getBottom():
                if diff < self.getVelY(): velY = -1
                self.setY(self.getY() - velY)


        self.setRunning(lbRunning)

    def atacar(self):
        if not self.isAcordado():
            return

        if (self.iiCountDelayAtaque >= self.iiMaxDelayAtaque):
            self.ibPodeAtacar = True

        if not self.ibPodeAtacar:
            self.iiCountDelayAtaque += 1

        if self.ibPodeAtacar:
            self.ataque(GameConfig.ATAQUE_NORMAL)
            self.ibPodeAtacar = False
            self.iiCountDelayAtaque = 0

    def atacarProjetil(self, imgProjetil='espada'):
        self.setProjetil(None)

        if not self.isAcordado():
            return

        if (self.iiCountDelayAtaqueProjetil >= self.iiMaxDelayAtaqueProjetil):
            self.ibPodeAtacarProjetil = True

        if not self.ibPodeAtacarProjetil:
            self.iiCountDelayAtaqueProjetil += 1

        if self.ibPodeAtacarProjetil:
            self.ibPodeAtacarProjetil = False
            self.setProjetil(self.lancaProjetil(imgProjetil, self.getDirecao()))
            self.iiCountDelayAtaqueProjetil = 0

    def zeraContadoresAtaque(self):
        self.iiCountDelayAtaque             = 0
        self.iiCountDelayAtaqueProjetil     = 0