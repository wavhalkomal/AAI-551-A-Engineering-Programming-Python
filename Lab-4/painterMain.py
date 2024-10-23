#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:34:16 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 29 Sept 2024  
# Description:  python program to prompts user for art choice and border symbol.


# Additional information - to run the program no need to open the painterfunc python file, directly execute the main file and main file will cann the function
# from the file which is imported on line 21 (import painterFuncs as pf) to make this more easier we 
# added the alies pf and used it as an object to call function. 


"""



import painterFuncs as pf

def main():
    """Coordinates the overall execution of the painting printer."""
    choice, border = pf.intro()
 
    if choice == 1:
        pf.sleepingCat(border)
    elif choice == 2:
        pf.sailingShip(border)
    elif choice == 3:
        pf.guitar(border)
    elif choice == 4:
        pf.teddy_bears(border)
    else:
        pf.blank(border)
        print("Hmmmm....we don't seem to have that painting.")
        exit(-1)

    print("I hope you enjoyed your art!")


if __name__ == "__main__":
    main()








