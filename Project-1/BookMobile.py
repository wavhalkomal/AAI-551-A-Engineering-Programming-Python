#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:32:05 2024

@author: komalwavhal 

# Author: Komal Wavhal
# Date: 17 Oct 2024  
# Description:  python program to to perform data analytics on a data set of books and book reviews.
user can load the files including series of book and the rating of book. Then, your program should perform the required analyses and return the requested
information, such as: listing all books within a literary category; providing detailed information for a specified
book; providing the average ratings for each author; and specifying the most helpful reviewer. 
The user should be able to repeatedly request information until they are satisfied and wish to quit the program.


# Additional information - this is the main program through wich all the functions will get called from the another python file named as BookMobileFunction.py
in the same location. first step is to import the python module, then 
the main function call,
main function first initilie all the variables locally inside function, 
declare the dictionaries, lists and set.
by calling welcome_message program display the welcome message.
using the while condition get the users choice   
load the book dataset by calling the load_book function, then load review by calling the 
load_reviews function. 
perform the data processing, calculate the average rating, categories unique values and save all book details in dictionary. 


"""
 

from BookMobileFunctions import *

def main():
    

    book_file_loaded = False
    review_file_loaded = False
    books_dict = {}
    categories_set = set()
    reviews_list = []

    welcome_message()

    while True:
        choice = menu()

        match choice:
            case "1":
                books_dict, categories_set = load_books()
                book_file_loaded = True
            case "2":
                if not book_file_loaded:
                    print("Please load the book file first.")
                else:
                    try:
                        reviews_list = load_reviews(books_dict)
                        review_file_loaded = True
                    except LookupError as e:
                        print(e)
            case "3":
                if not review_file_loaded:
                    print("Please load the book reviews file first.")
                else:
                    output_books_by_category(books_dict, categories_set)
            case "4":
                if not review_file_loaded:
                    print("Please load the book reviews file first.")
                else:
                    output_book_details(books_dict, reviews_list)
            case "5":
                if not review_file_loaded:
                    print("Please load the book reviews file first.")
                else:
                    output_average_author_ratings(books_dict, reviews_list)
            case "6":
                if not review_file_loaded:
                    print("Please load the book reviews file first.")
                else:
                    output_most_helpful_reviewer(reviews_list)
            case "7":
                farewell_message()
                return
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


    
    
 
