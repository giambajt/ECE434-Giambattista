#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

pygame.init()

if len(sys.argv) == 3:
    etchx = int(sys.argv[1])
    etchy = int(sys.argv[2])
else:
    etchx=600
    etchy=400
screen = pygame.display.set_mode((600,400))
x= etchx//2
y= etchy//2
opening_screen=1
black= (0,0,0)
white = (255,255,255)

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



while 1:
    clock.tick(60)
    pygame.display.update()
    if opening_screen == 0:
        pygame.draw.circle(screen, black, (x,y),2)
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:x+=1
        if key[pygame.K_LEFT]:x-=1
        if key[pygame.K_UP]:y-=1
        if key[pygame.K_DOWN]:y+=1
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()
            
            elif event.type == KEYDOWN and event.key == K_SPACE:
                screen.fill(white)
    elif opening_screen == 1:
        screen.blit(text,textRect)
        screen.blit(instructionText, insTextRect)
        screen.blit(instructionText2, insTextRect2)
        screen.blit(instructionText3, insTextRect3)
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_SPACE:
                screen = pygame.display.set_mode((etchx,etchy))
                screen.fill(white)
                opening_screen = 0
            elif event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                sys.exit()

