import pygame
import time

x = pygame.init()
print (x)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

pygame.display.update()

gameExit=False

while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
                gameExit = True



pygame.quit()

quit()

