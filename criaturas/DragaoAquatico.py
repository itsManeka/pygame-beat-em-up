import pygame

from criaturas.Inimigo import Inimigo

class DragaoAquatico(Inimigo):

    def __init__(self, aoJogador):
        self.setJogador(aoJogador)
        self.setInimigo("dragao-aquatico", 'Dragão Aquático', 100, 0, 10)
        self.setMaxDelayAtaque(200)
        self.setPontos(10)
        pass

    def update(self):
        self.perseguir()
        self.atacar()

        super(DragaoAquatico, self).update()
