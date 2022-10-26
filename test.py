import pygame
import pdb

from estados.GameOverEstado import GameOverEstado
from projetil.Projetil import Projetil

pygame.init()
screen = pygame.display.set_mode((800, 600))

p = Projetil('espada.png', (0, 0))

while True:
    key = pygame.key.get_pressed()

    p.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                pass

    screen.fill((155, 155, 155))

    screen.blit(p.getImg(), p.getRect())

    pygame.display.flip()
