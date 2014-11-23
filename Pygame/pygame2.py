import pygame
import time


x = pygame.init()
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

SCREEN_X=400
SCREEN_Y=200
BLOCKSIZE=10
FPS=10


gameDisplay = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
pygame.display.set_caption('Slither')



gameExit=False
lead_x = SCREEN_X/2
lead_y = SCREEN_Y/2
lead_x_change=0
lead_y_change=0

clock=pygame.time.Clock()




while not gameExit:
    print('lead_x=',lead_x,'lead_y=',lead_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameExit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -2
                lead_y_change = 0

            elif event.key == pygame.K_RIGHT:
                lead_x_change = 2
                lead_y_change = 0

            elif event.key == pygame.K_DOWN:
                lead_y_change = 2
                lead_x_change = 0

            elif event.key == pygame.K_UP:
                lead_y_change = -2
                lead_x_change = 0

            elif event.key == pygame.K_ESCAPE:
                gameExit = True

    if lead_x >= SCREEN_X:
        lead_x = 1


    if lead_x <= 0:
        lead_x = SCREEN_X

    if lead_y >= SCREEN_Y:
        lead_y=1

    if lead_y <= 0:
        lead_y = SCREEN_Y

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay,RED,[lead_x,lead_y,BLOCKSIZE,BLOCKSIZE])
    #pygame.draw.circle(gameDisplay,BLUE,[350,250,10,10])
    #ameDisplay.fill(BLUE,rect=(200,200,30,30))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

quit()

