import pygame

from criaturas.Inimigo import Inimigo

class DragaoTartaruga(Inimigo):

    def __init__(self, aoJogador):
        self.setJogador(aoJogador)
        self.setInimigo("dragao-tartaruga", 'Dragão Tartaruga', 100, 0, 10)
        self.setMaxDelayAtaque(100)
        self.setMaxDelayAtaqueProjetil(200)
        self.setPontos(20)
        pass

    def update(self):
        self.perseguir()
        self.atacar()
        self.atacarProjetil()

        super(DragaoTartaruga, self).update()
