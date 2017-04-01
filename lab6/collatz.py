# Lab 6, CS104 3n+1 sequence
# <Oshomah Agbugui (ota2) 2355813, Shurjo Maitra (sm47) 2356985
# <15th October, 2015>
from __future__ import division, print_function
input = raw_input


# constant definitions here


# function definitions here 
def seq3np1(n):
    """ Print the 3n+1 sequence from n, terminating when it reaches 1."""
    
    count=0
    while n != 1:
        count += 1
        if n % 2 == 0:        # n is even
            n = n // 2
            
        else:                 # n is odd
            n = n * 3 + 1
            
    return(count)              # the last print is 1  

# --------- main program -------------
  
maxsofar=0
for start in range (1,51):
    result = seq3np1(start)
    if result > maxsofar:   #finds the largest count 
        maxsofar=result

print("Longest collatz sequence found has", maxsofar,"steps")         #prints the largest count