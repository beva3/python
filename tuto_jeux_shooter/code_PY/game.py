import pygame
from player import Player

#creer une second class qui va representer notre jeu
class Game:
    #generer notre joueur
    def __init__(self):
        self.player = Player()
