# Lab 5, CS104 Approximating pi
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.8.15>

from __future__ import division, print_function
input = raw_input

import turtle
import math
import random

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1) #sets up drawing are

fred = turtle.Turtle() #defines turtle
fred.up()
fred.tracer(1000)




numdarts = 1000 #gives number of points on the drawing are
insideCount = 0
for i in range(numdarts):
    
    randx = random.random()*2-1 
    randy = random.random()*2-1
    
    fred.goto(randx, randy)   
    
    
    if fred.distance(0,0) <=1:   
        fred.color('red')
        fred.dot()
        insideCount+=1              #counts all points with distance less than or equal to 1
        
    else:
        fred.color('blue')          #counts all points with distance greater than 1
        fred.dot()
        
    
pi =float((insideCount/numdarts)*4) #calculates pi
print(pi)                           #prints pi
print(insideCount)                  #prints points inside
    

wn.exitonclick()