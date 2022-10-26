from menu.Menu import Menu
import pygame

class MenuPauseEstado:
    k_up = [pygame.K_UP, pygame.K_k]
    k_down = [pygame.K_DOWN, pygame.K_j]
    k_confirm = [pygame.K_RETURN]
    k_quit = [pygame.K_ESCAPE]

    def __init__(self, screen):
        self.menu = Menu()
        self.menu.init(['Continuar', 'Sair'], screen)

    def update(self, key, screen):
        self.menu.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key in self.k_up:
                    self.menu.draw(-1)
                if event.key in self.k_down:
                    self.menu.draw(1)
                if event.key in self.k_confirm:
                    if self.menu.get_position() == 0:
                        return "continue"
                    if self.menu.get_position() == 1:
                        return "quit"
