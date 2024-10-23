#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:07:36 2024

@author: komalwavhal
"""

time =  float(input("An appropriate prompt for information ")) 

print("Time value is :", time)

####result variable declaration 
velocity = 0
average_velocity = 0 
displacement = 0

# Useful values:
acceleration = 5.25
initialVelocity = 8.25 

# Calculate the properties of the object:

velocity = initialVelocity + acceleration * time
displacement = initialVelocity * time + 0.5 * acceleration * time**2
average_velocity = displacement / time    
     
# Print the results:
 
print(" Time : ", time)
print(" velocity: ", velocity)
print(" average velocity: ", average_velocity)
print(" displacement: ", displacement)
  
### got error when the flote was not added in input time value   
# velocity = initialVelocity + acceleration * time
###TypeError: can't multiply sequence by non-int of type 'float'

## error resolved by adding float

# An appropriate prompt for information 15.5
# Time value is : 15.5
#  Time :  15.5
#  velocity:  89.625
#  average velocity:  48.9375
#  displacement:  758.53125

