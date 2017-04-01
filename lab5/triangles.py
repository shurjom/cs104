# Lab 5, CS104 Triangles
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.8.15>

# imports
from __future__ import division, print_function
input = raw_input

# constants defined here
s1 = float(input("Enter length of side 1:")) #input section for the three sides of the triangle
s2 = float(input("Enter length of side 2:"))
s3 = float(input("Enter length of side 3:"))

# functions defined here
def isEquilateral(s1, s2, s3): #function definition for equilateral triangle
    if s1 == s2 and s2 == s3:
        return(True)
    else:
        return(False)

def isIsosceles(s1, s2, s3): #function definition for isosceles triangle
    if s1 == s2 or s2 == s3 or s3 == s1:
         return(True)
    else:
        return(False)
        
def isScalene(s1, s2, s3): #function definition for scalene triangle
    if s1 != s2 and s2 != s3:
         return(True)
    else:
        return(False)
        

# ----------------- main code ------------------------
if isEquilateral(s1, s2, s3) == True: #function call for each of the triangle types
    print("The triangle is an Equilateral.")
elif isIsosceles(s1, s2, s3) == True:
    print("The triangle is an Isosceles.")
elif isScalene(s1, s2, s3) == True:
    print("The triangle is an Scalene.")



