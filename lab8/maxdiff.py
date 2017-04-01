# Lab 8, CS104 Max increase in list
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.29.15>

# imports here
from __future__ import division, print_function
input = raw_input 

# Constants here (if any)

# Function declarations here (if any)

# main code here.
def findMaxDiff(lst):
    "Finds the max difference between 2 consecutive items in a list"
    maxdiff = 0
    for i in range(len(lst) - 1):       #loop for finding the max diff.
        diff = lst[i + 1] - lst[i]
        if diff > maxdiff:
                maxdiff = diff
    return maxdiff

lst = [2,3,2,4,1,500]           #declares in the used list in the function
print(findMaxDiff(lst))

