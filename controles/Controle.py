import pygame
import pdb

class Controle(object):

	def __init__(self):
		self.controles = []

		self.__iniciaControle__()
		pass

	def __iniciaControle__(self):

		#Para todos os controles conectados
		print('count: ', pygame.joystick.get_count())
		for i in range(0, pygame.joystick.get_count()):
			#Cria objeto do controle
			self.controles.append(pygame.joystick.Joystick(i))

			#inicializa os controles (-1 faz um laço para sempre)
			self.controles[-1].init()

			#informa qual controle está sendo usado
			print("Joystick detectado: ", self.controles[-1].get_name())

	def getControles(self):
		return self.controles

	def getControleX(self, controle = 0):
		return self.controles[controle]