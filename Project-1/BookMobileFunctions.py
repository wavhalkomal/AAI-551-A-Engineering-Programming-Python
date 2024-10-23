#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 19:01:21 2024

@author: komalwavhal

# Author: Komal Wavhal
# Date: 17 Oct 2024  
# Description:  python program to to perform data analytics on a data set of books and book reviews.
user can load the files including series of book and the rating of book. Then, your program should perform the required analyses and return the requested
information, such as: listing all books within a literary category; providing detailed information for a specified
book; providing the average ratings for each author; and specifying the most helpful reviewer. 
The user should be able to repeatedly request information until they are satisfied and wish to quit the program.


# Additional information - This program contains the python functions to 
load the book data set of csv file format, 
another function to load the review of books,  
Create reviews_list, book list and the book category list,
provide the options to choose for users, 
Calculate average rating and price if reviews exist, 
display the welcome message, farewell message
and all this defined functions will be called in the another python file named as BookMobile.py

"""

###############################  ( Import Library ) ################################################
import os
####################################################################################################

###################################### ( Start Code ) ###############################################
##### A function to load a file containing a list of books, that has no parameters, returns a
##### Dictionary of Lists containing each of the books from the file and a Set containing all of
##### the literary categories of the books in the file

 
    
def load_books():
    
    """Loads books from a user-specified CSV file."""
    books_dict = {}          ### new Dictionary
    categories_set = set()   ### new set    
    
    while True:       ### while condition untill the condition becomes true, then the code will exit the loop 
        filename = input("Enter the book file name: ")     #### take the input from user 
        if os.path.exists(filename):    ### check the filepath is exist and yes then run the next line 
            with open(filename, 'r') as file:
                header = file.readline()  # Skip header line
                print(header)
                
                
                for line in file:      ### for loop on each file
                    line = line.strip()
                    if line:  # Ensure line is not empty
                    
                    #####    Title,description,authors,publisher,publishedDate,categories
                    
                        parts = line.split(',')    ### split the line by ,
                        title = parts[0].strip()    ### take the 0th element as title
                        author = parts[2].strip()   ### take the 2 element as auther name 
                        description = parts[1].strip()  ### take 1 element as description of the book
                        publisher = parts[3].strip()   ### take the 3 element as publisher name 
                        year = parts[4].strip()       ### take the 4 element as book published year 
                        category = parts[5].strip().lower()   ### take the 5 element as category of the book   
                        
                        books_dict[title] = [author, description, publisher, year, category]     ### take all data into dictionary with the key as title of book and all data as the list of values
                        categories_set.add(category)       ### to make the value unique, add it into categories_set   
                         
            return(books_dict, categories_set)
        else:
            print("File not found. Please try again.")      ### show message when the input filename is not found 



##### A function to load a file containing a list of book reviews, that takes in a Dictionary of book
##### information as a parameter, returns a List containing each of the book reviews from the file

def load_reviews(books_dict): 
    """Loads book reviews from a user-specified CSV file."""
    reviews_list = []

    while True:
        filename = input("Enter the reviews file name: ")
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                header = file.readline()  # Skip header line
                print(header)
                
                for line in file:
                    line = line.strip()
             ####   Id,Title,Price,User_id,profileName,review/helpfulness,review/score
                    
                    print(line )
                    print('===============')
                    if line:
                        parts = line.split(',')
                        review_title = parts[1].strip()
                        rating = float(((parts[6].strip())))
                        helpfulness = str( (parts[5].strip()) )
                        price = float(parts[2].strip())
                        review_score = float(parts[6].strip())

                        print('review_title - ' , review_title )
                        print('rating - ' , rating )
                        print('helpfulness - '   , helpfulness  )
                        print('price - '   , price  )
                        print('review_score - '   , review_score  )
     
                
                        if review_title not in books_dict:
                            raise LookupError(f"Book '{review_title}' not found in books dictionary.")
                        
                        reviews_list.append([review_title, rating, helpfulness,price,review_score])
                        
            return reviews_list
        else:
            print("File not found. Please try again.")



def output_books_by_category(books_dict, categories_set):
    
    """Outputs all books in a specified literary category."""
    print("\nAvailable categories:")
    for idx, category in enumerate(categories_set, start=1):
        print(f"{idx}. {category}")
    
    selected_category = input("Select a category: ").strip().lower()
    while selected_category not in categories_set:
        selected_category = input("Invalid category. Select a category: ").strip().lower()
    
    print(f"\nBooks in category '{selected_category}':")
    for title, info in books_dict.items():
        if info[4] == selected_category:
            print(f"Title: {title}, Author: {info[0]}")
            
            

def output_book_details(books_dict, reviews_list):
    """Outputs detailed information for a specified book."""
    print("\nAvailable books:")
    for idx, title in enumerate(books_dict.keys(), start=1):
        print(f"{idx}. {title}")
    
    selected_title = input("Select a book title: ").strip()
    while selected_title not in books_dict:
        selected_title = input("Invalid title. Select a book title: ").strip()
    
    book_info = books_dict[selected_title]
    relevant_reviews = [r for r in reviews_list if r[0] == selected_title]
    
    
    print('relevant_reviews ----->>> ',relevant_reviews)
    
    
    
    # Calculate average rating and price if reviews exist

    if relevant_reviews:
        # Calculate average rating, handling non-numeric values
        valid_ratings = []
        for r in relevant_reviews:
            try:
                valid_ratings.append(float(r[1]))  # Attempt to convert rating to float
            except ValueError:
                print(f"Invalid rating '{r[1]}' for review of '{selected_title}' ignored.")

        avg_rating = sum(valid_ratings) / len(valid_ratings) if valid_ratings else 0
        print(f"\nDetails for '{selected_title}':")
        print(f"Author: {book_info[0]}")
        print(f"Description: {book_info[1]}")
        print(f"Publisher: {book_info[2]}, Year: {book_info[3]}")
        print(f"Category: {book_info[4]}")
        print(f"Average Rating: {avg_rating:.1f}")
    else:
        print(f"No reviews available for '{selected_title}'.") 
        

def output_average_author_ratings(books_dict, reviews_list):
    """Calculates and outputs the average ratings for each author."""
    author_ratings = {}
    author_books = {}
    
    # Aggregate ratings by author
    for title, info in books_dict.items():
        authors = info[0].split(';')  # Handle multiple authors
        author_books.setdefault(tuple(authors), []).append(title)
    
    for review in reviews_list:
        review_title, rating = review[0], review[1]
        if review_title in books_dict:
            authors = books_dict[review_title][0].split(';')
            for author in authors:
                author_ratings.setdefault(author.strip(), []).append(rating)
    
    # Calculate average ratings
    for author, ratings in author_ratings.items():
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        print(f"{author}: Average Rating = {avg_rating:.1f}" if ratings else f"{author}: No ratings available.")

def output_most_helpful_reviewer(reviews_list):
    """Calculates and outputs the most helpful reviewer.
       Outputs the name and average helpfulness rating of the most helpful reviewer."""
       
    reviewer_helpfulness = {}

    print('reviews_list------>>>', reviews_list)
    for review in reviews_list:
        
        print('review------>>>', review)  
        
        
        #####  reviews_list ([review_title, rating, helpfulness,price,review_score])
                        
        reviewer = review[0]  # Assuming the reviewe is at index 2
        helpful_count = float(review[1])  # Assuming helpful votes are at index 1
        total_votes = float(review[4])  # Assuming total votes are at index 4

        if reviewer not in reviewer_helpfulness:
            reviewer_helpfulness[reviewer] = [0, 0]  # [sum of helpfulness, count of total reviews]

        reviewer_helpfulness[reviewer][0] += helpful_count
        reviewer_helpfulness[reviewer][1] += total_votes

    # Calculate average helpfulness
    most_helpful = None
    max_average = 0

    for reviewer, (helpful, total) in reviewer_helpfulness.items():
        if total >= 10:  # Only consider reviewers with at least 10 votes
            average_helpfulness = (helpful / total) * 100 if total > 0 else 0
            if average_helpfulness > max_average:
                max_average = average_helpfulness
                most_helpful = reviewer

    if most_helpful:
        print(f"Most helpful reviewer: {most_helpful} with an average helpfulness of {int(max_average)}%")
    else:
        print("No reviewers with sufficient data to determine the most helpful reviewer.")


def welcome_message():
    """Displays a welcome message."""
    print("Welcome to the Book Mobile!")

def farewell_message():
    """Displays a farewell message."""
    print("Thank you for using the Book Mobile!")

def menu():
    """Displays a menu and returns the user's choice."""
    print("\nMenu:")
    print("1. Load book file")
    print("2. Load book review file")
    print("3. Output books by literary category")
    print("4. Output a book's details")
    print("5. Output average author ratings")
    print("6. Output most helpful reviewer")
    print("7. Quit")
    
    choice = input("Select an option (1-7): ")
    return choice

 







