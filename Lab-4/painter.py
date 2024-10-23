#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 10:34:16 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 29 Sept 2024  
# Description:  python program to prompts user for art choice and border symbol.
 

"""


def intro():
    """Introduces the program and prompts user for art choice and border symbol."""
    print("Welcome to the ASCII Art Painter!")
    print("Choose from the following options:")
    print("1. Sleeping Cat")
    print("2. Sailing Ship")
    print("3. Teddy bears")
    print("4. Guitar")

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

def main():
    """Coordinates the overall execution of the ASCII art painter."""
    choice, border = intro()

    if choice == 1:
        sleepingCat(border)
    elif choice == 2:
        sailingShip(border)
    elif choice == 3:
        teddy_bears(border)
    elif choice == 4:
        guitar(border)
    else:
        blank(border)
        print("That option is not available.")
        exit(-1)

    print("I hope you enjoyed your art!")

if __name__ == "__main__":
    main()




"""
----------------Sample Output------------------
Welcome to the ASCII Art Painter!
Choose from the following options:
1. Sleeping Cat
2. Sailing Ship
3. Teddy bears
4. Guitar
Enter the number of your choice (1-4): 1
Enter a single symbol for the border: #
##############################
#          |\ _,,,---,,_           #
#  ZZZzz /,`.-'`' -. ;-;;,_        #
#       |,4- ) )- ,_. ,\ ( `'-'    #
#       '---''(_/--' `-'\_)        #
##############################
I hope you enjoyed your art!

%runfile '/Users/komalwavhal/Desktop/AAI-551/Lab 4/painter.py' --wdir
Welcome to the ASCII Art Painter!
Choose from the following options:
1. Sleeping Cat
2. Sailing Ship
3. Teddy bears
4. Guitar
Enter the number of your choice (1-4): 2
Enter a single symbol for the border: @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@     |    |    |                   @
@    )_)  )_)  )_)                  @
@   )___))___))___)\                @
@  )____)____)_____)\\              @
@  _____|____|____|____\\\__        @
@  \    Satisfaction   /              @
@ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^         @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
I hope you enjoyed your art!

%runfile '/Users/komalwavhal/Desktop/AAI-551/Lab 4/painter.py' --wdir
Welcome to the ASCII Art Painter!
Choose from the following options:
1. Sleeping Cat
2. Sailing Ship
3. Teddy bears
4. Guitar
Enter the number of your choice (1-4): 3
Enter a single symbol for the border: #
##############################
# {~._.~} #
#  ( Y )  #
# ()~*~() #
# (_)-(_) #
##############################
I hope you enjoyed your art!

%runfile '/Users/komalwavhal/Desktop/AAI-551/Lab 4/painter.py' --wdir
Welcome to the ASCII Art Painter!
Choose from the following options:
1. Sleeping Cat
2. Sailing Ship
3. Teddy bears
4. Guitar
Enter the number of your choice (1-4): 4
Enter a single symbol for the border: *
******************************
*                _______       __                                               *
*              /   ------.   / ._`_                                             *
*             |  /         ~--~    \                                            *
*             | |             __    `.____________________ _^-----^             *
*             | |  I=|=======/--\=========================| o o o |             *
*             \ |  I=|=======\__/=========================|_o_o_o_|             *
*              \|                   /                       ~    ~              *
*                \       .---.    .                                             *
*                  -----'     ~~''                                              *
******************************
I hope you enjoyed your art!

"""