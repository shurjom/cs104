# Lab 8, CS104 Max increase in list
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <10.29.15>

# imports here
from __future__ import division, print_function
input = raw_input 
# Constants here (if any)

# Function declarations here (if any)
def isPrime(maxVal):
    'Function returns True if n is prime and False otherwise'
    for i in range(2, int(maxVal/2) + 1):
        result = maxVal % i
        if result == 0:
            return False
    return True

def genPrimesList(topVal):
    'Function generates a list of primes up to the value entered by user'
    PrimesList = []
    for i in range(2, topVal):
        if isPrime(i) == True:
            PrimesList.append(i)
    return PrimesList



# main code here.
maxVal = int(input("Enter a number:"))   
primesList = genPrimesList(maxVal)
print("Prime numbers up to", maxVal, "are", primesList)

count = 0
for e in range(4, maxVal + 1, 2):
    found = False
    for p in primesList:
        # finding the difference between 
        if (e - p) in primesList:
            found = True
            print("Found", e, "is the sum of primes", p, "and", e - p)
            break
    if found == False:
        print("Goldbach's conjecture is false for e")
        count += maxVal
print("Goldbach's conjecture holds for all even numbers up to the one in input ")
     
