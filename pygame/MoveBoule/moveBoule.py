import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("BouleMove")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()