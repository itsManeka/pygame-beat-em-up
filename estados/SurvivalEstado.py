import pdb
import pygame
from estados.CorrendoBatendoEstado import CorrendoBatendoEstado
from GameConfig import GameConfig

class SurvivalEstado(CorrendoBatendoEstado):
    def __init__(self, estado, estagio="rua.lvl", personagem="templario-spartano", nome="Templario Spartano"):
        CorrendoBatendoEstado.__init__(self, estado, estagio, personagem, nome)
        self.setTituloTela("DRAGON PUNCH! Uma aventura na terra dos dragões [Survival]")

        self.setDadosJogador(30)
        if personagem == "nigga_templario_spartano":
            self.setDadosJogador(500)

        self.newInimigo(randomico=True)
        pass

    def update(self, key, screen):
        out = self.updateEstado(key, screen)
        if (out == GameConfig.OUT_QUIT):
            return out
        elif (out == GameConfig.OUT_GAME_OVER):
            return out
        
        #-- Randomicos
        self.randInimigo()
        self.randObjeto()

        #-- Desenha dados
        self.desenhaDadosPontuacao(screen)
        self.desenhaDadosTempo(screen)