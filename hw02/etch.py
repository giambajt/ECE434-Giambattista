#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import pygame, sys
from pygame.locals import *

pygame.init()
#check if the command line was run with 2 arguments, otherwise default the etch window size
if len(sys.argv) == 3:
    etchx = int(sys.argv[1])
    etchy = int(sys.argv[2])
else:
    etchx=600
    etchy=400
#general setup for pygame and some user variables
screen = pygame.display.set_mode((600,400))
left_button = "P9_19"
up_button = "P9_21"
down_button = "P9_23"
right_button = "P9_22"
GPIO.setup(left_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(up_button, GPIO.IN,pull_up_down =  GPIO.PUD_DOWN)
GPIO.setup(down_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(right_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

x= etchx//2
y= etchy//2

def read_pin(pin):
    global x
    global y
    if pin == up_button:
        y-=1
    elif pin == down_button:
        y+=1
    elif pin == left_button:
        x-=1
    elif pin == right_button:
        x+=1



#GPIO.add_event_detect(up_button, GPIO.BOTH, turn_LED_ON)
#GPIO.add_event_detect(down_button, GPIO.BOTH, turn_LED_ON2)
#GPIO.add_event_detect(left_button, GPIO.BOTH, turn_LED_ON3)
#GPIO.add_event_detect(right_button, GPIO.BOTH, turn_LED_ON4)

opening_screen=1#binary value that dictates whether the computer is on the opening screen or the etch screen
black= (0,0,0)
white = (255,255,255)
#setup the basics for pygame and all of the text instructions on the opening screen
clock = pygame.time.Clock()
screen.fill(white)
pygame.display.set_caption('etch_a_sktech')
font = pygame.font.Font('freesansbold.ttf',16) 
text = font.render('Welcome to Etch-A-Sketch!', True, black, white)
textRect = text.get_rect()
textRect.center = (300, 200)
instructionText = font.render('Instructions: Move the line using the arrow keys and', True, black, white)
insTextRect = instructionText.get_rect()
insTextRect.center = (300, 200+20)
instructionText2 = font.render('shake the pad with space bar. Press escape to exit.', True, black, white)
insTextRect2 = instructionText2.get_rect()
insTextRect2.center = (300, 200+40)
instructionText3 = font.render('Press the space bar to start the game', True, black, white)
insTextRect3 = instructionText3.get_rect()
insTextRect3.center = (300, 200+60)


#main loop
while 1:
    #makes game run at 60 FPS and updates the screen
    clock.tick(60)
    pygame.display.update()
    #etch screen
    if opening_screen == 0:
        #etch window event loop that draws the sketches and reads for keyboard inputs
        pygame.draw.circle(screen, black, (x,y),2)
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT] or GPIO.input(right_button):x+=1
        if key[pygame.K_LEFT] or GPIO.input(left_button):x-=1
        if key[pygame.K_UP] or GPIO.input(up_button):y-=1
        if key[pygame.K_DOWN] or GPIO.input(down_button):y+=1
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
            
            elif event.type == KEYDOWN and event.key == K_SPACE:
                screen.fill(white)#screen 'shake'
    #opening screen
    elif opening_screen == 1:
        #display all of the instruction texts
        screen.blit(text,textRect)
        screen.blit(instructionText, insTextRect)
        screen.blit(instructionText2, insTextRect2)
        screen.blit(instructionText3, insTextRect3)
        #event loop that checks for keyboard presses
        for event in pygame.event.get():
            #When space is pressed, setup the screen for the etch window
            if event.type == KEYDOWN and event.key == K_SPACE:
                screen = pygame.display.set_mode((etchx,etchy))
                screen.fill(white)
                opening_screen = 0
            elif event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
