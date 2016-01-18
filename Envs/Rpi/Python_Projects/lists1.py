#! /usr/bin/env python3.2 
# create a list named a
a = ['hotspurs', 'rule', 'gunners', 'drool']
print(a)

# now lets print each item in the list:
print(a[0])
print(a[1])
print(a[2])
print(a[3])

# but what if you don't know how many slices there are?
# use the len function to find the number of slices
b=len(a)
print("list a has "+ str(b) +" slices.\n")

# here's a way to print each slice regardless of how many:
for w in a:
   print(w)



