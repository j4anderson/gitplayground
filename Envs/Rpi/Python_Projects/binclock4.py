#!/usr/bin/python3.2
#
# binclock4.py
#
# Gets the system time and displays it in binary format
# This version will attempt to reduce CPU usage by reducing the number of 
# cycles in the WHILE loop to 10 per second...see test_sec.py for comparative 
# cycle counts...currently only uses about 2% vs 20

# import
import time

# Get the system time:
#thetime=time.strftime("%H%M%S")

#Now try to display it in a graphical way

import sys, pygame
pygame.init()

# display details:
size = width, height = 700, 580
gray = 192, 192, 192
white= 255,255,255

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Binary Clock 4')
blkball = pygame.image.load("images/4row_black.png")
redball = pygame.image.load("images/4row_red.png")

font=pygame.font.Font('/usr/share/fonts/truetype/roboto/Roboto-Black.ttf',60)

## so start here and figure out how to make the spots for
## each ball on the display surface.  stacked: 2,4,3,4,3,4
pos_h11 = blkball.get_rect(center=(55,400))
pos_h12 = blkball.get_rect(center=(55,290))
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

compTime="25:00:00"
i=1

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	#Get the time
	theTime=time.localtime()

	#Compare it to previous time every tenth of a second (save cpu cycles)
	if compTime==time.strftime("%H:%M:%S",theTime):
		i=i+1
		time.sleep(0.1)
		continue
	else:
		i=1
		compTime=time.strftime("%H:%M:%S",theTime)

		screen.fill(gray)
		#Hrs
		screen.blit(blkball,pos_h11)
		screen.blit(blkball,pos_h12)
		screen.blit(blkball,pos_h21)
		screen.blit(blkball,pos_h22)
		screen.blit(blkball,pos_h23)
		screen.blit(blkball,pos_h24)
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
	
		#Display the time for reference:
		stdclock=font.render(time.strftime("%H:%M:%S",theTime),1,(white))
	
		#Hours
		theHrs=time.strftime("%H",theTime)
		if int(theHrs) >= 10:
			theHrs1=bin(int(theHrs[0]))
			theHrs1=theHrs1.lstrip('-0b')
			theLen=len(theHrs1)
			if theLen==2:
				if theHrs1[1]=="1":
					screen.blit(redball,pos_h11)
				if theHrs1[0]=="1":
					screen.blit(redball,pos_h12)
			if theLen==1:
				if theHrs1[0]=="1":
					screen.blit(redball,pos_h11)
		theHrs0=bin(int(theHrs[1]))
		theHrs0=theHrs0.lstrip('-0b')
		theLen=len(theHrs0)
		if theLen==4:
			if theHrs0[3]=="1":
				screen.blit(redball,pos_h21)
			if theHrs0[2]=="1":
				screen.blit(redball,pos_h22)
			if theHrs0[1]=="1":
				screen.blit(redball,pos_h23)
			if theHrs0[0]=="1":
				screen.blit(redball,pos_h24)
		if theLen==3:
			if theHrs0[2]=="1":
				screen.blit(redball,pos_h21)
			if theHrs0[1]=="1":
				screen.blit(redball,pos_h22)
			if theHrs0[0]=="1":
				screen.blit(redball,pos_h23)
		if theLen==2:
			if theHrs0[1]=="1":
				screen.blit(redball,pos_h21)
			if theHrs0[0]=="1":
				screen.blit(redball,pos_h22)
		if theLen==1:
			if theHrs0[0]=="1":
				screen.blit(redball,pos_h21)
	
		#Mins
		theMins=time.strftime("%M",theTime)
		if int(theMins) >= 10:
			theMins1=bin(int(theMins[0]))
			theMins1=theMins1.lstrip('-0b')
			theLen=len(theMins1)
			if theLen==3:
				if theMins1[2]=="1":
					screen.blit(redball,pos_h31)
				if theMins1[1]=="1":
					screen.blit(redball,pos_h32)
				if theMins1[0]=="1":
					screen.blit(redball,pos_h33)
			if theLen==2:
				if theMins1[1]=="1":
					screen.blit(redball,pos_h31)
				if theMins1[0]=="1":
					screen.blit(redball,pos_h32)
			if theLen==1:
				if theMins1[0]=="1":
					screen.blit(redball,pos_h31)
		theMins0=bin(int(theMins[1]))
		theMins0=theMins0.lstrip('-0b')
		theLen=len(theMins0)
		if theLen==4:
			if theMins0[3]=="1":
				screen.blit(redball,pos_h41)
			if theMins0[2]=="1":
				screen.blit(redball,pos_h42)
			if theMins0[1]=="1":
				screen.blit(redball,pos_h43)
			if theMins0[0]=="1":
				screen.blit(redball,pos_h44)
		if theLen==3:
			if theMins0[2]=="1":
				screen.blit(redball,pos_h41)
			if theMins0[1]=="1":
				screen.blit(redball,pos_h42)
			if theMins0[0]=="1":
				screen.blit(redball,pos_h43)
		if theLen==2:
			if theMins0[1]=="1":
				screen.blit(redball,pos_h41)
			if theMins0[0]=="1":
				screen.blit(redball,pos_h42)
		if theLen==1:
			if theMins0[0]=="1":
				screen.blit(redball,pos_h41)
	
		#Secs
		theSecs=time.strftime("%S",theTime)
		if int(theSecs) >= 10:
			theSecs1=bin(int(theSecs[0]))
			theSecs1=theSecs1.lstrip('-0b')
			theLen=len(theSecs1)
			if theLen==3:
				if theSecs1[2]=="1":
					screen.blit(redball,pos_h51)
				if theSecs1[1]=="1":
					screen.blit(redball,pos_h52)
				if theSecs1[0]=="1":
					screen.blit(redball,pos_h53)
			if theLen==2:
				if theSecs1[1]=="1":
					screen.blit(redball,pos_h51)
				if theSecs1[0]=="1":
					screen.blit(redball,pos_h52)
			if theLen==1:
				if theSecs1[0]=="1":
					screen.blit(redball,pos_h51)
		theSecs0=bin(int(theSecs[1]))
		theSecs0=theSecs0.lstrip('-0b')
		theLen=len(theSecs0)
		if theLen==4:
			if theSecs0[3]=="1":
				screen.blit(redball,pos_h61)
			if theSecs0[2]=="1":
				screen.blit(redball,pos_h62)
			if theSecs0[1]=="1":
				screen.blit(redball,pos_h63)
			if theSecs0[0]=="1":
				screen.blit(redball,pos_h64)
		if theLen==3:
			if theSecs0[2]=="1":
				screen.blit(redball,pos_h61)
			if theSecs0[1]=="1":
				screen.blit(redball,pos_h62)
			if theSecs0[0]=="1":
				screen.blit(redball,pos_h63)
		if theLen==2:
			if theSecs0[1]=="1":
				screen.blit(redball,pos_h61)
			if theSecs0[0]=="1":
				screen.blit(redball,pos_h62)
		if theLen==1:
			if theSecs0[0]=="1":
				screen.blit(redball,pos_h61)
	
		#STD Clock
		screen.blit(stdclock,(250,480))
		
	pygame.display.flip()

