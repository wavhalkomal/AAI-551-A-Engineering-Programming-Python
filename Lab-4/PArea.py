#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:12:44 2024

@author: komalwavhal
"""

     
def calcBaseArea(side): 
    print('----komal----')
    resultval = side ** 2
    
    print('PArea resultval - ', resultval )   
    return( resultval )

def calcSideAreaBetween(side, height):  
        
    # Area of one triangle face of the pyramid
    slant_height = (height ** 2 + (side / 2) ** 2) ** 0.5  # Using Pythagorean theorem
    triangle_area = (side * slant_height) / 2  # Area of one triangle
    triangle_area_val =  4 * triangle_area 
    
    return(triangle_area_val) # There are 4 triangular faces

def prntSurfArea(base_area, side_area): 
    
    total_surface_area = base_area + side_area
    print(f"The total surface area of the pyramid is: {total_surface_area:.2f}")

