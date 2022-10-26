from criaturas.Jogador import Jogador
from criaturas.DragaoZumbi import DragaoZumbi
from criaturas.DragaoMorfeu import DragaoMorfeu
from criaturas.DragaoAquatico import DragaoAquatico
from criaturas.DragaoTartaruga import DragaoTartaruga
from GameConfig import GameConfig
from estagio.Estagio import Estagio
from estados.MenuPauseEstado import MenuPauseEstado
from animacoes.Fumaca import Fumaca
from animacoes.Seta import Seta
import random
import timeit
import pygame
import pdb

class ArcadeEstado(object):
    def __init__(self, estado, estagio="rua.lvl", personagem="templario-spartano", nome="Templario Spartano"):
        #Titulo
        pygame.display.set_caption("DRAGON PUNCH! Uma aventura na terra dos dragões [Arcade]")

        self.blit = {}

        self.estado     = estado

        self.inimigos           = pygame.sprite.Group()
        self.animacoes          = pygame.sprite.Group()
        self.projeteis          = pygame.sprite.Group()
        self.projeteisInimigo   = pygame.sprite.Group()

        self.animacaoSeta = Seta(((GameConfig.WIDTH - 180), GameConfig.CENTER - 100)) 

        self.pontos     = 0

        self.font       = pygame.font.Font(None, 25)
        posXTexto       = 0
        posYTexto       = 0

        # estagio
        self.ioEstagio = Estagio(estagio)

        self.jogador = Jogador(self.ioEstagio, estado, personagem, nome)

        self.jogador.setY(GameConfig.HEIGHT - self.jogador.getHeight())
        self.jogador.setX(self.ioEstagio.getMarginLeft() + 10)

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

        if self.jogador.isDead():
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
                self.animacoes.add(Fumaca((inimigo.getX(), inimigo.getY())))
                self.inimigos.remove(inimigo)

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

        lbColide = pygame.sprite.spritecollide(self.jogador, self.projeteisInimigo,  False, pygame.sprite.collide_mask)

        if lbColide:
            self.jogador.danoHP(projetil.getAtk())
            self.projeteisInimigo.remove(projetil)

        self.jogador.desenhaDados(screen)

        pontuacaoFont = self.font.render("Pontuacao:" + str(self.pontos), 1, (255,255,255))
        screen.blit(pontuacaoFont, (10, 23))

        if (len(self.inimigos) == 0):
            screen.blit(self.animacaoSeta.getImage(), self.animacaoSeta.getRect())
            self.animacaoSeta.update(key)

            if self.ioEstagio.endLevel():
                if self.ioEstagio.getProximoLevel() != 'fim':
                    return ArcadeEstado(self.estado, self.ioEstagio.getProximoLevel(), self.jogador.getCriatura(), self.jogador.getNome())
                else:
                    return 'end-arcade'
        
    def newInimigo(self):
        for inimigos in range(0,1):
            if self.ioEstagio.getLevel() == 'rua.lvl' or self.ioEstagio.getLevel == 'calabouco.lvl':
                inimigo = DragaoZumbi(self.jogador)
            elif self.ioEstagio.getLevel() == 'selva.lvl':
                inimigo = DragaoMorfeu(self.jogador)
            elif self.ioEstagio.getLevel() == 'dragons1.lvl' or self.ioEstagio.getLevel == 'dragons2.lvl':
                inimigo = DragaoTartaruga(self.jogador) 
            else:
                inimigo = DragaoAquatico(self.jogador)

            x = random.randint(self.ioEstagio.getMarginLeft(), self.ioEstagio.getMarginRight())
            y = random.randint(self.ioEstagio.getMarginTop() - inimigo.getHeight(), self.ioEstagio.getMarginBottom() - inimigo.getHeight())
            inimigo.setY(y)
            inimigo.setX(x)
            self.inimigos.add(inimigo)

    def gameOver(self, screen):
        screen.fill((11, 11, 11))