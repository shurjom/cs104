# Lab 6, CS104 Moving using user input
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.15.15>

from __future__ import division, print_function
input = raw_input
from move import *

# constant definitions here
dist = 10
degrees = 90

# function definitions here 
def getCommand():
    print ("Commands:")
    print ("f or F for forward,")
    print ("b or B for backward, ")
    print ("l or L for left turn of 90 degrees, ")
    print ("r or R for a right turn of 90 degrees")
    print ("t or T for a turn, and ")
    print ("q or Q for quit.")
    print ("Enter a command:")
    return input()

#turning function from user input
def getTurnAmount():
    return float(input("Enter amount to turn:"))

# --------- main program -------------
#initializes the com port
init("COM40")
done = False

# carries out commands based on the user inputed command
while not done:
    command = getCommand()
    print (command)
    if command == "q" or command == "Q":
        done = True
    elif command == "f" or command == "F":
        travelForw(dist)
    elif command == "b" or command == "B":
        travelBack(dist)
    elif command == "l" or command == "L":
        turnLeftDegrees(degrees)
    elif command == "r" or command == "R":
        turnRightDegrees(degrees)    
    elif command == "t" or command == "T":
        turnDegrees(getTurnAmount())    
    else:
        print ("Command not implemented yet.")
   
  



