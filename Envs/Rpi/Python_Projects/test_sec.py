#!/usr/bin/python3.2

# import
import time

thatTime="25:00:00"
i=1

#print("thatTime: " + thatTime)
#print("thisTime: " + thisTime)

while 1:
	thisTime=time.strftime("%H:%M:%S",time.localtime())
	if thisTime==thatTime:
		i=i+1
		time.sleep(0.1)
		continue
	else:
		print("thisTime: " + thisTime + " cycle count:" + str(i))
		i=1
		thatTime=thisTime
	
