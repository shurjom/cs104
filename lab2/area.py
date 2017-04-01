# Lab 1, CS104
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <9.17.15>

from __future__ import division, print_function
input = raw_input

print ("Find the area a and circumference of a circle given a diameter.")
diameter = float(input("Enter a diameter in inches:")) #get value for diameter from user
pi = 3.14159265 #assigns value to pi

area = (((2.54 * diameter)/2) ** 2) * pi #area calculation
print ('Area = ', area,"cm^2") #prints value of area calculated
    
circumference = (2.54 * diameter) * pi #circumference calculation
print ('Circumference = ', circumference, "cm"),  # prints value of circumference calculated