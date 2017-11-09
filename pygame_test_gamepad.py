#!/usr/bin/env python

import os, sys, pygame 
from pygame import locals
import time

# Define the colors we will use in RGB format
black = [ 0, 0, 0]
white = [255,255,255]
red = [255, 0, 0]

#os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

# Set the height and width of the screen
size=[630,300]
screen=pygame.display.set_mode(size)
# Fill the screen White
screen.fill(white)
# Put something in the application Bar
pygame.display.set_caption("Testing gamepad")

pygame.draw.rect(screen,black,(19,19,276,276),0)

pygame.display.flip()

pygame.joystick.init() # main joystick device system

textfont = pygame.font.SysFont("moonspace",24)

done = True

try:
    j = pygame.joystick.Joystick(0) # create a joystick instance
    j.init() # init instance
    print 'Enabled joystick: ' + j.get_name()
except pygame.error:
    print 'no joystick found.'

pygame.draw.rect(screen,black,(19,19,276,276),0)
pygame.draw.rect(screen,white,(148,148,20,20),0)
pygame.display.flip()


while done:
    for e in pygame.event.get(): # iterate over event stack
        if e.type == pygame.QUIT:
            done = False
        
        if e.type == pygame.locals.JOYAXISMOTION: # Read Analog Joystick Axis
            x1 , y1 = j.get_axis(0), j.get_axis(1) # Left Stick

            print x1
            print y1
            pygame.draw.rect(screen,black,(19,19,276,276),0)
            pygame.draw.rect(screen,white,(148+(x1*128),148+(y1*128),20,20),0)
            pygame.display.flip()

        
        if e.type == pygame.locals.JOYBUTTONDOWN: # Read the buttons
            print ("button down"+str(e.button))
            for i in range(0,10):
                if e.button == i:
                    pygame.draw.rect(screen,red,(300+(i*30),20,20,20),0)
                    buttonText = textfont.render(str(i),1,white)
                    screen.blit(buttonText,(300+(i*30)+3,20))
                    pygame.display.flip()
            

        if e.type == pygame.locals.JOYBUTTONUP: # Read the buttons
            print ("button up"+str(e.button))
            for i in range(0,10):
                if e.button == i:
                    pygame.draw.rect(screen,white,(300+(i*30),20,20,20),0)
                    pygame.display.flip()
