
import pygame
import sys
from pygame.locals import *
import time
import random


pygame.init()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
CYAN=(0,255,255)
PURPLE=(255,0,255)

COLOR=(WHITE,BLACK,RED,GREEN,BLUE,YELLOW,CYAN,PURPLE)

SCREEN_X=800
SCREEN_Y=600

setDisplay=pygame.display.set_mode((SCREEN_X,SCREEN_Y))

singlePixel=pygame.PixelArray(setDisplay)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    while 1:
            color=COLOR[random.randint(0,7)]

            xpos=random.randint(1,SCREEN_X)
            ypos=random.randint(1,SCREEN_Y)
            if xpos >SCREEN_X:
                    sys.exit()
            if ypos>SCREEN_Y:
                    sys.exit()

            print (xpos,ypos)

            singlePixel[ypos][xpos]=color
            pygame.display.update()
            time.sleep(.1)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

