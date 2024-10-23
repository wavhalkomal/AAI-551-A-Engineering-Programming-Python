#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:34:16 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 29 Sept 2024  
# Description:  python program to 

# Additional information - No need to run this file, python code from main file will import this functions and call from the printer main file. 

"""



def intro():
    """Introduces the program and prompts user for art choice and border symbol."""
    print("Welcome to the ASCII Art Painter!")
    print("Choose from the following options:")
    print("1. Sleeping Cat")
    print("2. Sailing Ship")
    print("3. Guitar")
    print("4. Teddy bears")

    choice = int(input("Enter the number of your choice (1-4): "))
    border = input("Enter a single symbol for the border: ")

    return choice, border

def printHeaderFooter(border, size):
    """Prints the border symbol size number of times."""
    print(border * size)

def sleepingCat(border):
    """Displays a sleeping cat ASCII art with the specified border."""
    cat_art = [
        "         |\ _,,,---,,_          ",
        " ZZZzz /,`.-'`' -. ;-;;,_       ",
        "      |,4- ) )- ,_. ,\ ( `'-'   ",
        "      '---''(_/--' `-'\_)       "
        
    ]
    size = 30
    printHeaderFooter(border, size)

    for line in cat_art:
        print(f"{border} {line} {border}")

    printHeaderFooter(border, size)

def sailingShip(border):
    """Displays a sailing ship ASCII art with the specified border."""
    ship_art = [
           "    |    |    |                  ",
           "   )_)  )_)  )_)                 ",
          "  )___))___))___)\\               ",
         " )____)____)_____)\\\\             ",
        " _____|____|____|____\\\\\\__       ",
        " \\    Satisfaction   /             ",
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^        "     
    ]
    size = 30
    printHeaderFooter(border, size)

    for line in ship_art:
        print(f"{border} {line} {border}")

    printHeaderFooter(border, size)

def guitar(border):
    """Displays another ASCII art choice with the specified border."""
    art_choice1 = [
"               _______       __                                              ",
"             /   ------.   / ._`_                                            ",
"            |  /         ~--~    \                                           ",
"            | |             __    `.____________________ _^-----^            ",
"            | |  I=|=======/--\=========================| o o o |            ",
"            \ |  I=|=======\__/=========================|_o_o_o_|            ",
"             \|                   /                       ~    ~             ",
"               \       .---.    .                                            ",
"                 -----'     ~~''                                             "
    ]      
    size = 30
    printHeaderFooter(border, size)

    for line in art_choice1:
        print(f"{border} {line} {border}")

    printHeaderFooter(border, size)

def teddy_bears(border):
    """Displays another ASCII art choice with the specified border."""
    art_choice2 = [
            "{~._.~}",
            " ( Y ) ",
            "()~*~()",
            "(_)-(_)"
    ]
    size = 30
    printHeaderFooter(border, size)

    for line in art_choice2:
        print(f"{border} {line} {border}")

    printHeaderFooter(border, size)

def blank(border):
    """Displays a blank canvas with the specified border."""
    size = 30
    printHeaderFooter(border, size)

    for _ in range(5):
        print(f"{border}     {border}")

    printHeaderFooter(border, size)



