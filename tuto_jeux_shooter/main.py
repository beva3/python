import pygame

pygame.init()

#generer la fenetre de jeux
pygame.display.set_caption("Mon jeux shooter")
pygame.display.set_mode((1080,500))

runing =True

#le boucle tant que cette ondtition est vrai
while runing:
    #si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            runing = False
            pygame.quit()
