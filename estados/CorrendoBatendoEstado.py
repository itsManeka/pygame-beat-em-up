from criaturas.Jogador import Jogador
from datetime import datetime
from criaturas.DragaoZumbi import DragaoZumbi
from criaturas.DragaoMorfeu import DragaoMorfeu
from criaturas.DragaoAquatico import DragaoAquatico
from criaturas.DragaoTartaruga import DragaoTartaruga
from criaturas.MiniDragao import MiniDragao
from GameConfig import GameConfig
from estagio.Estagio import Estagio
from estados.MenuPauseEstado import MenuPauseEstado
from animacoes.Fumaca import Fumaca
from animacoes.Barril import Barril
from animacoes.MaisItem import MaisItem
from animacoes.Comida import Comida
from animacoes.AnimacaoPronta import AnimacaoPronta
from animacoes.Seta import Seta
import random
import timeit
import pygame
import pdb

class CorrendoBatendoEstado(object):
    font                = pygame.font.Font(None, 25)
    pontos              = 0
    runningTime         = 0
    animacaoSeta        = Seta(((GameConfig.WIDTH - 180), GameConfig.CENTER - 100)) 

    def __init__(self, estado, estagio="rua.lvl", personagem="templario-spartano", nome="Templario Spartano"):
        self.timer      = timeit.Timer()
        self.blit       = {}
        self.estado     = estado
        self.ioEstagio  = Estagio(estagio)
        self.jogador    = Jogador(self.ioEstagio, estado, personagem, nome)

        self.objetos             = pygame.sprite.Group()
        self.inimigos            = pygame.sprite.Group()
        self.animacoes           = pygame.sprite.Group()
        self.projeteis           = pygame.sprite.Group()
        self.projeteisInimigo    = pygame.sprite.Group()

        self.jogador.setY(GameConfig.HEIGHT - self.jogador.getHeight())
        self.jogador.setX(self.ioEstagio.getMarginLeft() + 10)

 
    def setDadosJogador(self, atk=30):
        self.jogador.setAtk(atk)

    def getEstagio(self):
        return self.ioEstagio

    def getInimigos(self):
        return self.inimigos

    def getJogador(self):
        return self.jogador

    def getEstado(self):
        return self.estado

    def setTituloTela(self, asTitulo="DRAGON PUNCH! Uma aventura na terra dos dragões"):
        pygame.display.set_caption(asTitulo)

    def limpaBlit(self):
        self.blit = {}

    def salvaPotucaoArquivo(self):
        arquivo = open(GameConfig.DIR_ARQUIVO_PONTUACAO, GameConfig.ARQUIVO_READ)
        texto = arquivo.readlines()
        data = datetime.now()
        data = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
        texto.append('Nome: ' + str(self.jogador.getNome()) + ' | Pontos: ' + str(self.pontos) + '|  Data: ' + data + '\n')
        arquivo = open(GameConfig.DIR_ARQUIVO_PONTUACAO, GameConfig.ARQUIVO_WRITE)
        arquivo.writelines(texto)
        arquivo.close()

    def verificaZerouInimigos(self):
        return (len(self.inimigos) == 0)

    def proximoEstagio(self, screen, key): 
        screen.blit(self.animacaoSeta.getImage(), self.animacaoSeta.getRect())
        self.animacaoSeta.update(key)

        if self.ioEstagio.endLevel():
            if self.ioEstagio.getProximoLevel() != self.ioEstagio.LEVEL_FINAL:
                return GameConfig.OUT_PROXIMO_LEVEL
            else:
                return GameConfig.OUT_END_ARCADE

    def executaGameOver(self):
        self.estado.setEstado(self.estado.GAME_OVER)
        self.estado.estado.setPontos(self.pontos)

    def randInimigo(self, rand=500):
        if random.randrange(rand) == 1:
            self.newInimigo(randomico=True)

    def randObjeto(self, rand=1000):
        if random.randrange(rand) == 1:
            self.newObjeto()

    def desenhaDadosTempo(self, screen):
        tempoFont = self.font.render("Tempo percorrido: " + str("{:10.2f}".format(self.runningTime)), 1, (255,255,255))
        screen.blit(tempoFont, (10, 10))
        self.runningTime += self.timer.timeit()

    def desenhaDadosPontuacao(self, screen):
        pontuacaoFont = self.font.render("Pontuacao:" + str(self.pontos), 1, (255,255,255))
        screen.blit(pontuacaoFont, (10, 23))

    def acoesJogador(self, key, screen):
        jogadorOut = self.jogador.update(key)

        self.jogador.updateCriatura()
        self.jogador.desenhaDados(screen)

        if self.jogador.getNewInimigo():
            self.newInimigo(randomico=True)

        if self.jogador.getProjetil():
            self.projeteis.add(self.jogador.getProjetil())

        if not self.jogador.getBottom() in self.blit.keys():
            self.blit[self.jogador.getBottom()] = []

        self.blit[self.jogador.getBottom()].append([self.jogador.getImage(), self.jogador.getRect()])

        if self.jogador.isDead():
            self.salvaPotucaoArquivo()
            self.executaGameOver()

        return jogadorOut

    def acoesInimigos(self, screen, jogadorOut):
        for inimigo in self.inimigos:
            if self.jogador.isRunnig():
                if jogadorOut == 'R':
                    inimigo.setTrocaImagemAutomatico(False)
                    inimigo.setX(inimigo.getX() - self.jogador.getVelocidadeX())
                    inimigo.setTrocaImagemAutomatico(True)

                elif jogadorOut == 'L':
                    inimigo.setTrocaImagemAutomatico(False)
                    inimigo.setX(inimigo.getX() + self.jogador.getVelocidadeX())
                    inimigo.setTrocaImagemAutomatico(True)

            inimigo.update()
            inimigo.updateCriatura()
            inimigo.desenhaDados(screen)

            if inimigo.getProjetil():
                self.projeteisInimigo.add(inimigo.getProjetil())

            if not inimigo.getBottom() in self.blit.keys():
                self.blit[inimigo.getBottom()] = []

            self.blit[inimigo.getBottom()].append([inimigo.getImage(), inimigo.getRect()])

            if not inimigo.isVivo(): # verifica se o inimigo morreu
                self.pontos += inimigo.getPontos()
                self.animacoes.add(AnimacaoPronta((inimigo.getX(), inimigo.getY()), inimigo.getVetorDerrotado(), inimigo.getHeight(), inimigo.getWidth()))
                self.inimigos.remove(inimigo)

    def ObjetosEColisoes(self, screen, key, jogadorOut):
        for objeto in self.objetos:
            if self.jogador.isRunnig():
                if jogadorOut == 'R':
                    objeto.setX(objeto.getX() - self.jogador.getVelocidadeX())

                elif jogadorOut == 'L':
                    objeto.setX(objeto.getX() + self.jogador.getVelocidadeX())

            screen.blit(objeto.getImage(), objeto.getRect())
            objeto.update(key)

        for y, objs in sorted(self.blit.items()):
            for obj in objs:
                screen.blit(obj[0], obj[1])

        for animacao in self.animacoes:
            screen.blit(animacao.getImage(), animacao.getRect())
            animacao.update(key)
            if animacao.isDone():
                self.animacoes.remove(animacao)

        for projetil in self.projeteis:
            screen.blit(projetil.getImg(), (projetil.getX(), projetil.getY()))
            projetil.update()

            collide = pygame.sprite.spritecollide(projetil, self.inimigos,
                    False, pygame.sprite.collide_mask)

            for c in collide:
                if c.isAcordado():
                    c.setAcordado(True)

                c.danoHP(projetil.getAtk())
                self.projeteis.remove(projetil)
                continue

            if projetil.getLeft() > GameConfig.WIDTH:
                self.projeteis.remove(projetil)

        for projetil in self.projeteisInimigo:
            screen.blit(projetil.getImg(), (projetil.getX(), projetil.getY()))
            projetil.update()
        
            if projetil.getLeft() > GameConfig.WIDTH:
                self.projeteisInimigo.remove(projetil)

        lbColide        = pygame.sprite.spritecollide(self.jogador, self.projeteisInimigo,  False, pygame.sprite.collide_mask)
        lbColideObjeto  = pygame.sprite.spritecollide(self.jogador, self.objetos, True, pygame.sprite.collide_mask)

        if lbColide:
            self.jogador.danoHP(projetil.getAtk())
            self.projeteisInimigo.remove(projetil)

        if lbColideObjeto:
            if objeto.getTipo() == GameConfig.TIPO_ITEM_VIDA:
                self.jogador.addHP(10)
            else:
                self.jogador.adicionaProjetil()
                self.animacoes.add(MaisItem((self.jogador.getCenterX(), self.jogador.getCenterY())))

    def updateEstado(self, key, screen):
        self.limpaBlit()
        screen.fill((0, 0, 0))
        screen.blit(self.ioEstagio.getBg(), self.ioEstagio.getRect())

        jogadorOut = self.acoesJogador(key, screen)
        if (jogadorOut == GameConfig.OUT_QUIT):
            return jogadorOut
        elif (jogadorOut == GameConfig.OUT_GAME_OVER):
            return jogadorOut

        self.acoesInimigos(screen, jogadorOut)
        self.ObjetosEColisoes(screen, key, jogadorOut)

    def newInimigo(self, tipoInimigo=1, x=0, y=0, randomico=False):
        if randomico:
            tipoInimigo = random.randint(1, 5)

        if tipoInimigo == GameConfig.TIPO_INIMIGO_DRAGAO_ZUMBI:
            inimigo = DragaoZumbi(self.jogador)

        elif tipoInimigo == GameConfig.TIPO_INIMIGO_DRAGAO_MORFEU:
            inimigo = DragaoMorfeu(self.jogador)

        elif tipoInimigo == GameConfig.TIPO_INIMIGO_DRAGAO_TARTARUGA:
            inimigo = DragaoTartaruga(self.jogador)

        elif tipoInimigo == GameConfig.TIPO_INIMIGO_MINI_DRAGAO:
            inimigo = MiniDragao(self.jogador)

        elif tipoInimigo == GameConfig.TIPO_INIMIGO_DRAGAO_AQUATICO:
            inimigo = DragaoAquatico(self.jogador)

        x = random.randint(self.ioEstagio.getMarginLeft(), self.ioEstagio.getMarginRight())
        y = random.randint(self.ioEstagio.getMarginTop() - inimigo.getHeight(), self.ioEstagio.getMarginBottom() - inimigo.getHeight())

        inimigo.setY(y)
        inimigo.setX(x)

        inimigo.zeraContadoresAtaque()
        self.inimigos.add(inimigo)

    def newObjeto(self):
        randObjeto = random.randint(1, 2) 

        x = random.randint(self.ioEstagio.getMarginLeft(), self.ioEstagio.getMarginRight())
        y = random.randint(self.ioEstagio.getMarginTop() - 35, self.ioEstagio.getMarginBottom() - 35)
        
        if randObjeto == 1: 
            self.objetos.add(Barril((x, y)))
        else:
            self.objetos.add(Comida((x, y)))

    def gameOver(self, screen):
        screen.fill((11, 11, 11))