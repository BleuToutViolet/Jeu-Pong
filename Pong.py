from pygame.math import Vector2
import core
import pygame
from Joueur2 import JoueurD
from Joueur1 import JoueurG
from Balle import balle

def setup():
    print("Setup START---------")

    core.fps = 60
    core.WINDOW_SIZE = [1600, 900]
    core.memory("Joueur2", JoueurD())
    core.memory("Joueur1", JoueurG())
    core.memory("balle", balle())

    core.memory("z", Vector2(0, -1))
    core.memory("q", Vector2(-1, 0))
    core.memory("s", Vector2(0, 1))
    core.memory("d", Vector2(1, 0))

def run():
    core.cleanScreen()
    if core.memory("Joueur1").vivant:
        core.memory("Joueur1").deplacer(core.getKeyPressList)



    core.memory("Joueur2").afficher(core.screen)
    core.memory("Joueur1").afficher(core.screen)
    core.memory("balle").draw(core.screen)


    #core.memory(("Joueur")).deplacement(core.screen)



core.main(setup, run)