#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:41:09 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 14 Oct 2024   
# Description:  python program to read in a file containing numbers, separated (delimited) by commas and
converting those numbers into specific symbols that will create an ASCII art image.

# Additional information - Program read the image.txt and using loops, iterate on data and ifelse condition will help to get the correct data and convert it to ascii and then save output to the txt file.
 

Below are the setps performed to generate the results: 
# Step 1:  getFileName function to take the filename as a input from user, check if its correct format 
# Step 2:  read the data and using for loop add the ifelse condition and change the number to ASCII code
# Step 3:  using open function, write the data into the txt file by adding \n for next line 
# Step 4:   print output  

"""


#######################( Import Library )#############################################
  
import os

########################( Write the code )##############################################
 
def getFileName():
    while True:
        file_name = input("Please input the name of the file you wish to have painted: ")
        if os.path.isfile(file_name):
            return file_name
        else:
            print(f"{file_name} does not exist! Please input the name of the file you wish to have painted.")

def convertLine(line):
    line = line.strip()
    newLine = ""
    numbers = line.split(",")  # Split line into a list using comma as delimiter

    for num in numbers:
        if num == '1':
            newLine += ' '
        elif num == '2':
            newLine += ','
        elif num == '3':
            newLine += '_'
        elif num == '4':
            newLine += '('
        elif num == '5':
            newLine += 'O'
        elif num == '6':
            newLine += ')'
        elif num == '7':
            newLine += '-'
        elif num == '8':
            newLine += '"'
    
    return newLine

def processFile(filename):
    with open(filename, 'r') as input_file, open('painting.txt', 'w') as output_file:
        for line in input_file:
            newLine = convertLine(line)
            output_file.write(newLine + "\n")
 

#########################( Result )#############################################
 
# Please input the name of the file you wish to have painted: image
# image does not exist! Please input the name of the file you wish to have painted.
# Please input the name of the file you wish to have painted: image.txt
# image.txt does not exist! Please input the name of the file you wish to have painted.
# Please input the name of the file you wish to have painted: image.csv
# Your image can be found in painting.txt. Enjoy!

# painting.txt
#  ,_,
# (O,O)
# (   )
# -"-"------

######################################################################









