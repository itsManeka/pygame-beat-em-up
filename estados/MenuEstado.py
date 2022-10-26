from menu.Menu import Menu
from estados.SurvivalEstado import SurvivalEstado
from GameConfig import GameConfig
from estados.ArcadeEstado import ArcadeEstado
import pygame
import sys
import pdb

class MenuEstado(object):

    ibArcade = False

    k_up = [pygame.K_UP, pygame.K_k]
    k_down = [pygame.K_DOWN, pygame.K_j]
    k_confirm = [pygame.K_RETURN]
    k_quit = [pygame.K_ESCAPE]

    def __init__(self, estado):
        self.estado = estado
        self.estagio = None

        self.setMenuPrincipal()

        pygame.display.update()

    def update(self, key, screen):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.key in self.k_up:
                    self.mainMenu.draw(-1)
                if event.key in self.k_down:
                    self.mainMenu.draw(1)

                if self.menuAtual == "main":
                    self.mainMenuAction(event)

                elif self.menuAtual == "estagios":
                    self.estagioMenuAction(event)

                elif self.menuAtual == "personagens":
                    personagem = self.personagemMenuAction(event)
                    if personagem: return personagem                        

                pygame.display.update()
            elif event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
        return None


    def mainMenuAction(self, event):
        if event.key in self.k_confirm:
            if self.mainMenu.get_position() == 0: # Arcade
                self.ibArcade = True
                self.setPersonagensMenu()

            elif self.mainMenu.get_position() == 1: # Survival
                self.ibArcade = False
                self.setEstagioMenu()

            elif self.mainMenu.get_position() == 2: # tela cheia
                pygame.display.toggle_fullscreen()
                GameConfig.FULLSCREEN = True

            elif self.mainMenu.get_position() == 3: # Quit
                pygame.display.quit()
                sys.exit()

    def personagemMenuAction(self, event):
        if event.key in self.k_confirm:
            if self.mainMenu.get_position() == 0: # templario spartano
                if self.ibArcade:
                    return ArcadeEstado(self.estado, personagem="templario-spartano", nome="Templario Spartano")
                else:
                    return SurvivalEstado(self.estado, self.estagio, "templario-spartano", "Templario Spartano")

            elif self.mainMenu.get_position() == 1: # jesus-karateka
                if self.ibArcade:
                    return ArcadeEstado(self.estado, personagem="jesus-karateka", nome="Jesus Karateka")
                else:
                    return SurvivalEstado(self.estado, self.estagio, "jesus-karateka", "Jesus Karateka")

            elif self.mainMenu.get_position() == 4: # dark templario spartano
                if self.ibArcade:
                    return ArcadeEstado(self.estado, personagem="nigga_templario_spartano", nome="Nigga Templario Spartano")
                else:
                    return SurvivalEstado(self.estado, self.estagio, "nigga_templario_spartano", "Nigga Templario Spartano")

            elif self.mainMenu.get_position() == 5: #Voltar
                if self.ibArcade:
                    self.setMenuPrincipal()
                else:
                    self.setEstagioMenu()

    def estagioMenuAction(self, event):
        if event.key in self.k_confirm:
            if self.mainMenu.get_position() == 0: #Rua
                self.estagio = "rua.lvl" 

            elif self.mainMenu.get_position() == 1: #Selva
                self.estagio = "selva.lvl"

            elif self.mainMenu.get_position() == 2: #Lago
                self.estagio = "lago.lvl"

            elif self.mainMenu.get_position() == 3: #Calabouço
                self.estagio = "calabouco.lvl"

            elif self.mainMenu.get_position() == 4: #Dragons Stage 1
                self.estagio = "dragons1.lvl"

            elif self.mainMenu.get_position() == 5: #Dragons Stage 2
                self.estagio = "dragons2.lvl"

            elif self.mainMenu.get_position() == 6: #Voltar
                self.setMenuPrincipal()
                return

            self.setPersonagensMenu()

    def setPersonagensMenu(self):
        #Titulo
        pygame.display.set_caption("Personagens")

        self.menuAtual = "personagens"
        self.mainMenu = Menu()
        self.mainMenu.init(['Templario Spartano', 'Jesus Karateka', 'Cowboy From Hell', 'Mendigo Guitarrista', 'Nigga Templario Spartano', 'Voltar'], self.estado.screen)
        self.estado.screen.fill((51,51,51))

        self.mainMenu.draw()

        pygame.key.set_repeat(199,69)
        pygame.display.flip()

    def setEstagioMenu(self):
        #Titulo
        pygame.display.set_caption("Estagios")

        self.menuAtual = "estagios"
        self.mainMenu = Menu()
        self.mainMenu.init(['Rua', 'Selva', 'Lago', 'Calabouço', 'Dragons Stage 1', 'Dragons Stage 2', 'Voltar'], self.estado.screen)
        self.estado.screen.fill((51,51,51))

        self.mainMenu.draw()

        pygame.key.set_repeat(199, 69)
        pygame.display.flip()

    def setMenuPrincipal(self):
        #Titulo
        pygame.display.set_caption("Menu principal")

        self.menuAtual = "main"
        self.mainMenu = Menu()
        self.mainMenu.init(['Arcade', 'Survival', 'Tela cheia/Janela', 'Fechar'], self.estado.screen)
        self.estado.screen.fill((51,51,51))

        self.mainMenu.draw()

        pygame.key.set_repeat(199, 69)
        pygame.display.flip()