"""11 import modul : pour faire pygame il faut de librairie pygame
"""
import pygame

pygame.init()


"""12 show the evemt loop

while True:
    for event in pygame.event.get():
        print(event)
"""
"""13 Quit the event loop properly
"""
runing = True
screen = pygame.display.set_mode((400,300)) # return the surface x * y
pygame.display.set_caption("je suis un titre")

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        #else :print(event)


pygame.quit()