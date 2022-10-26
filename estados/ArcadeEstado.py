import pdb
import pygame
from estados.CorrendoBatendoEstado import CorrendoBatendoEstado
from GameConfig import GameConfig

class ArcadeEstado(CorrendoBatendoEstado):
    def __init__(self, estado, estagio="rua.lvl", personagem="templario-spartano", nome="Templario Spartano"):
        CorrendoBatendoEstado.__init__(self, estado, estagio, personagem, nome)
        self.setTituloTela("DRAGON PUNCH! - [" + self.getEstagio().getNome() + "]")

        self.addInimigoPorLevel()
        pass

    def update(self, key, screen):
        out = self.updateEstado(key, screen)
        if (out == GameConfig.OUT_QUIT):
            return out
        elif (out == GameConfig.OUT_GAME_OVER):
            return out

        #-- Desenha dados
        self.desenhaDadosPontuacao(screen)

        #-- Verifica final estagio
        if self.verificaZerouInimigos():
            out = self.proximoEstagio(screen, key)
            if (out == GameConfig.OUT_PROXIMO_LEVEL):
                return ArcadeEstado(self.getEstado(),
                                           self.getEstagio().getProximoLevel(),
                                           self.getJogador().getCriatura(),
                                           self.getJogador().getNome()) 
            elif (out == GameConfig.OUT_END_ARCADE):
                return out

    def addInimigoPorLevel(self):
        if self.getEstagio().getLevel() == 'rua.lvl' or self.getEstagio().getLevel == 'calabouco.lvl':
            liTipoInimigo = GameConfig.TIPO_INIMIGO_DRAGAO_ZUMBI
        elif self.getEstagio().getLevel() == 'selva.lvl':
            liTipoInimigo = GameConfig.TIPO_INIMIGO_DRAGAO_MORFEU
        elif self.getEstagio().getLevel() == 'dragons1.lvl' or self.getEstagio().getLevel == 'dragons2.lvl':
            liTipoInimigo = GameConfig.TIPO_INIMIGO_DRAGAO_TARTARUGA
        else:
            liTipoInimigo = GameConfig.TIPO_INIMIGO_DRAGAO_AQUATICO

        self.newInimigo(liTipoInimigo)