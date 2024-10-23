
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:34:16 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 29 Sept 2024  
# Description:  python program to calculate total surface area of a square pyramid:


# Additional information - you can directly run the program in idle and it will execute the program, no need to install any supporting library as 
# this are all simple math operations 


"""

     
def calcBaseArea(side):
    return side ** 2

def calcSideArea(side, height): 
    # Area of one triangle face of the pyramid
    slant_height = (height ** 2 + (side / 2) ** 2) ** 0.5  # Using Pythagorean theorem
    triangle_area = (side * slant_height) / 2  # Area of one triangle
    return 4 * triangle_area  # There are 4 triangular faces


def prntSurfArea(base_area, side_area): 
    total_surface_area = base_area + side_area
    print(f"Total surface area of the square pyramid is {total_surface_area:.2f} square feet.")

def main():
    """Main function to execute the program logic."""
    side = float(input("Enter the side length of the base of the square pyramid in feet: "))
    height = float(input("Enter the height of the square pyramid in feet: "))

    # Calculate base area
    base_area = calcBaseArea(side)
    print(f"Base surface area of the square pyramid is {base_area:.2f} square feet.")

    # Calculate side area
    side_area = calcSideArea(side, height)
    print(f"Total side area of the square pyramid is {side_area:.2f} square feet.")

    # Print the total surface area
    prntSurfArea(base_area, side_area)

if __name__ == "__main__":
    main()
 
    
    
    
    

"""
----------------Sample Output------------------
Enter the side length of the base of the square pyramid in feet: 15
Enter the height of the square pyramid in feet: 5
Base surface area of the square pyramid is 225.00 square feet.
Total side area of the square pyramid is 270.42 square feet.
Total surface area of the square pyramid is 495.42 square feet.

"""
    
    
    
    
    
    
    
    