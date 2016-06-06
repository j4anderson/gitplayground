#!/usr/bin/python3.2
#
# test_font.py
#
# Play with pygame font objects for testing

# import
import time

# Get the system time:
thetime=time.strftime("%H:%M:%S")

#Now try to display it in a graphical way

import sys, pygame
pygame.init()

# display details:
size = width, height = 300, 300
gray = 192, 192, 192
white= 255,255,255
black= 0,0,0

screen=pygame.display.set_mode(size)

#font=pygame.font.Font(None,30)
font=pygame.font.Font('/usr/share/fonts/truetype/roboto/Roboto-Black.ttf',30)
#How did I find this file?  
# python3.2
#>>>import pygame
#>>>pygame.font.get_fonts()   - lists them out (but no punctuation & lower case)
#>>>pygame.font.match_font('roboto')  - and Viola!

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	stdclock=font.render("Time: "+time.strftime("%H:%M:%S"),1,(white))
	screen.fill(black)
	screen.blit(stdclock,(50,100))

	pygame.display.flip()