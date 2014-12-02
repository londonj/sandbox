import pygame

pygame.init()

gameDisplay=pygame.display.set_mode((800,600))

pygame.display.set_caption('RaceyRay')

clock = pygame.time.Clock()

crashed = False

while not crashed:
