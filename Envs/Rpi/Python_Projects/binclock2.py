#!/usr/bin/python3.2
#
# binclock2.py
#
# Gets the system time and displays it in binary format

# import
import time

# Get the system time:
thetime=time.strftime("%H%M%S")
bintime=bin(int(thetime2))
print("The time in not quite binary " + bintime)

#Now try to display it in a graphical way

import sys, pygame
pygame.init()

# display details:
size = width, height = 700, 480
gray = 192, 192, 192

screen = pygame.display.set_mode(size)
blkball = pygame.image.load("images/4row_black.png")
redball = pygame.image.load("images/4row_red.png")

## so start here and figure out how to make the spots for
## each ball on the display surface.  stacked: 1,4,3,4,3,4
pos_h11 = blkball.get_rect(center=(55,400))
pos_h21 = blkball.get_rect(center=(170,400))
pos_h22 = blkball.get_rect(center=(170,290))
pos_h23 = blkball.get_rect(center=(170,180))
pos_h24 = blkball.get_rect(center=(170,70))
pos_h31 = blkball.get_rect(center=(285,400))
pos_h32 = blkball.get_rect(center=(285,290))
pos_h33 = blkball.get_rect(center=(285,180))
pos_h41 = blkball.get_rect(center=(400,400))
pos_h42 = blkball.get_rect(center=(400,290))
pos_h43 = blkball.get_rect(center=(400,180))
pos_h44 = blkball.get_rect(center=(400,70))
pos_h51 = blkball.get_rect(center=(515,400))
pos_h52 = blkball.get_rect(center=(515,290))
pos_h53 = blkball.get_rect(center=(515,180))
pos_h61 = blkball.get_rect(center=(630,400))
pos_h62 = blkball.get_rect(center=(630,290))
pos_h63 = blkball.get_rect(center=(630,180))
pos_h64 = blkball.get_rect(center=(630,70))

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill(gray)
	#Hrs
	screen.blit(blkball,pos_h11)
	screen.blit(blkball,pos_h21)
	screen.blit(redball,pos_h22)
	screen.blit(redball,pos_h23)
	screen.blit(redball,pos_h24)
	#Mins
	screen.blit(blkball,pos_h31)
	screen.blit(blkball,pos_h32)
	screen.blit(blkball,pos_h33)
	screen.blit(blkball,pos_h41)
	screen.blit(blkball,pos_h42)
	screen.blit(blkball,pos_h43)
	screen.blit(blkball,pos_h44)
	#Secs
	screen.blit(blkball,pos_h51)
	screen.blit(blkball,pos_h52)
	screen.blit(blkball,pos_h53)
	screen.blit(blkball,pos_h61)
	screen.blit(blkball,pos_h62)
	screen.blit(blkball,pos_h63)
	screen.blit(blkball,pos_h64)

	pygame.display.flip()

## then wire up the thetime to the balls