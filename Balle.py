import random
from pygame.math import Vector2
from hold import core
import core
import pygame
from pygame.math import Vector2

class balle :
    def __init__(self):
        self.rayon = 20
        self.position = (800, 450)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def mourir(self):
        pass

    def deplacer (self,Joueurs):
        pass

    def limit(self):
        pass

    def draw(self,screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.rayon)







