import pygame
from player import Player
from game import Game

pygame.init()

#generer la fenetre de jeux
pygame.display.set_caption("Mon jeux shooter")
screen = pygame.display.set_mode((1080,600))

#importer de charger l'arierre plan cd notre jeux
background = pygame.image.load("../assets/bg.jpg")

""" #charger notre joueur
player = Player()
 """
#charger notre jeux
game =  Game()
runing =True

#le boucle tant que cette ondtition est vrai
while runing:
    
    
    #appliquer l'arrier plan de notre jeux 
    screen.blit(background,(0,-300))
    
    #appliquer l'image de mon joueur
    screen.blit(game.player.image,game.player.rect)
    
    #mise a jour de l'ecran
    pygame.display.flip()
    
    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        
        
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()
