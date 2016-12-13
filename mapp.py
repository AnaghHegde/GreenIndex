#!/usr/bin/python
from numpy import *
from cv2 import *
from sys import *
#img1,img2=raw_input().split(" ")


for line in stdin:
	continue

img1=imread('cubbon.jpg')
img2=imread('cubbon5.jpg')

row=img1.shape[0]
column=img1.shape[1]

row1=img2.shape[0]
column1=img2.shape[1]

def splitr():
	for i in range(0,row,2):
		array=[]
		array1=[]
		for j in range(0,column):
			b = img1[i,j]
			array.append(list(b))
			
			b1 = img2[i,j]
			array1.append(list(b1))
			
			b = img1[i+1,j]
			array.append(list(b))
			
			b1 = img2[i+1,j]
			array1.append(list(b1))			

		printfn(array,array1)

def printfn(ar,ar1):
	for i in range(len(ar)):
		print ar[i][0],ar[i][1],ar[i][2],ar1[i][0],ar1[i][1],ar1[i][2]
		
splitr()
