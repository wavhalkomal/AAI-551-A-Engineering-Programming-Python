# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:37:14 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 23 Sept 2024  
# Description:  python program to converts a user specified
number in the range of 1-9, inclusively, into the equivalent Roman numeral 

"""


from sys import exit 

# script to prompt the user for a number in the range of 1-9
user_input = input("Please enter a number between 1 and 9: ")

# Convert the input to an integer
try:
    number = int(user_input)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
    exit()

# Determine the Roman numeral equivalent using if, elif, else statements
if number == 1:
    roman_numeral = "\u2160"  # code should give the result I
    message = "The Roman numeral for 1 is " + roman_numeral 
elif number == 2:
    roman_numeral = "\u2161"  #  code should give the resultII
    message = "The Roman numeral for 2 is " + roman_numeral 
elif number == 3:
    roman_numeral = "\u2162"  # code should give the result III
    message = "The Roman numeral for 3 is " + roman_numeral 
elif number == 4:
    roman_numeral = "\u2163"  # code should give the result IV
    message = "The Roman numeral for 4 is " + roman_numeral 
elif number == 5:
    roman_numeral = "\u2164"  # code should give the result V
    message = "The Roman numeral for 5 is " + roman_numeral 
elif number == 6:
    roman_numeral = "\u2165"  # code should give the result VI
    message = "The Roman numeral for 6 is " + roman_numeral 
elif number == 7:
    roman_numeral = "\u2166"  # code should give the result VII
    message = "The Roman numeral for 7 is " + roman_numeral 
elif number == 8:
    roman_numeral = "\u2167"  # code should give the result VIII
    message = "The Roman numeral for 8 is " + roman_numeral 
elif number == 9:
    roman_numeral = "\u2168"  # code should give the result IX
    message = "The Roman numeral for 9 is " + roman_numeral 
else:
    print("Error: The number is outside the range of 1 to 9.")
    exit()

# Output the Roman numeral along with the message
print(message)

######################################################################

# Please enter a number between 1 and 9: 4
# The Roman numeral for 4 is Ⅳ
 
# Please enter a number between 1 and 9: 10
# Error: The number is outside the range of 1 to 9.

######################################################################



