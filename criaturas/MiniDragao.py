import pygame

from criaturas.Inimigo import Inimigo

class MiniDragao(Inimigo):

    def __init__(self, aoJogador):
        self.setJogador(aoJogador)
        self.setInimigo("mini-dragao", 'Mini Dragão', 100, 0, 5, aiHeight=52, aiWidth=47, crop=(60,70))
        self.setMaxDelayAtaque(200)
        self.setMaxDelayAtaqueProjetil(200)
        self.setPontos(10)
        pass

    def update(self):
        self.perseguir()
       	self.atacarProjetil('fogo-toon')

        super(MiniDragao, self).update()
