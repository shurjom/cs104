# Lab 1, CS104 Drawing sine wave curves lab
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <9.25.15>

import math #importing math library in code
import turtle #importing turtle graphics library into code

wn = turtle.Screen() #assigning name to reference turtle screen
wn.setworldcoordinates(0,-1,360,1) #assigning values to coordinate system 
wn.bgcolor('hotpink') #assigning color to background because of Oshomah (his favorite color)
fred = turtle.Turtle() 

for angle in range(360): #assigning value to range of degrees
    y = math.sin(math.radians(angle)) #using sin function from math library to report values for function of angle
    fred.goto(angle, y) #using turtle goto function to map sin curve on screen

wn.exitonclick() #to exit by clicking on screen

