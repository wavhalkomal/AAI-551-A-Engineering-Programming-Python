#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 18:53:06 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 06 Oct 2024  
# Description:  python program to manage the small laboratory’s equipment inventory.  


# Additional information - program to enter the maximum 5 items in the lab equipment inventory 
give option to user to select add the equipments, remove it if required, display all equipments and 
if user enters the invalid number then display a message to choose correct option. 

"""
 


def main():
    # Initialize the equipment list
    equipment = []
    print('Welcome to the inventory manager for your laboratory!')
    
    while True:
        # Display the menu
        print("\nYou can choose from the following options in")
        print("\nLaboratory Equipment Manager") 
        print("1. Add Equipment")
        print("2. Remove Equipment")
        print("3. Display Current Equipment")
        print("4. Leave the Laboratory Manager")
        
        # Get user choice
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            # Add Equipment
            if len(equipment) >= 5:
                print("Cannot add equipment. The maximum capacity is 5 items so your laboratory cannot support any more equipment!")
            else:
                new_equipment = input("Enter the name of the equipment to add: ")
                equipment.append(new_equipment)
                print(f"{new_equipment} has been added to the laboratory.")
        
        elif choice == '2':
            # Remove Equipment
            equipment_to_remove = input("What would you like to remove from the laboratory: ")
            if equipment_to_remove in equipment:
                equipment.remove(equipment_to_remove)
                print(f"{equipment_to_remove} has been removed from the laboratory.")
            else:
                print(f"{equipment_to_remove} was not present and could not be removed")
        
        elif choice == '3':
            # Display Current Equipment
            if equipment:
                print("Current Equipment in the Laboratory:")
                for item in equipment:
                    print(f"- {item}")
            else:
                print("No equipment currently in the laboratory.")
        
        elif choice == '4':
            # Leave the Laboratory Manager
            print("Thank you for using the Laboratory Equipment Manager. Good luck on your journey of discovery!")
            break
        
        else:
            # Invalid choice
            print(f"{choice} was not a valid option. Please try again")

if __name__ == "__main__":
    main()



#######################( Result) ######################
# Welcome to the inventory manager for your laboratory!

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 1
# Enter the name of the equipment to add: Telescope
# Telescope has been added to the laboratory.

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 1
# Enter the name of the equipment to add: Electron Microscope
# Electron Microscope has been added to the laboratory.

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 1
# Enter the name of the equipment to add: Electromagnets
# Electromagnets has been added to the laboratory.

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 1
# Enter the name of the equipment to add: Liquid Helium
# Liquid Helium has been added to the laboratory.

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 1
# Enter the name of the equipment to add: Lenses
# Lenses has been added to the laboratory.

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 1
# Cannot add equipment. The maximum capacity is 5 items so your laboratory cannot support any more equipment!

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 2
# What would you like to remove from the laboratory: Telescope
# Telescope has been removed from the laboratory.

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 3
# Current Equipment in the Laboratory:
# - Electron Microscope
# - Electromagnets
# - Liquid Helium
# - Lenses

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 5
# 5 was not a valid option. Please try again

# You can choose from the following options in

# Laboratory Equipment Manager
# 1. Add Equipment
# 2. Remove Equipment
# 3. Display Current Equipment
# 4. Leave the Laboratory Manager
# Choose an option (1-4): 4
# Thank you for using the Laboratory Equipment Manager. Good luck on your journey of discovery!

########################################################