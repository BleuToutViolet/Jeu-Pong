import random
from pygame.math import Vector2
from hold import core
import core
import pygame
from pygame.math import Vector2

class JoueurD :
    def __init__(self):
        self.couleur = (255, 0, 0)
        self.dimmension = 15, 120
        self.position = Vector2(1550, 450)
        self.direction = Vector2(0, 0)


    def deplacer(self, position):

        if core.getKeyPressList(pygame.K_t):
            self.direction, Vector2(self.direction.y, -1)
        if core.getKeyPressList(pygame.K_g):
            self.direction, Vector2(self.direction.y, +1)

    def vivant(self):
        self.vivant = True

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)

    def afficher(self, screen):
        pygame.draw.rect(screen, self.couleur, (self.position, self.dimmension), 0, 10)

