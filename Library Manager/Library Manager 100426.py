# ============================================
# Homework Assignment: Personal Library Manager
# ============================================
#
# Objective:
# Practice using lists, dictionaries, loops,
# functions, searching, sorting, and JSON files
# to manage a personal library.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Each book should be represented by a dictionary.
#
# Example:
#
# books = [
#     {
#         "title": "Harry Potter",
#         "author": "J.K. Rowling",
#         "year": 1997,
#         "genre": "Fantasy",
#         "rating": 5,
#         "read": True
#     },
#     {
#         "title": "The Hobbit",
#         "author": "J.R.R. Tolkien",
#         "year": 1937,
#         "genre": "Fantasy",
#         "rating": 4,
#         "read": False
#     }
# ]
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View All Books
# 2. Add Book
# 3. Remove Book
# 4. Search Books
# 5. Mark Book as Read
# 6. Rate Book
# 7. View Read Books
# 8. View Unread Books
# 9. Highest Rated Book
# 10. Books by Genre
# 11. Sort Books
# 12. Library Statistics
# 13. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW ALL BOOKS
# -----------------
# Display every book in the library.
#
# Display:
# - Title
# - Author
# - Year
# - Genre
# - Rating
# - Read status
#
#
# 2. ADD BOOK
# -----------
# Ask the user for:
#
# - title
# - author
# - year
# - genre
#
# New books should start with:
#
# rating = 0
# read = False
#
# Requirements:
# - Title cannot be empty.
# - Author cannot be empty.
# - Year must be a valid number.
# - A book with the same title cannot already exist.
#
#
# 3. REMOVE BOOK
# --------------
# Ask for a book title.
#
# Remove that book from the library.
#
# Requirements:
# - Display an error if the book does not exist.
#
#
# 4. SEARCH BOOKS
# ---------------
# Ask the user for a search term.
#
# Search both the title and author.
#
# Display every book where the search term
# appears in either the title or author.
#
#
# 5. MARK BOOK AS READ
# --------------------
# Ask for a book title.
#
# Change the book's read status to True.
#
# Requirements:
# - Book must exist.
#
#
# 6. RATE BOOK
# ------------
# Ask for:
# - book title
# - rating
#
# Rating must be between 1 and 5.
#
# Update the book's rating.
#
#
# 7. VIEW READ BOOKS
# ------------------
# Display only books that have been read.
#
#
# 8. VIEW UNREAD BOOKS
# --------------------
# Display only books that have not been read.
#
#
# 9. HIGHEST RATED BOOK
# ---------------------
# Find the book with the highest rating.
#
# Display:
# - Title
# - Author
# - Rating
#
# If multiple books have the same rating,
# display all books with that rating.
#
#
# 10. BOOKS BY GENRE
# ------------------
# Ask for a genre.
#
# Display every book belonging to that genre.
#
# The search should not be case-sensitive.
#
#
# 11. SORT BOOKS
# --------------
# Give the user another menu:
#
# 1. Sort by Title
# 2. Sort by Year
# 3. Sort by Rating
#
# Display the books in the selected order.
#
# For rating:
# - Highest rating should appear first.
#
# For year:
# - Newest book should appear first.
#
# --------------------------------------------
# 12. LIBRARY STATISTICS
# ----------------------
# Display:
#
# - Total number of books
# - Number of read books
# - Number of unread books
# - Average rating
# - Oldest book
# - Newest book
#
# --------------------------------------------
# 13. EXIT
# --------
# End the program.
#
# --------------------------------------------
# PROGRAM REQUIREMENTS
# --------------------------------------------
#
# - Use functions for each menu option.
# - Use a while loop for the menu.
# - Use a list of dictionaries.
# - Use loops.
# - Use conditionals.
# - Validate user input.
# - Use dictionary access.
# - Use sorted().
# - Use max() or another appropriate method.
# - Use string methods.
#
# --------------------------------------------
# SAVE / LOAD
# --------------------------------------------
#
# Save the library to:
#
# "books.json"
#
# When the program starts:
#
# - Try to load books.json.
# - If the file does not exist, start with
#   an empty list.
#
# Save the data whenever the library changes.
#
# Changes include:
#
# - Adding a book
# - Removing a book
# - Marking a book as read
# - Rating a book
#
# ============================================



import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "books.json")


# --------------------------------------------
# LOAD DATA
# --------------------------------------------
def load_data():
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            books = json.load(file)
            if isinstance(books, list):
                return books
            print("Invalid data format. Starting with an empty library.")
            return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("The JSON file is invalid. Starting with an empty library.")
        return []


# --------------------------------------------
# SAVE DATA
# --------------------------------------------
def save_data(books):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)


# --------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------
def find_book(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None


def display_book(book):
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    print(f"Genre: {book['genre']}")
    print(f"Rating: {book['rating']}/5")
    print(f"Read: {'Yes' if book['read'] else 'No'}")
    print("-" * 35)


def display_books(books):
    if not books:
        print("No books found.")
        return

    for book in books:
        display_book(book)


def get_integer(prompt, minimum=None, maximum=None):
    while True:
        try:
            number = int(input(prompt).strip())

            if minimum is not None and number < minimum:
                print(f"Please enter a number of at least {minimum}.")
                continue

            if maximum is not None and number > maximum:
                print(f"Please enter a number no greater than {maximum}.")
                continue

            return number
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# --------------------------------------------
# 1. VIEW ALL BOOKS
# --------------------------------------------
def view_books():
    books = load_data()
    display_books(books)


# --------------------------------------------
# 2. ADD BOOK
# --------------------------------------------
def add_book():
    books = load_data()

    title = input("Enter the book title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    if find_book(books, title):
        print("A book with this title already exists.")
        return

    author = input("Enter the book author: ").strip()
    if not author:
        print("Author cannot be empty.")
        return

    year = get_integer("Enter the publication year: ", 1)
    genre = input("Enter the book genre: ").strip()

    if not genre:
        print("Genre cannot be empty.")
        return

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "rating": 0,
        "read": False
    }

    books.append(book)
    save_data(books)
    print(f"Added book: {title}")


# --------------------------------------------
# 3. REMOVE BOOK
# --------------------------------------------
def remove_book():
    books = load_data()
    title = input("Enter the book title to remove: ").strip()

    book = find_book(books, title)

    if book is None:
        print(f"Book '{title}' not found.")
        return

    books.remove(book)
    save_data(books)
    print(f"Removed book: {title}")


# --------------------------------------------
# 4. SEARCH BOOKS
# --------------------------------------------
def search_books():
    books = load_data()
    search_term = input("Enter a title or author to search: ").strip().lower()

    if not search_term:
        print("Search term cannot be empty.")
        return

    found_books = [
        book for book in books
        if search_term in book["title"].lower()
        or search_term in book["author"].lower()
    ]

    if found_books:
        print(f"\nFound {len(found_books)} matching book(s):")
        display_books(found_books)
    else:
        print("No matching books found.")


# --------------------------------------------
# 5. MARK BOOK AS READ
# --------------------------------------------
def mark_as_read():
    books = load_data()
    title = input("Enter the book title to mark as read: ").strip()

    book = find_book(books, title)

    if book is None:
        print(f"Book '{title}' not found.")
        return

    if book["read"]:
        print("This book is already marked as read.")
        return

    book["read"] = True
    save_data(books)
    print(f"Marked '{title}' as read.")


# --------------------------------------------
# 6. RATE BOOK
# --------------------------------------------
def rate_book():
    books = load_data()
    title = input("Enter the book title to rate: ").strip()

    book = find_book(books, title)

    if book is None:
        print(f"Book '{title}' not found.")
        return

    rating = get_integer("Enter a rating (1-5): ", 1, 5)

    book["rating"] = rating
    save_data(books)
    print(f"Updated rating for '{title}' to {rating}/5.")


# --------------------------------------------
# VIEW READ BOOKS
# --------------------------------------------

def view_read_books():
    # TODO
    pass


# --------------------------------------------
# VIEW UNREAD BOOKS
# --------------------------------------------

def view_unread_books():
    # TODO
    pass


# --------------------------------------------
# HIGHEST RATED BOOK
# --------------------------------------------

def highest_rated_book():
    # TODO
    pass


# --------------------------------------------
# BOOKS BY GENRE
# --------------------------------------------

def books_by_genre():
    # TODO
    pass


# --------------------------------------------
# SORT BOOKS
# --------------------------------------------

def sort_books():
    # TODO
    pass


# --------------------------------------------
# LIBRARY STATISTICS
# --------------------------------------------

def library_statistics():
    # TODO
    pass


# --------------------------------------------
# MAIN MENU
# --------------------------------------------

while True:

    print("\n===== PERSONAL LIBRARY =====")
    print("1. View All Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Books")
    print("5. Mark Book as Read")
    print("6. Rate Book")
    # print("7. View Read Books")
    # print("8. View Unread Books")
    # print("9. Highest Rated Book")
    # print("10. Books by Genre")
    # print("11. Sort Books")
    # print("12. Library Statistics")
    print("13. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_books()

    elif choice == "2":
        add_book()

    elif choice == "3":
        remove_book()

    elif choice == "4":
        search_books()

    elif choice == "5":
        mark_as_read()

    elif choice == "6":
        rate_book()

    # elif choice == "7":
    #     view_read_books()

    # elif choice == "8":
    #     view_unread_books()

    # elif choice == "9":
    #     highest_rated_book()

    # elif choice == "10":
    #     books_by_genre()

    # elif choice == "11":
    #     sort_books()

    # elif choice == "12":
    #     library_statistics()

    elif choice == "13":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-13.")