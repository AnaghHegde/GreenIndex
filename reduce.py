#!/usr/bin/python
from numpy import *
from cv2 import *
import sys 
import fileinput

count=1
count1=1
def convert(r, g, b):
	
	r=r/255.0
	b=b/255.0
	g=g/255.0
	cm=maximum(maximum(r,g),b)
	cl=minimum(minimum(r,g),b)
	#print r,g,b
	c=cm-cl
	
	if c==0:
		h=0
	elif cm==r:
		h=((g-b)/c)%6
		
	elif cm==g:
		h=2.0+((b-r)/c)
	elif cm==b:
		h=4.0+((r-g)/c)
		
	h=h*60
	return h

for line in sys.stdin:
    # remove leading and trailing whitespace
	#line = line.strip()
    # parse the input we got from mapper.py
	a,b,c,a1,b1,c1 = line.split(' ')
	
	r=int(a)
	g=int(b)
	b=int(c)
	r1=int(a1)
	g1=int(b1)
	b1=int(c1)
	#print r,g,b,r1,g1,b1
	px=convert(r,g,b)
	px1=convert(r1,g1,b1)
	
	if(80<=px<=140 or (30<=b<=60 and 30<=r<=60 and 30<=g<=60) ):
		count+=1
		#print count
	if(80<=px1<=140 or (30<=b<=60 and 30<=r<=60 and 30<=g<=60) ):
		count1+=1
		#print count
		
print "Green Pixels 1 "+str(count)	
print "Green Pixels 2 "+str(count1)		
print (count*1.0/count1) 	
