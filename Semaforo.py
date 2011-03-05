#VictorCase 03/2001#
import serial,pygame,time
from pygame.locals import *


for i in range(1,45):
	try:
		ser = serial.Serial('COM%d' % i ,9600)
	except:
		print 'nao eh %d' % i
		

pygame.init()
windowsSurface = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption('Semaforo')

Vermelho = False
Verde = False

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_v:
                Verde = True
            if event.key == K_f:
                Vermelho = True
                
    if Verde == True:
        ser.write('1')
        Verde = False
        Vermelho = False

    if Vermelho == True:
        ser.write('0')
        Verde = False
        Vermelho = False
            

   



    
                
