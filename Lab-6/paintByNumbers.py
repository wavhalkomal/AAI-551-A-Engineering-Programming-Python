#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:41:09 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 14 Oct 2024   
# Description:  python program to read in a file containing numbers, separated (delimited) by commas and
converting those numbers into specific symbols that will create an ASCII art image.

# Additional information - Program to call main function and the to import the pnbfunction, call process file finction in it and generate the output result.  

Below are the setps performed to generate the results: 
# Step 1:  import the library
# Step 2:  call the main function
# Step 3:  get the input file name 
# Step 4:  print the output  

"""


#######################( Import Library )#############################################
  
import pbnFunctions
 
########################( Write the code )##############################################
 

def main():
    filename = pbnFunctions.getFileName()  # Get the input file name
    pbnFunctions.processFile(filename)      # Process the file
    print("Your image can be found in painting.txt. Enjoy!")

# Call the main function
if __name__ == "__main__":
    main()




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
