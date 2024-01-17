import pygame

pygame.init()

screen = pygame.display.set_mode((400,400))
boule = pygame.image.load("boule,png").convert()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()