import pygame
import sys
from estados.MenuEstado import MenuEstado

class GameOverEstado(object):

    def __init__(self, estado):
        #Titulo
        pygame.display.set_caption("Game Over")
        self.estado = estado
        self.font1 = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 30)
        self.gameOverFont= self.font1.render("GameOver", 1, (255, 0, 0))

    def setPontos(self, pontos):
        #arquivo =  open("pontuacao.txt", 'r')
        #self.pontos = for line in arquivo.readlines():
        self.pontos = []
        for row in open("pontuacao.txt", 'r').readlines():
            self.pontos.append(row)
        #self.pontos = pontos
        #self.pontuacaoFont = self.font2.render(str(self.pontos) + " pontos", 1, (255, 255, 255))
        #self.pontuacaoFont = self.font2.render(str(self.pontos), 1, (255, 255, 255))

    def update(self, key, screen):
        screen.fill((5, 5, 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return MenuEstado(self.estado)

        widthBase = (screen.get_width() -
                     self.gameOverFont.get_width()) / 2
        heightBase = (screen.get_height() -
                      self.gameOverFont.get_height() - 50) / 2

        screen.blit(self.gameOverFont, ((screen.get_width() -
                     self.gameOverFont.get_width()) / 2, heightBase))

        count = 0
        for ponto in self.pontos:
            count += 50
            self.pontuacaoFont = self.font2.render(str(ponto.strip('\n')), 1, (255, 255, 255))
            screen.blit(self.pontuacaoFont, ((screen.get_width() -
                        self.pontuacaoFont.get_width()) / 2, heightBase + count))
