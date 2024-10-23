#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:41:09 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 14 Oct 2024   
# Description:  python program to read from this file, compute the
# average of these integers in the file (reading from the file), and then print out the average of these integers.

# Additional information - Program will read the text file name numbers.txt saved in the same location as the python file, if the file on other location
# then we have to give the full fath of text file to access it. Reading the file and performing data processing on it and calculatng the average of the integers 
# present in the text file. 

Below are the setps performed to generate the results: 
# Step 1: Open the file
# Step 2: Process the file
# Step 3: Close the file and compute the average
# Step 4: Call the main function
# Step 5: display the result on console 

"""
 
 

########################( Write the code )##############################################
def main():
    # Step 1: Open the file
    try:
        with open('numbers.txt', 'r') as file:
            total = 0
            count = 0
            
            # Step 2: Process the file
            for line in file:
                # Strip any newlines and print the line
                number = line.strip()
                print(number)
                
                # Parse the value and update total and count
                total += int(number)
                count += 1

    except FileNotFoundError:
        print("The file numbers.txt was not found.")
        return

    # Step 3: Close the file and compute the average
    if count > 0:
        average = total / count
        print(f"The average of the numbers is {average:.2f}")
    else:
        print("No numbers to average.")

# Call the main function
if __name__ == "__main__":
    main()

#########################( Result )#############################################

# 13
# 42
# 19
# 352
# 17
# 652
# 53
# 84
# 35
# The average of the numbers is 140.78

######################################################################
