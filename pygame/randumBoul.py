import pygame
import random

pygame.init()

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
x = 2
y = 2
""" circle = Circle(x,y,50,(0,0,0)) """
#Couleur de fond
screen.fill((60,128,0))

#mise a jour de l'affichage
pygame.display.flip()
runing = True



while runing:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            runing = False
    
    #Affichage du Cercle
    x = random.randint(100,screen.get_width()-100)
    y = random.randint(100,screen.get_height()-100)
    circle = Circle(x,y,1,(0,0,0))
    circle.draw(screen)
    pygame.display.flip()
pygame.quit()