import sys

import pygame
from estados.GameOverEstado import GameOverEstado
from estados.Estado import Estado
from GameConfig import GameConfig
import pdb

class Game(object):
    estadoAtual = int

    def __init__(self):
        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode((GameConfig.WIDTH, GameConfig.HEIGHT))
        icon = pygame.image.load("img/icon/icon.png")
        pygame.display.set_icon(icon)

        self.estado = Estado(self.screen)
        self.estado.setEstado(Estado.MENU)

        self.clock = pygame.time.Clock()

    def run(self):
        # iniciando loop principal
        while self.running:
            self.clock.tick(400)

            key = pygame.key.get_pressed()
            estadoOut = self.estado.update(key, self.screen)

            if estadoOut:
                self.estado = Estado(self.screen)
                if estadoOut == GameConfig.OUT_MENU:
                    self.estado.setEstado(Estado.MENU)
                elif (estadoOut == GameConfig.OUT_GAME_OVER) or (estadoOut == GameConfig.OUT_END_ARCADE):
                    self.estado.setEstado(Estado.GAME_OVER)
                elif estadoOut == GameConfig.OUT_PROXIMO_LEVEL:
                    self.estado.setEstado(Estado.ARCADE)
                elif isinstance(estadoOut, GameOverEstado):
                    self.estado.estado = estadoOut
                else: self.estado.setEstado(Estado.MENU)

            pygame.display.flip()
        sys.exit()
