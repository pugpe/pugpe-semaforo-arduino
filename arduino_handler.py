#-*-coding:utf-8

'''
PUG-PE Arduino Tools 

Por Marcel Pinheiro Caraciolo - caraciol@gmail.com
    Victor Case -  victor.case@hotmail.com
    Gabriel  -  lsl.gabriel@gmail.com
    Diego Liber - diegoliber@gmail.com

Arduino Connector Handler

'''

import serial
import time
import sys

PASS = 1
FAIL = 0

GREEN = '1'
RED = '0'

class Arduino(object):
    
    def __init__(self):
        self.arduino = None
        
        if sys.platform == 'linux2':
            for i in range(0,45):
                try:
                     self.arduino = serial.Serial('/dev/ttyACM%d' %i, 9600)
                     break
                except serial.serialutil.SerialException:
                     pass
        elif sys.platform == 'darwin':
            for i in range(0,500):
                try:
                     self.arduino = serial.Serial('/dev/cu.usbmodem%d' %i, 9600)
                     break
                except serial.serialutil.SerialException:
                     pass  
        else:
            for i in range(0,45):
                try:
                     self.arduino = serial.Serial('COM%d' % i, 9600)
                     break
                except serial.SerialException:
                     pass
        if not self.arduino:
            print 'ERRO: Arduino nao encontrado. Favor verificar a porta correta.'
            exit()
            

    def send_message(self,test_code):
        '''
        Send a message to Arduino via serial
        '''   
        if test_code == PASS:
            self.arduino.write(GREEN)
        else:
            self.arduino.write(RED)

     
        


if __name__ ==  '__main__':
    handler = Arduino()
    handler.send_message(PASS)







