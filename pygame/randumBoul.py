import pygame
import random

class Circle:
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.radius =radius
        self.color = color
    def draw(self, surface):
        pygame.draw.circle(surface,self.color,(self.x,self.y),self.radius)
         
#creation de la fenetre      
screen = pygame.display.set_mode((400,400))
#creer cercle
""" circle = Circle(200,200,50,(0,0,0)) """
#Couleur de fond
screen.fill((60,128,0))

#mise a jour de l'affichage
pygame.display.flip()
runing = True


pygame.init()

while runing:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            runing = False
    
    #Affichage du Cercle
    circle = Circle(200,200,50,(0,0,0))
    circle.draw(screen)
    pygame.display.flip()
pygame.quit()