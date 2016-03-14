#!/usr/bin/python3.2
#
# binclock.py
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

# Nope, do it the right way, secs, mins, hours:
theSecs=time.strftime("%S",thetime)
print("Secs: " + theSecs)
