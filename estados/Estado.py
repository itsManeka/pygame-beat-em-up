from estados.MenuEstado import MenuEstado
from estados.MenuPauseEstado import MenuPauseEstado
from estados.GameOverEstado import GameOverEstado
from GameConfig import GameConfig
import pygame
import pdb

class Estado(object):
    CORRENDO_BATENDO = 1
    MENU = 2
    SURVIVAL = 3
    GAME_OVER = 4
    ARCADE = 5

    estadoAtual = int

    stop = False

    def __init__(self, screen):
        self.screen = screen

    def setEstado(self, estadoId):
        self.estadoAtual = estadoId
        self.estado = {
            self.CORRENDO_BATENDO: lambda x: CorrendoBatendoEstado(self),
            self.MENU: lambda x: MenuEstado(self),
            self.SURVIVAL: lambda x: SurvivalEstado(self),
            self.GAME_OVER: lambda x: GameOverEstado(self),
            self.ARCADE: lambda x: ArcadeEstado(self)
        }[estadoId](estadoId)

    def update(self, key, screen):
        novoEstado = self.estado.update(key, screen)
        if (novoEstado == GameConfig.OUT_QUIT) or (novoEstado == GameConfig.OUT_END_ARCADE):
            return novoEstado
        elif novoEstado == GameConfig.OUT_GAME_OVER:
            return novoEstado
        elif isinstance(novoEstado, GameOverEstado):
            return novoEstado

        if novoEstado != None:
            self.estado = novoEstado
            novoEstado = None

    def pause(self, key, screen):
        paused = True
        menu = MenuPauseEstado(screen)
        while paused:
            out = menu.update(key, screen)
            if out == GameConfig.OUT_CONTINUE:
                paused = False
            if out == GameConfig.OUT_QUIT:
                return out
            pygame.display.flip()

    def goToMainMenu(self):
        return self.stop
