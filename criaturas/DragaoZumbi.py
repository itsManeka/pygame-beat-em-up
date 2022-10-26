import pygame

from criaturas.Inimigo import Inimigo

class DragaoZumbi(Inimigo):

    def __init__(self, aoJogador):
        self.setJogador(aoJogador)
        self.setInimigo("dragao-zumbi", 'Dragão Zumbi', 100, 0, 10)
        self.setMaxDelayAtaque(200)
        self.setPontos(15)
        pass

    def update(self):
        self.perseguir()
        self.atacar()

        super(DragaoZumbi, self).update()
