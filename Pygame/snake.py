import pygame, random, sys
from pygame.locals import *
import time

def collide(x1, x2, y1, y2, w1, w2, h1, h2):
	#x1=first block on the x
	#x2=last block on the x
	#y1=first block on the y
	#y2=last block on the y
	#w1=width
	#w2=width
	#h1=height
	#h2=height

	print ('x1=',x1,'x2=',x2,'y1=',y1,'y2=',y2,'w1=',w1,'w2=',w2,'h1=',h1,'h2=',h2)
	if x1+w1>x2 and x1<x2+w2 and y1+h1>y2 and y1<y2+h2:
		return True
	else:
		return False

def die(screen, score):
	f=pygame.font.SysFont('Arial', 30);t=f.render('Your score was: '+str(score), True, (0, 0, 0))
	screen.blit(t, (10, 270))
	pygame.display.update()
	pygame.time.wait(2000)
	sys.exit(0)


#The initial X position of each segment of the snake
xs = [290, 290, 290, 290, 290]

#The initial Y position of each segment of the snake
ys = [290, 270, 250, 230, 210]

#dirs indicates direction - 0=down, 1=right, 2=up, 3=left
dirs = 0
DIRECTION='down'

#Set the score to zero
score = 0


#Set the position of the 'apple'
applepos = (random.randint(100, 400), random.randint(100, 400))

#Initialize pgame
pygame.init()

SCREEN_X=500
SCREEN_Y=500

#Set the screen size
s=pygame.display.set_mode((SCREEN_X,SCREEN_Y))

#Set the caption of the screen
pygame.display.set_caption('Snake')

#Surface is the pygame object for representing images
#Create a 10pxlx10pxl object
appleimage = pygame.Surface((10, 10))

#Make it green
appleimage.fill((0, 255, 0))

#Now, create the snake, a 20x20 object
img = pygame.Surface((20, 20))

#Make the snake red
img.fill((255, 0, 0))

#Set the font
f = pygame.font.SysFont('Arial', 20)

#Create a clock object
clock = pygame.time.Clock()

while True:
	clock.tick(5) #Ensures we don't go over 10 FPS
	print (dirs)

	for event in pygame.event.get(): #Trap any events

		if event.type == QUIT: #The x on the window
			sys.exit(0)
		#dirs indicates direction - 0=down, 1=right, 2=up, 3=left
		elif event.type == KEYDOWN: #Detects a keypress
			if event.key == K_SPACE:
				time.sleep(10)
			if event.key == K_UP and dirs != 0: #If you press up key and we aren't going down, then go up
				dirs = 2 #2=up
			elif event.key == K_DOWN and dirs != 2: #If you press down key aand we aren't going up, then ok
				dirs = 0 #0=down
			elif event.key == K_LEFT and dirs != 1: #If you press the left key and we aren't going right, then ok
				dirs = 3 #3=left
			elif event.key == K_RIGHT and dirs != 3: #If you press the right key and we aren't going left, then ok
				dirs = 1 #1=right





	i = len(xs)-1 #How many segments the snake has on the X axis

	print ('i=',i)

	while i >= 2:
		#args are: first block of snake on the x, last block on the x, first on the y, last on the y
		# and then the size of each block (20x20 pixels)
		if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
			print ('collided,i=',i)
			die(s, score)
		i-= 1

	if collide(xs[0], applepos[0], ys[0], applepos[1], 20, 10, 20, 10):
		score+=1;xs.append(700)
		ys.append(700)
		applepos=(random.randint(0,SCREEN_X-50),random.randint(0,SCREEN_Y-50)

	if xs[0] < 0 or xs[0] > SCREEN_X-20 or ys[ 0] < 0 or ys[0] > SCREEN_Y-20: #If the head of the snake hits edge of screen
		print ('hit edge of screen')
		die(s, score)

	i = len(xs)-1

	while i >= 1:
		xs[i] = xs[i-1];ys[i] = ys[i-1];i -= 1
	if dirs==0:
		ys[0] += 20
	elif dirs==1:
		xs[0] += 20
	elif dirs==2:
		ys[0] -= 20
	elif dirs==3:
		xs[0] -= 20

	# print ('xs[0]=',xs[0])
	# print ('xs[1]=',xs[1])
	# print ('xs[2]=',xs[2])
	# print ('xs[3]=',xs[3])
	# print ('xs[4]=',xs[4])


	# print ('ys[0]=',ys[0])
	# print ('ys[1]=',ys[1])
	# print ('ys[2]=',ys[2])
	# print ('ys[3]=',ys[3])
	# print ('ys[4]=',ys[4])



	#time.sleep(1)
	s.fill((255, 255, 255))

	for i in range(0, len(xs)):
		s.blit(img, (xs[i], ys[i]))

	s.blit(appleimage, applepos)
	t=f.render(str(score), True, (0, 0, 0))
	s.blit(t, (10, 10))
	pygame.display.update()
					
					
			


