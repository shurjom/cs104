# Lab 1, CS104
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <9.17.15>

from __future__ import division, print_function
input = raw_input

print ("This program will allow you to calculate period of a simple pendulum")
import math #includes library in code

pi = 3.14159265 #assigns value to pi
g = 980 #assigns value to g

L = float(input("Enter pendulum length in cm:")) #asks user to input value of L
alpha = float(input("Enter angle of displacement in radians:")) # asks user to input value of alpha

print ("Pendulum length = ", L, "cm") #prints out user-inputed value of L
print ("Angle of displacement", alpha, "radians") #prints out user-inputed value of alpha

p = 2 * pi * (( L / g) ** 0.5) * (1 + ( 0.25 * (math.sin(alpha / 2)) ** 2)) #computes period based on given formula
print ("Period of pendulum is", p, "s") #reports period calculated