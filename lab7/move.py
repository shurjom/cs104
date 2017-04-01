# Lab 7, CS104 Go Robot Go
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.22.15>

from __future__ import division, print_function
input = raw_input

from myro import *


# constants defined here.

# Number of centimeters the Scribbler travels in 1 second.
CENTS_PER_SEC = 17
# Number of degrees the Scribbler turns (at full speed) in 1 second.
# (It takes 1.35 seconds to turn 180 degrees.)
DEGS_PER_SEC = 180 / 1.35

# functions defined here.

def travelForw(dist):
    """Make scribbler go forward for dist centimeters.
    """
    secsPerCent = 1 / CENTS_PER_SEC
    # Go forward for dist centimeters, at full speed.
    forward(1.0, dist * secsPerCent)
    
def travelBack(dist):
    """Make scribbler go backward for dist centimeters.
    """
    secsPerCent = 1 / CENTS_PER_SEC
    # Go backward for dist centimeters, at full speed.
    backward(1.0, dist * secsPerCent)

def turnLeftDegrees(degs):
    """Make scribbler turn left the given number of degrees."""
    secsPerDegr = 1 / DEGS_PER_SEC
    turnLeft(1.0, degs * secsPerDegr)

def turnRightDegrees(degs):
    """Make scribbler turn right the given number of degrees."""
    secsPerDegr = 1 / DEGS_PER_SEC
    turnRight(1.0, degs * secsPerDegr)
    
def turnDegrees(degs):
    """Turn the optimal degrees, either left or right, anywhere from
    0 to 180.  Negative values mean turn right, positive values, turn left.
    """
    degs = degs % 360
    if degs == 0:
        return
    if degs > 180:
        turnRightDegrees(360 - degs)
    else:
        turnLeftDegrees(degs)

def executeInstructions(instr):
    """Interpret instructions in the format f02b02... using while loop and carries uot commands defined previously"""
    done = False
    currIdx = 0
    while not done:    
        cmd = instr[currIdx]
        val = int((instr[currIdx + 1:currIdx + 3]))
        print (cmd, val)
        currIdx += 3
         
        if currIdx >= len(instr):
             done = True
             
        if cmd == 'f':
            travelForw(val)   
        elif cmd == 'b':
            travelBack(val)
        elif cmd == 'l':
            turnLeftDegrees(val)
        elif cmd == 'r':
            turnRightDegrees(val)
        elif cmd == 'B':
            robot.beep(val, 880, 660)
        else:
             print("Unrecognized instr", instr)
    print("Done!  Hope you enjoyed yourself.")

    
