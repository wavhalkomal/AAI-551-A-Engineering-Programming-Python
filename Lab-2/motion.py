#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:05:23 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 16 Sept 2024  
# Description:  python program to calculate velocity, 
average velocity, and displacement of an object, given the amount of time elapsed. 

"""


####result variable declaration 
velocity = 0
average_velocity = 0 
displacement = 0


# Useful values:
acceleration = 5.25
initialVelocity = 8.25
time = 10.0

# Calculate the properties of the object:

velocity = initialVelocity + acceleration * time
displacement = initialVelocity * time + 0.5 * acceleration * time**2
average_velocity = displacement / time    
     

# Print the results:
 
print(" Time : ", time)
print(" velocity: ", velocity)
print(" average velocity: ", average_velocity)
print(" displacement: ", displacement)
  