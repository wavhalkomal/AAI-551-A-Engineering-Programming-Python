#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:37:41 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 23 Sept 2024  
# Description:  python program to 

"""
 
import random

# Initialize the user's guesses
guesses_remaining = 3

# Set the x and y coordinates of the particle
x_coordinate = random.randint(1, 10)
y_coordinate = random.randint(1, 10)

# Game loop
while guesses_remaining > 0:
    
    print(f"The particle is somewhere in this space! You have {guesses_remaining} chances to guess it.")
    
    # Prompt user for their guess
    user_x = int(input("Guess the x coordinate (1-10)? : "))
    user_y = int(input("Guess the y coordinate (1-10)? : "))
    
    # Check if the user's coordinates are within bounds
    if user_x < 1 or user_x > 10 or user_y < 1 or user_y > 10:
        print("Your guess was outside the coordinate bounds. Please guess again.")
    else:
        # Check if the guess is correct
        if user_x == x_coordinate and user_y == y_coordinate:
            print("Congratulations! You guessed correctly and win!")
            break
        else:
            # Provide hints
            if user_x > x_coordinate:
                print("Your guess for x is too high.")
            elif user_x < x_coordinate:
                print("Your guess for x is too low.")
                
            if user_y > y_coordinate:
                print("Your guess for y is too high.")
            elif user_y < y_coordinate:
                print("Your guess for y is too low.")
    
    # Decrement the number of chances
    guesses_remaining -= 1
    
    # Check if the user has run out of chances
    if guesses_remaining == 0:
        print(f"Oh no! You ran out of chances. ({x_coordinate}, {y_coordinate}) was the particle's position!")
              # You've run out of chances! The correct position was ({x_coordinate}, {y_coordinate}).")



######################################################################

# The particle is somewhere in this space! You have 3 chances to guess it.
# Guess the x coordinate (1-10)? : 4
# Guess the y coordinate (1-10)? : 6
# Your guess for x is too high.
# Your guess for y is too low.
# The particle is somewhere in this space! You have 2 chances to guess it.
# Guess the x coordinate (1-10)? : 2
# Guess the y coordinate (1-10)? : 4
# Your guess for y is too low.
# The particle is somewhere in this space! You have 1 chances to guess it.
# Guess the x coordinate (1-10)? : 6
# Guess the y coordinate (1-10)? : 7
# Your guess for x is too high.
# Your guess for y is too low.
# Oh no! You ran out of chances. (2, 10) was the particle's position!

######################################################################





