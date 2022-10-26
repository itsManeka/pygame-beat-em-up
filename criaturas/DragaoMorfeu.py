import pygame

from criaturas.Inimigo import Inimigo

class DragaoMorfeu(Inimigo):
	def __init__(self, aoJogador):
		self.setJogador(aoJogador)
		self.setInimigo("dragao-morfeu", 'Dragão Morfeu', 100, 0, 10)
		self.setMaxDelayAtaque(200)
		self.setPontos(15)
		pass

	def update(self):
		self.perseguir()
		self.atacar()

		super(DragaoMorfeu, self).update()
