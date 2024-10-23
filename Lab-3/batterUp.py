#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 00:37:14 2024

@author: komalwavhal
# Author: Komal Wavhal
# Date: 23 Sept 2024  
# Description:  python program to 

"""
 
import random

# Generate a random integer in the range of 0 to 450
distance = random.randint(0, 450)

# Determine the outcome based on the distance
if distance > 400:
    message = f"The batter hit the ball {distance} feet! It's a home run! The batter scored a run for the team."
elif 135 <= distance <= 400:
    message = f"The batter hit the ball {distance} feet into the outfield and made it to third base."
elif 10 <= distance <= 134:
    message = f"The batter hit the ball {distance} feet into the infield and made it to second base."
elif 1 <= distance <= 9:
    message = f"The batter bunted the ball {distance} feet and made it to first base."
else:  # distance == 0
    message = "The batter made a strike."

# Output the result
print(message)



######################################################################

# The batter bunted the ball 3 feet and made it to first base.
# The batter hit the ball 218 feet into the outfield and made it to third base.
# The batter hit the ball 167 feet into the outfield and made it to third base.
# The batter hit the ball 222 feet into the outfield and made it to third base.
# The batter hit the ball 182 feet into the outfield and made it to third base.
# The batter hit the ball 418 feet! It's a home run! The batter scored a run for the team.
# The batter hit the ball 265 feet into the outfield and made it to third base.
# The batter hit the ball 97 feet into the infield and made it to second base.
# The batter hit the ball 171 feet into the outfield and made it to third base.
# The batter hit the ball 59 feet into the infield and made it to second base.
# The batter hit the ball 60 feet into the infield and made it to second base.
# The batter hit the ball 449 feet! It's a home run! The batter scored a run for the team.
# The batter hit the ball 401 feet! It's a home run! The batter scored a run for the team.

######################################################################
