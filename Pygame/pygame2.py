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

font=pygame.font.SysFont(None,25)

def msg(msg,color):
    start=(SCREEN_X/2)-len(msg)/2
    print (start)
    screen_text = font.render(msg,True,color)
    print (start)
    gameDisplay.blit(screen_text,[start,SCREEN_Y/2])
    pygame.display.update()


gameDisplay = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
pygame.display.set_caption('Slither')



clock=pygame.time.Clock()



def gameLoop():

    gameExit=False
    gameOver=False

    lead_x = SCREEN_X/2
    lead_y = SCREEN_Y/2
    lead_x_change=0
    lead_y_change=0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            msg("Game Over. P to Play Again, Q to Quit")
            pygame.display.update()
            time.sleep(3)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit=True
                        gameOver=False

                if event.key ==pygame.K_c:
                    gameLoop()

        #print('lead_x=',lead_x,'lead_y=',lead_y)
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
                    msg('Testing123',BLUE)
                    time.sleep(5)
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

gameLoop()
