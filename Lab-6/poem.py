#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:41:09 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 14 Oct 2024   
# Description:  python program to read the text file, process the text file and store the data in the text file like , first line is the name of poem, then auther name and 
# count of the line, and create the file called output.txt and save the result in the file.

# Additional information - Program import the of library to work with file operations and then read the txt file, ge the desire result and by using the open function,
# write the output file and save at same python file location.    

Below are the setps performed to generate the results: 
# Step 1: initilize the variable
# Step 2: get the file name from user
# Step 3: give the message if file incorrect
# Step 4:  read the txt file and save the data into the variable
# Step 5:  write the output.txt file and save the output and display the result on console.

"""

#######################( Import Library )#############################################
 
import os

 

########################( Write the code )##############################################

def main():
    # Variable to store the poem's title
    poem_title = ""
    # Variable to store the poem's author
    poem_author = ""
    # List to store the lines of the poem
    poem_lines = []
    # Variable to store the file name
    file_name = ""

    # Prompt for the file name and check for existence
    while True:
        file_name = input("Please input the name of the poem you wish summarized: ")
        if os.path.isfile(file_name):
            break
        else:
            print(f"{file_name} does not exist! Please input the name of the poem you wish summarized.")

    # Open the file for reading
    with open(file_name, 'r') as file:
        # Read and store the name of the poem
        poem_title = file.readline().strip()
        print('--->>>',poem_title)
        
        
        # Read and store the author of the poem
        poem_author = file.readline().strip()
        print('--->>>',poem_author)
        
        # Read each line of the poem and store it in the list
        poem_lines = [line.strip() for line in file.readlines()]
        print('--->>>',poem_lines)

    # Open Output.txt for writing
    with open('Output.txt', 'w') as output_file:
        # Write the summary information to Output.txt
        output_file.write(f"The name of the poem is {poem_title}\n")
        output_file.write(f"The author of the poem is {poem_author}\n")
        output_file.write(f"The number of lines in the poem is {len(poem_lines)}\n")
        output_file.write("A preview of the poem is: \n")
        
        # Write the first three lines of the poem
        for line in poem_lines[:3]:
            output_file.write(line + "\n")

    print(f"Summary of the poem '{poem_title}' has been written to Output.txt.")

# Call the main function
if __name__ == "__main__":
    main()


#########################( Result )#############################################
 
# Please input the name of the poem you wish summarized: Snowball
# Snowball does not exist! Please input the name of the poem you wish summarized.
# Please input the name of the poem you wish summarized: Snowball.txt
# --->>> Snowball
# --->>> Shel Silverstein
# --->>> ['I made myself a snowball', 'As perfect as could be.', 'I thought I’d keep it as a pet', 'And let it sleep with me.', 'I made it some pajamas', 'And a pillow for its head.', 'Then last night it ran away,', 'But first-it wet the bed.']
# Summary of the poem 'Snowball' has been written to Output.txt.

# Output file 
# The name of the poem is Snowball
# The author of the poem is Shel Silverstein
# The number of lines in the poem is 8
# A preview of the poem is: 
# I made myself a snowball
# As perfect as could be.
# I thought I’d keep it as a pet

######################################################################
