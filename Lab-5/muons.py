#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:53:06 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 06 Oct 2024  
# Description:  python program to calculate  

# Additional information - 

Step 1: Initialized the constant GRID_SIZE is set to 8, representing the dimensions of the grid.
Step 2: Created an 8x8 two-dimensional List of integers with the value 0 using nested list comprehensions.
Step 3: Iterated over the entire two-dimensional List and for each slot assign a random value in the range of 0-500, inclusively
Step 4: Initialized variables to track the highest and lowest capture rates
Step 5: Iterated through the grid. For each rate, it checks if it’s the highest or lowest found so far and updates the corresponding variables if it is.
Step 6: Printed out the two-dimensional List 
Step 7: To have multiple outputs print on the same line added the end=” “
"""
 
import random

def main():
    # Constants
    GRID_SIZE = 8
    
    # Create an 8x8 grid initialized to 0
    capture_rates = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Assign random values between 0 and 500 to the grid
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            capture_rates[i][j] = random.randint(0, 500)
    
    # Initialize variables to track the highest and lowest capture rates
    highest_rate = -1
    lowest_rate = 501  # Set higher than the max possible value
    highest_x, highest_y = 0, 0
    lowest_x, lowest_y = 0, 0

    # Iterate through the grid to find the highest and lowest capture rates
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rate = capture_rates[x][y]
            # Update highest rate and coordinates
            if rate > highest_rate:
                highest_rate = rate
                highest_x, highest_y = x, y
            # Update lowest rate and coordinates
            if rate < lowest_rate:
                lowest_rate = rate
                lowest_x, lowest_y = x, y

    # Output the results
    print(f"Highest capture rate: {highest_rate} at coordinates ({highest_x + 1}, {highest_y + 1})")
    print(f"Lowest capture rate: {lowest_rate} at coordinates ({lowest_x + 1}, {lowest_y + 1})")
    
    # Print the grid
    print("\nCapture Rates Grid:")
    for row in capture_rates:
        for value in row:
            print(f"{value:3}", end=" ")  # Print each value formatted
        print()  # Newline after each row

if __name__ == "__main__":
    main()



#######################( Result) ######################

# Highest capture rate: 499 at coordinates (1, 8)
# Lowest capture rate: 1 at coordinates (7, 5)

# Capture Rates Grid:
# 356 245 359 209 204  78 240 499 
# 329  99  12 417 132 364 347 396 
# 473 438  40 385 230 413 496 163 
# 215  14  28 178 196 377  94 341 
# 433 174 334  75 216 275  11 275 
# 289 221 417 234 339 258 363 470 
# 396 484 204 282   1 137 400 424 
# 368 455  43 170 197 126 406  69 


#########################################################

