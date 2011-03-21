#-*-coding:utf-8

'''
PUG-PE Arduino Tools 

Por Marcel Pinheiro Caraciolo - caraciol@gmail.com
    Victor Case -  victor.case@hotmail.com
    Gabriel Liber  -  lsl.gabriel@gmail.com
    Diego Liber - diegoliber@gmail.com

Semaforo PUG-PE
'''

from optparse import OptionParser,SUPPRESS_USAGE
from arduino_handler import *
import commands
import os
from time import ctime
import subprocess
import pygame
from pygame.locals import *


__version__ = 0.1

event_happened = False

def git_commit_all(directory):
    """
    Adds all files and commits them using git
    
    Code fetched from Flavio Amieiro
    https://github.com/flavioamieiro/dojotools/blob/master/dojotools.py
    
    """
    msg = ctime()
    process = subprocess.Popen(
        "git add . && git commit -m '%s'" % msg,
        shell=True,
        cwd= directory,
    )

    #if git returns 128 it means 'command not found' or 'not a git repo'
    if process.wait() == 128:
        error = ('Impossible to commit to repository. '
                'Make sure git is installed an this is a valid repository')
        raise OSError(error)


def key_handler():
    global event_happened
    for event in pygame.event.get():
        if not hasattr(event,'key'): continue
        if event.key  == K_ESCAPE: 
            sys.exit(0)
        elif event.key == K_SPACE and event.type == KEYDOWN:
            event_happened = True
            
def main(options):
    global event_happened
    #Execute the test and get the output
    #Send the ouput to arduino
    test_file = options.test_file
    test_file = test_file + '.py' if not test_file.endswith('.py') else test_file
    output =  commands.getoutput('python %s/%s' % (options.directory,test_file))
    if 'FAILED' in output or 'Traceback' in output or 'Error' in output:
        arduino.send_message(FAIL)
        print output
        print 'Test has failed.'

    else:
        arduino.send_message(PASS)
        print output
        print 'Test has passed.'

    #if -c active, add, commit the files.
    if options.commit:
        git_commit_all(options.directory)

    event_happened = False


def run_main(options):
    #Connect to Arduino
    arduino = Arduino()

    #Initialize the main program
    pygame.init()
    windowsSurface = pygame.display.set_mode((640,480),0,32)
    pygame.display.set_caption('Semaforo')

    while True:
        key_handler()
        if event_happened:
            main(options)



if __name__ == '__main__':
    parser = OptionParser(usage=SUPPRESS_USAGE)
    print 'PUG-PE Semaforo Monitor v.%s\n' % __version__
    print 'Type --help parameter for help.\n'
    
    parser.add_option('-t', '--test-file', dest='test_file',
                        help='Test File that will be executed and monitored.')
    parser.add_option('-c', '--commit', action= 'store_true', dest= 'commit', default= False,
                        help = 'if this flag is used, a git commit will be issued whenever the files change')
    parser.add_option('-d', '--directory', dest= 'directory',
                        help='Watch Directory', default= os.path.abspath(os.path.curdir))
    
    (options,args) = parser.parse_args()

    if not options.test_file:
        parser.error('You must specifiy a valid test_file .py (-t parameter) !')

    run_main(options)