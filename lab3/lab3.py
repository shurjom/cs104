#
# CS104 Lab 3: Drawing shapes with Myro
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <9.25.15>
#

from __future__ import division, print_function
input = raw_input
from myro import *    # pull everything from myro library into this program

# connect to the robot
init("COM41")

#Assigns values to variables used to control the scribbler
numSeconds = 0.1
leftSeconds = 0.5
speed = 0.5
numTimes = 30

for i in range(numTimes): #for loop allows for the process to continue for 30s
    forward(speed, numSeconds)
    turnLeft(speed, leftSeconds)
    #increases the value of time that scribbler goes forward by increments of 0.1
    numSeconds =( numSeconds + 0.1)
  
    
