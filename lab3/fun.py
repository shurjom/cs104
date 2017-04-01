from __future__ import division, print_function
input = raw_input
from myro import *    # pull everything from myro library into this program

# connect to the robot
init("COM41")

motors(2,2)
for i in range(4):
    forward(1,1)
    turnLeft(1,1)
