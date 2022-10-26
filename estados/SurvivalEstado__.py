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
import random
import timeit
import pygame
import pdb

class SurvivalEstado(object):

    def __init__(self, estado, estagio="rua.lvl", personagem="templario-spartano", nome="Templario Spartano"):
        #Titulo
        pygame.display.set_caption("DRAGON PUNCH! Uma aventura na terra dos dragões [Survival]")

        self.blit = {}

        self.estado = estado

        self.objetos            = pygame.sprite.Group()
        self.inimigos           = pygame.sprite.Group()
        self.animacoes          = pygame.sprite.Group()
        self.projeteis          = pygame.sprite.Group()
        self.projeteisInimigo   = pygame.sprite.Group()

        self.pontos     = 0

        self.font           = pygame.font.Font(None, 25)
        posXTexto           = 0
        posYTexto           = 0
        self.runningTime    = 0
        self.timer          = timeit.Timer()

        # estagio
        self.ioEstagio = Estagio(estagio)

        self.jogador = Jogador(self.ioEstagio, estado, personagem, nome)

        self.jogador.setAtk(30)
        self.jogador.setY(GameConfig.HEIGHT - self.jogador.getHeight())
        self.jogador.setX(self.ioEstagio.getMarginLeft() + 10)

        if personagem == "nigga_templario_spartano":
            self.jogador.setAtk(500)

        self.newInimigo()

    def update(self, key, screen):
        self.blit = {}
        screen.fill((0, 0, 0))
        jogadorOut = self.jogador.update(key)
        if jogadorOut == "quit":
            return jogadorOut
        elif jogadorOut == "game-over":
            return jogadorOut

        self.jogador.updateCriatura()

        if self.jogador.getNewInimigo():
            self.newInimigo()

        if random.randrange(500) == 1:
            self.newInimigo()

        if random.randrange(1000) == 1:
            self.newObjeto()

        if self.jogador.isDead():
            #-- armazena pontuacao
            arquivo = open('pontuacao.txt', 'r')
            texto = arquivo.readlines()
            data = datetime.now()
            data = str(data.day) + '/' + str(data.month) + '/' + str(data.year)
            texto.append('Nome: ' + str(self.jogador.getNome()) + ' | Pontos: ' + str(self.pontos) + '|  Data: ' + data + '\n')
            arquivo = open('pontuacao.txt', 'w')
            arquivo.writelines(texto)
            arquivo.close()

            #-- executa game over
            self.estado.setEstado(self.estado.GAME_OVER)
            self.estado.estado.setPontos(self.pontos)

        if self.jogador.getProjetil():
            self.projeteis.add(self.jogador.getProjetil())

        screen.blit(self.ioEstagio.getBg(), self.ioEstagio.getRect())

        if not self.jogador.getBottom() in self.blit.keys():
            self.blit[self.jogador.getBottom()] = []

        self.blit[self.jogador.getBottom()].append([self.jogador.getImage(), self.jogador.getRect()])

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
                self.pontos += 10
                self.animacoes.add(AnimacaoPronta((inimigo.getX(), inimigo.getY()), inimigo.getVetorDerrotado(), inimigo.getHeight(), inimigo.getWidth()))
                self.inimigos.remove(inimigo)
        
        for objeto in self.objetos:
            if self.jogador.isRunnig():
                if jogadorOut == 'R':
                    objeto.setX(objeto.getX() - self.jogador.getVelocidadeX())

                elif jogadorOut == 'L':
                    objeto.setX(objeto.getX() + self.jogador.getVelocidadeX())

        for y, objs in sorted(self.blit.items()):
            for obj in objs:
                screen.blit(obj[0], obj[1])

        for animacao in self.animacoes:
            screen.blit(animacao.getImage(), animacao.getRect())
            animacao.update(key)
            if animacao.isDone():
                self.animacoes.remove(animacao)

        for objeto in self.objetos:
            screen.blit(objeto.getImage(), objeto.getRect())
            objeto.update(key)

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
            print('colidiu objeto')
            print('tipo: ', objeto.getTipo())
            if objeto.getTipo() == GameConfig.TIPO_ITEM_VIDA:
                print('vida')
                self.jogador.addHP(10)
            else:
                print('item')
                self.jogador.adicionaProjetil()
                self.animacoes.add(MaisItem((self.jogador.getCenterX(), self.jogador.getCenterY())))

        self.jogador.desenhaDados(screen)

        tempoFont = self.font.render("Tempo percorrido: " + str("{:10.2f}".format(self.runningTime)), 1, (255,255,255))
        screen.blit(tempoFont, (10, 10))
        pontuacaoFont = self.font.render("Pontuacao:" + str(self.pontos), 1, (255,255,255))
        screen.blit(pontuacaoFont, (10, 23))
        self.runningTime += self.timer.timeit()

    def newInimigo(self):
        randinimigo = random.randint(1, 5)
        randinimigo = 4

        if randinimigo == 1:
            inimigo = DragaoZumbi(self.jogador)
            inimigo.setVelX(random.randint(2, 3))
            inimigo.setVelY(2)
        elif randinimigo == 2:
            inimigo = DragaoMorfeu(self.jogador)
            inimigo.setVelX(random.randint(2, 5))
            inimigo.setVelY(random.randint(2, 4))
        elif randinimigo == 3:
            inimigo = DragaoTartaruga(self.jogador)
            inimigo.setVelX(random.randint(1, 2))
            inimigo.setVelY(1)
        elif randinimigo == 4:
            inimigo = MiniDragao(self.jogador)
            inimigo.setVelX(5)
            inimigo.setVelY(5)
        else:
            inimigo = DragaoAquatico(self.jogador)
            inimigo.setVelX(random.randint(2, 5))
            inimigo.setVelY(random.randint(2, 3))

        x = random.randint(self.ioEstagio.getMarginLeft(), self.ioEstagio.getMarginRight())
        y = random.randint(self.ioEstagio.getMarginTop() - inimigo.getHeight(), self.ioEstagio.getMarginBottom() - inimigo.getHeight())
        inimigo.setY(y)
        inimigo.setX(x)

        inimigo.iiCountDelayAtaque = 0

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
