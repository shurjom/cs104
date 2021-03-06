# Lab 6, CS104 Moving function definitions
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.15.15>

from __future__ import division, print_function
input = raw_input
from myro import *


#File contains functions to enhance scribbler movement

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

def turnDegrees(degs):                  #function definition for turning "degrees"
    degs = degs % 360
    if degs == 0:
        return()
    elif degs <= 180:
        turnLeftDegrees(degs)
    elif degs > 180:
        turnRightDegrees(360-degs)


# --------- main program -------------
