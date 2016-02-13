#!/usr/bin/python3.2
# illustrate how command line arguments work:

import sys

print("There are "+str(len(sys.argv))+" element(s) passed in from the command line.")
i=0
for x in sys.argv:
  print("Argv("+str(i)+") is: ",x)
  i=i+1
