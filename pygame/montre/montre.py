import pygame
from datetime import datetime

pygame.init()

screen  = pygame.display.set_mode((400,400))
pygame.display.set_caption("time is now")
clock = pygame.time.Clock()
text = pygame.font.SysFont("Verdana", 20, bold=False, italic=False)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #get time
    t = datetime.now()  #2024-01-17 18:21:23
    #print(t) draw clock
    time_render = text.render(f"{t:%H:%M:%S}", True, (10,1,4), (0,128,0)) #font et bacgroud
    screen.blit(time_render,(0,0))
    pygame.display.flip()
    
pygame.quit()