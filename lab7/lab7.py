# Lab 7, CS104 Go Robot Go
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.22.15>

from __future__ import division, print_function
input = raw_input

from move import *
from myro import * 

# constants defined here.

# Distance scribbler should move forward or backward, by default.
DEFAULT_DIST = 10   # centimeters

# Default amount to turn for l or r instrs.
DEFAULT_TURN = 90   # degrees


# functions defined here.

def getcommand():    #prints out commands that the user can put in                                            
    """Print out a menu of commands and get the result from the user, and
    return it."""
    print("Legal Instructions: ")
    print("Use lowercase letters only. Except 'B' which is for Beep")
    print("Only use two digit numbers")
    print("  'f' for forward")
    print("  'b' backward")
    print("  'l' for left turn of 90 degrees")
    print("  'r' for right turn of 90 degrees")
    print("  'B' for beep")
    res = input("Enter your choice: ")
    return res


# ------------------- main program -------------------------
init("COM40") #initializes and refers to the command in move.py to carry out instructions 
instr = getcommand()
executeInstructions(instr)
