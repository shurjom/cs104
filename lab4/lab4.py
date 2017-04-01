# Lab 1, CS104 Drawing sine wave curves lab
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.1.15>

# imports
from __future__ import division, print_function
input = raw_input
from myro import *

# connect to the robot
init("COM40")

# constants defined here
CENTS_PER_SEC = 19 # the distance traveled by the scribbler in 1s
DEGS_PER_SEC = 130

# functions defined here
def travelForw(dist):                   #function definition for going forward dist cm
    secsPerCent = dist / CENTS_PER_SEC
    forward(1, secsPerCent)
    
def travelBack(dist):
    secsPerCent = dist / CENTS_PER_SEC   #function definition for going backward dist cm
    backward(1, secsPerCent)
    
def turnLeftDegrees(degrees):
    secsPerDeg = degrees / DEGS_PER_SEC   #function definition for turning left "degrees" 
    turnLeft(1, secsPerDeg)

def turnRightDegrees(degrees):
    secsPerDeg = degrees / DEGS_PER_SEC    #function definition for turning right "degrees"
    turnRight(1, secsPerDeg)

def drawNgon(numSides, sideLen):         #function definition for drawing n sided polygon 
    for i in range(numSides):
        degrees = 360 / numSides
        travelForw(sideLen)
        turnLeftDegrees(degrees)
 
        
# ----------------- main code -----------------------

numSides = int(input("Enter number of sides for polygon: ")) #asking for input for number of sides of polygon and side length
sideLength = float(input("Enter length of each side, in cm: "))

drawNgon(numSides, sideLength) # carrying out function with given values


