#-*-coding:utf-8

'''
PUG-PE Arduino Tools 

Por Marcel Pinheiro Caraciolo - caraciol@gmail.com
    Victor Case -  victor.case@hotmail.com
    Gabriel Liber  -  lsl.gabriel@gmail.com
    Diego Liber - diegoliber@gmail.com

Semaforo PUG-PE
'''

import time,pygame
from arduino_handler import *
from pygame.locals import *


if __name__ == '__main__':
    arduino = Arduino()
    
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
            arduino.send_message(PASS)
            Verde = False
            Vermelho = False

        if Vermelho == True:
            arduino.send_message(FAIL)
            Verde = False
            Vermelho = False



    
                
