#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:53:06 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 06 Oct 2024  
# Description:  python program for recording the distances the projectile
flies for a number of trials.

# Additional information - Python program to record the distances the projectile
flies for a number of trials, and keeping track of the three trials with the furthest distance using Lists.

Below are the setps performed to generate the results 
# Step 1: top_distances and trial_numbers, are initialized to keep track of the top three distances and their corresponding trial numbers.
# Step 2: A while loop continues to prompt the user for distances until they choose to stop. 
# Step 3: Condition using if/elif/else statements determine the new distance 
# Step 4: Prompt the user if they wish to enter another distance & trial number, If yes then add conditions  
# Step 5: increment the trial number 
# Step 6: print the output 
    
"""
 
    

def main():
    # Initialize lists for the top three distances and their trial numbers
    top_distances = [0, 0, 0]
    trial_numbers = [0, 0, 0]
    
    # Variable to control the loop
    continue_input = "Y"
    trial_number = 1

    # Loop for user input
    while continue_input.upper() == "Y":
        # Prompt for the distance
        distance = int(input(f"Enter the distance for trial {trial_number}: "))
        
        # Update the top distances and trial numbers based on the new distance
        if distance > top_distances[0]:
            # Shift the current distances down the list
            top_distances[2] = top_distances[1]
            trial_numbers[2] = trial_numbers[1]
            top_distances[1] = top_distances[0]
            trial_numbers[1] = trial_numbers[0]
            # Update the top distance and trial number
            top_distances[0] = distance
            trial_numbers[0] = trial_number
        elif distance > top_distances[1]:
            # Shift the second to third
            top_distances[2] = top_distances[1]
            trial_numbers[2] = trial_numbers[1]
            # Update the second distance and trial number
            top_distances[1] = distance
            trial_numbers[1] = trial_number
        elif distance > top_distances[2]:
            # Update the third distance and trial number
            top_distances[2] = distance
            trial_numbers[2] = trial_number

        # Ask if the user wants to enter another trial
        continue_input = input("Would you like to enter another trial? (Y/N): ")
        
        # Increment trial number
        trial_number += 1

    # Output the results
    print("\nTThe top three distances for the trebuchet are:")
    print(f"{'Trial':<10} {'Distance':<10}")
    for i in range(3):
        if trial_numbers[i] != 0:  # Only display valid trials
            print(f"{trial_numbers[i]:<10} {top_distances[i]:<10}")

if __name__ == "__main__":
    main()




################# (Result) #####################
# Enter the distance for trial 1: 298
# Would you like to enter another trial? (Y/N): Y
# Enter the distance for trial 2: 305
# Would you like to enter another trial? (Y/N): Y
# Enter the distance for trial 3: 301
# Would you like to enter another trial? (Y/N): Y
# Enter the distance for trial 4: 312
# Would you like to enter another trial? (Y/N): Y
# Enter the distance for trial 5: 307
# Would you like to enter another trial? (Y/N): N

# The top three distances for the trebuchet are:
# Trial      Distance  
# 4          312       
# 5          307       
# 2          305  

###################################################



