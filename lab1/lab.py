#
# Lab 1, CS104
# <Shurjo Maitra (sm47), Oshomah Agbugui (ota2)>
# <9/10/15>

from __future__ import division, print_function
input = raw_input
from myro import *

init("COM40")
print("Done connecting")

# Make the robot draw a circle by making the left wheel
# go forward at speed 0.4, and the right wheel go forward
# at speed 0.75.  Stop the robot after 30 seconds.
print("Issuing motors command")
robot.motors(0.4, 0.75)
print("Doing nothing for 20 seconds")
wait(20)
print("Issuing stop command")
stop()
print("Done")