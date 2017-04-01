# Lab 1, CS104
# Student 1. Shurjo Maitra (sm47), Student 2. Oshomah Agbugui (ota2)
# <9.17.15>

from __future__ import division, print_function
input = raw_input

print ("This program will allow you to convert days to weeks.")
totaldays = (input("Enter a number of days:")) #asks for value of days user wants to convert

weeks = (int(totaldays) // 7) #calculates number of weeks in totaldays
days = (int(totaldays) % 7) #calculates number of days after weeks for totaldays

print (totaldays, "days is", weeks, "weeks and", days, "days.") #reports number of weeks and days in totaldays inputed