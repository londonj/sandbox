import pygame
import time


x = pygame.init()
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')



gameExit=False
lead_x = 300
lead_y = 300


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10
            if event.key == pygame.K_DOWN:
                lead_y += 10
            if event.key == pygame.K_UP:
                lead_y -= 10

        if event.type == pygame.QUIT:
                gameExit = True

    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay,RED,[lead_x,lead_y,10,10])
    #pygame.draw.circle(gameDisplay,BLUE,[350,250,10,10])
    gameDisplay.fill(BLUE,rect=(200,200,30,30))

    pygame.display.update()

pygame.quit()

quit()

