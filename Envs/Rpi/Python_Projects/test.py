#!/usr/bin/python3.2

import time

#Get the time
theTime=time.localtime()

theSecs=time.strftime("%S",theTime)
print("Secs: " + theSecs)

if int(theSecs)<10:
	print("One digits")
	theSecs=bin(int(theSecs))
	theSecs=theSecs.lstrip('-0b')
	print(theSecs)
	print(str(len(theSecs)) + " Length")
	for i in range(len(theSecs),0,-1):
		print(theSecs[i-1])
	
else:
	print("Two digits")
	print(bin(int(theSecs[0])) + " First ")
	print(bin(int(theSecs[1])) + " Second ")
