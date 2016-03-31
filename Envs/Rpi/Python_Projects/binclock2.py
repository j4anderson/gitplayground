#!/usr/bin/python3.2
#
# binclock2.py
#
# Gets the system time and displays it in binary format

# import
import time

# Get the system time:
thetime=time.strftime("%H:%M:%S")
print("The time in HH24:MI:SS is " + thetime)

# Convert its digits into binary
thetime2=time.strftime("%H%M%S")
bintime=bin(int(thetime2))
print("The time in not quite binary " + bintime)

#Now try to display it in a graphical way

import sys, pygame
pygame.init()

# display details:
size = width, height = 640, 480
gray = 192, 192, 192

screen = pygame.display.set_mode(size)
blkball = pygame.image.load("images/4row_black.png")
redball = pygame.image.load("images/4row_red.png")

## so start here and figure out how to make the spots for
## each ball on the display surface.  stacked: 1,2,3,4,3,4
pos_h11 = blkball.get_rect(center=(50,400))
pos_h21 = blkball.get_rect(center=(170,400))

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(gray)
	screen.blit(blkball,pos_h11)
	screen.blit(redball,pos_h21)
	pygame.display.flip()

# Finish drawing the ball locations

## then wire up the thetime to the balls