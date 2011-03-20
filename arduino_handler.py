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

def send_message(test_code):
    '''
    Send a message to Arduino via serial
    '''
    if sys.platform == 'linux2':
        for i in range(0,45):
            try:
                 arduino = serial.Serial('/dev/ttyACM%d' %i, 9600)
                 break
            except SerialException:
                 pass
    elif sys.platform == 'darwin':
        for i in range(0,500):
            try:
                 arduino = serial.Serial('/dev/cu.usbmodem%d',9600)
                 break
            except SerialException:
                 pass  
    else:
        for i in range(0,45):
            try:
                 arduino = serial.Serial('COM%d' % i, 9600)
                 break
            except SerialException:
                 pass  
   
    if test_code == PASS:
        arduino.write('1')
    else
        arduino.write('0')

     
        










