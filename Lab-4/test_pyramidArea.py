#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:34:16 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 29 Sept 2024  
# Description:  python program to 

# Additional information - 
To run the tests, make sure you have PyTest installed. 
You can execute the tests from the terminal with the command: pytest test_pyramidArea.py


"""

import pytest
import PArea as pa  # Assuming your pyramid area calculations are in this file


# # Test calcBaseArea() with a valid number
def test_calcBaseArea():
    
    print('1. running ------>>>>> test_calcBaseArea ')    
    resultval = pa.calcBaseArea(15)
    print('test file resultval - ', resultval )  
    
    assert resultval == 225

# # ###########################################################################

# Test calcBaseArea() with a invalid number
@pytest.mark.xfail(raises=RuntimeError)
def test_calcBaseAreaText():
    
    print('running ------>>>>> test_calcBaseAreaText ') 
    
    pa.calcBaseArea("5")  # This should raise a TypeError

# ###########################################################################

# Test calcSideAreaBetween() to ensure the result is between specific values
def test_calcSideAreaBetween():
    
    print('3. running ------>>>>> test_calcSideAreaBetween ')
    
    result = pa.calcSideAreaBetween(15, 5)
    assert 270.41 < result < 270.42

# ###########################################################################
### Test calcSideAreaBetween() to ensure the result is rounded correctly
def test_calcSideAreaRound():
    
    result = pa.calcSideAreaBetween(10, 3)
    print(result)
    print('4. running ------>>>>> test_calcSideAreaRound ')
    
    assert round(result, 2) == 270.42


# ###########################################################################

# # Test prntSurfArea() to skip the test since it prints output
@pytest.mark.skip(reason="Only prints text to the screen.")
def test_prntSurfArea():
    
    print('5. running ------>>>>> test_calcSideAreaRound ')
    
    pa.prntSurfArea(225, 270.42)  # This will be skipped

# ###########################################################################


if __name__ == "__main__": 
    pytest.main()



###################################### PArea Code ##########################################################################
# def calcBaseArea(side): 
#     print('----komal----')
#     resultval = side ** 2
    
#     print('PArea resultval - ', resultval )   
#     return( resultval )

# def calcSideAreaBetween(side, height):  
        
#     # Area of one triangle face of the pyramid
#     slant_height = (height ** 2 + (side / 2) ** 2) ** 0.5  # Using Pythagorean theorem
#     triangle_area = (side * slant_height) / 2  # Area of one triangle
#     triangle_area_val =  4 * triangle_area 
    
#     return(triangle_area_val) # There are 4 triangular faces

# def prntSurfArea(base_area, side_area): 
    
#     total_surface_area = base_area + side_area
#     print(f"The total surface area of the pyramid is: {total_surface_area:.2f}")


################################################################################################################

 

