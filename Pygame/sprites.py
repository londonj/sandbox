import pygame
import random
import time

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([width,height])
        self.image.fill(color)

        self.rect=self.image.get_rect()

#class Circle(pygame.sprite.Sprite):
 #   def __init__(self,color,(x,y),radius=20,thickness=10):
 #       self.image=pygame.Surface()


pygame.init()

screen_width=700
screen_height=400

screen=pygame.display.set_mode([screen_width,screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

#Draw the blocks on the screen

for i in range(20):
    block=Block(BLACK,20,15)

    block.rect.x=random.randrange(screen_width-20)
    block.rect.y=random.randrange(screen_height-15)

    block_list.add(block)
    all_sprites_list.add(block)

screen.fill(pygame.Color('cyan'))
#all_sprites_list.draw(screen)
#pygame.display.flip()
#print ("just drew, now sleeping")
#time.sleep(3)

player=Block(RED,20,15)
all_sprites_list.add(player)

done=False

clock=pygame.time.Clock()

score=0

while done==False:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done=True

        screen.fill(pygame.Color('cyan'))

        pos=pygame.mouse.get_pos()
        #print (pos[0],pos[1])

        player.rect.x=pos[0]
        player.rect.y=pos[1]

        blocks_hit_list = pygame.sprite.spritecollide(player,block_list,True)

        if len(blocks_hit_list) > 0:
            score += len(blocks_hit_list)
            print (score)

        all_sprites_list.draw(screen)

        clock.tick(20)

        pygame.display.flip()

pygame.quit()





