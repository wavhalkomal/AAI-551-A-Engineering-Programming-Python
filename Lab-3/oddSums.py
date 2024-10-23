#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:38:09 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 23 Sept 2024  
# Description:  python program to 

"""
 

import random

# Generate the first random integer between 1 and 10
first_number = random.randint(1, 10)

# Generate the second random integer between 11 and 20
second_number = random.randint(11, 20)

# Ensure the first number is less than the second number for proper range
lower_bound = min(first_number, second_number)
upper_bound = max(first_number, second_number)

# Initialize a variable to store the sum of odd numbers
odd_sum = 0

# Compute the sum of all odd integers between the two random integers
for number in range(lower_bound, upper_bound + 1):
    if number % 2 != 0:  # Check if the number is odd
        odd_sum += number

# Display the random integers and the sum
print(f"The random integers are: {first_number} and {second_number}.")
print(f"The sum of all odd integers between {lower_bound} and {upper_bound} is: {odd_sum}.")


print(f"The first random number was {lower_bound} , the second random number was {upper_bound}, and the sum is {odd_sum}.")

###################################################################### 

# he random integers are: 5 and 17.
# The sum of all odd integers between 5 and 17 is: 77.
# The first random number was 5 , the second random number was 17, and the sum is 77.

######################################################################

