import pygame
import pdb

from criaturas.Criatura import Criatura
from GameConfig import GameConfig
from controles.Controle import Controle

class Jogador(Criatura):

    limitUp     = 400
    limitBottom = 600

    k_right         = set([pygame.K_RIGHT, pygame.K_l])
    k_left          = set([pygame.K_LEFT, pygame.K_h])
    k_up            = set([pygame.K_UP, pygame.K_k])
    k_down          = set([pygame.K_DOWN, pygame.K_j])
    k_pause         = [pygame.K_ESCAPE]
    k_z             = [pygame.K_z]
    k_projetil      = [pygame.K_x]
    k_newInimigo    = [pygame.K_v]

    analogico_y = 0
    analogico_x = 0

    def __init__(self, estagio, estado=None, personagem="templario-spartano", nome="Templario Spartano"):
        self.ioEstagio = estagio
        self.limitUp = self.ioEstagio.getMarginTop()
        self.setVelX(8)
        self.setVelY(3)

        self.controles = Controle()

        if estado: self.estado = estado

        Criatura.__init__(self, personagem, nome, 100, 0, 10, crop=(110, 110))
        pass

    def isDead(self):
        if self.getHP() <= 0:
            return True
        return False

    def getVelocidadeX(self):
        return self.getVelX()

    def getVelocidadeY(self):
        return self.getVelY()

    def getNewInimigo(self):
        return self.newInimigo

    def update(self, keys):
        self.newInimigo = None
        self.setProjetil(None)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    self.ataque(GameConfig.ATAQUE_NORMAL)
                if event.button == 1:
                    self.setProjetil(self.lancaProjetil('espada', self.getDirecao()))
                if event.button == 2:
                    print('X')
                if event.button == 3:
                    print('Y')
                if event.button == 6:
                    self.newInimigo = True
                if event.button == 7:
                    choice = self.estado.pause(keys, self.estado.screen)
                    if choice == "quit":
                        return choice
                print('btn:', event.button)
            if event.type == pygame.JOYAXISMOTION:
                self.analogico_x = self.controles.getControleX().get_axis(0)
                self.analogico_y = self.controles.getControleX().get_axis(1)
                
            if event.type == pygame.KEYDOWN:
                if event.key in self.k_pause:
                    choice = self.estado.pause(keys, self.estado.screen)
                    if choice == "quit":
                        return choice

                if event.key in self.k_z:
                    self.ataque(GameConfig.ATAQUE_NORMAL)

                if event.key in self.k_projetil:
                    self.ataque(GameConfig.ATAQUE_PROJETIL)
                    self.setProjetil(self.lancaProjetil('espada', self.getDirecao()))

                if event.key in self.k_newInimigo:
                    self.newInimigo = True

        lbPressed = set([i for i, x in enumerate(keys) if x==1])
        
        lcMovimentando, lbRunning = self.joyMovimento()

        if bool(self.k_right.intersection(lbPressed)):
            lbRunning = True
            if self.getRight() < self.ioEstagio.getMarginRight():
                self.increaseX(self.getVelX())
            else:
                lcMovimentando = 'R'
                if not self.ioEstagio.scrollRight(self.getVelX()):
                    lbRunning = False

        if bool(self.k_left.intersection(lbPressed)):
            lbRunning = True
            if self.getLeft() > self.ioEstagio.getMarginLeft():
                self.increaseX(self.getVelX() * -1)
            else:
                lcMovimentando = 'L'
                if not self.ioEstagio.scrollLeft(self.getVelX()):
                    lbRunning = False

        if bool(self.k_up.intersection(lbPressed)) and self.getBottom() > self.limitUp:
            self.increaseY(self.getVelY() * -1)
        if bool(self.k_down.intersection(lbPressed)) and self.getBottom() < self.limitBottom:
            self.increaseY(self.getVelY())

        self.setRunning(lbRunning)

        super(Jogador, self).update()

        return lcMovimentando

    def joyMovimento(self):
        lbRunning       = False
        lcMovimentando  = None

        #print('ax: ', self.analogico_x, ' ay: ', self.analogico_y)

        if self.analogico_x > 0:
            lbRunning = True
            if self.getRight() < self.ioEstagio.getMarginRight():
                self.increaseX(int(self.analogico_x) * 5)
            else:
                lcMovimentando = 'R'
                if not self.ioEstagio.scrollRight(int(self.analogico_x) * 5):
                    lbRunning = False

        if self.analogico_x < 0:
            lbRunning = True
            if self.getLeft() > self.ioEstagio.getMarginLeft():
                self.increaseX(int(self.analogico_x) * 5)
            else:
                lcMovimentando = 'L'
                if not self.ioEstagio.scrollLeft(int(self.analogico_x) * -5):
                    lbRunning = False

        if self.analogico_y < 0 and self.getBottom() > self.limitUp:
            self.increaseY(int(self.analogico_y) * 5)
        if self.analogico_y > 0 and self.getBottom() < self.limitBottom:
            self.increaseY(int(self.analogico_y) * 5)

        return lcMovimentando, lbRunning