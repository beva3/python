import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
boule = pygame.image.load("boule.png") #.convert()
running = True
x = 0
y = 0
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -= 2 #print("left")
    elif pressed[pygame.K_RIGHT]:
        x += 2 #print("right")
    elif pressed[pygame.K_UP]:
        y -= 2 #print("up")
    elif pressed[pygame.K_DOWN]:
        y += 2 #print("down")
    
    screen.fill((0,0,0))
    screen.blit(boule,(x,y))
    pygame.display.flip()
    clock.tick(50000)
pygame.quit()