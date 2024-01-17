import pygame
import random
#setup
screenSize = (400,400)
screenColor = (10,0,0)
caption = "BouleMove"
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


pygame.quit()