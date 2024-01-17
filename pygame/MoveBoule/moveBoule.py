import pygame
import random
#setup
screenSize = (800,400)
screenColor = (10,0,0)
caption = "BouleMove"
#cercle
radius = 30
xO = 30
yO = 200
pygame.init()

screen = pygame.display.set_mode(screenSize)
screen.fill(screenColor)
pygame.display.set_caption(caption)
pygame.display.update()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    circle = pygame.draw.circle(screen, (255,0,0), (xO,yO), radius)
    # move
    pygame.display.flip()

pygame.quit()