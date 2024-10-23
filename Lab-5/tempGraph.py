#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:53:06 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 06 Oct 2024  
# Description:  python program to generate random temperatures for a series of cities, store those temperatures in lists and create a graph using those lists. 


# Additional information - 
Step 1: Installed matplotlib using "pip install matplotlib"
Step 2: import the pyplot 
Step 3: Create a new List named time with range for Months from 1 to 12
Step 4: Choose three city names, Create an empty List for each city, then Append 12 random integer values in the range of 10 through 30
Step 5: Call the plot() passing in time and your city’s List
Step 6: Provide a relevant title to graph & labels to your x and y axis
Step 7: Create a legend
Step 8: Call the show() 

"""


import matplotlib.pyplot as plt
import random

def main():
    # Create a list for the x-axis (time)
    time = list(range(1, 13))  # Months from 1 to 12

    # Choose three city names
    city1 = "Denton"
    city2 = "Allentown"
    city3 = "Raritan"

    # Create lists to store temperatures for each city
    temperatures_city1 = []
    temperatures_city2 = []
    temperatures_city3 = []

    # Append random temperatures (10 to 30) for each city
    for _ in range(12):
        temperatures_city1.append(random.randint(10, 30))
        temperatures_city2.append(random.randint(10, 30))
        temperatures_city3.append(random.randint(10, 30))

    # Plot the data
    plt.plot(time, temperatures_city1, label=city1)
    plt.plot(time, temperatures_city2, label=city2)
    plt.plot(time, temperatures_city3, label=city3)

    # Title and labels
    plt.title("Hourly Temperatures")
    plt.xlabel("Hours")
    plt.ylabel("Temperature (°C)")

    # Create a legend
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()






