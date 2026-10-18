# ============================================
# Homework Assignment: Word Analyzer
# ============================================
#
# Objective:
# Practice using dictionaries, lists, loops,
# strings, and calculations to analyze text.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# words = [
#     "apple",
#     "banana",
#     "apple",
#     "orange",
#     "banana",
#     "apple"
# ]
#
# Use a dictionary to keep track of how many
# times each word appears.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Words
# 2. Add Word
# 3. Remove Word
# 4. Count Words
# 5. Most Common Word
# 6. Least Common Word
# 7. Search Words
# 8. Longest Word
# 9. Shortest Word
# 10. Word Statistics
# 11. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW WORDS
# -------------
# Display every word currently in the list.
#
#
# 2. ADD WORD
# -----------
# Ask the user for a word.
#
# Add the word to the list.
#
# Requirements:
# - Word cannot be empty.
# - Convert the word to lowercase.
#
#
# 3. REMOVE WORD
# --------------
# Ask the user for a word.
#
# Remove one occurrence of that word.
#
# Requirements:
# - Display an error if the word does not exist.
#
#
# 4. COUNT WORDS
# --------------
# Create a dictionary showing how many
# times each word appears.
#
# Do not use collections.Counter.
#
#
# 5. MOST COMMON WORD
# -------------------
# Find the word that appears the most.
#
# Display the word and its count.
#
#
# 6. LEAST COMMON WORD
# --------------------
# Find the word that appears the fewest
# times.
#
# Display the word and its count.
#
#
# 7. SEARCH WORDS
# ---------------
# Ask the user for a search term.
#
# Display every word containing that
# search term.
#
#
# 8. LONGEST WORD
# ---------------
# Find and display the longest word.
#
# Display the word and its length.
#
#
# 9. SHORTEST WORD
# ----------------
# Find and display the shortest word.
#
# Display the word and its length.
#
#
# 10. WORD STATISTICS
# -------------------
# Display:
#
# - Total number of words
# - Number of unique words
# - Longest word
# - Shortest word
# - Most common word
# - Average word length
#
#
# 11. EXIT
# --------
# End the program.
#
# --------------------------------------------
# PROGRAM REQUIREMENTS
# --------------------------------------------
#
# - Use functions for each menu option.
# - Use a while loop for the menu.
# - Use a list to store the words.
# - Use a dictionary to count the words.
# - Use loops.
# - Use string methods.
# - Validate user input.
# - Do not use collections.Counter.
# - Do not use external libraries.
#
# --------------------------------------------
# SAVE / LOAD
# --------------------------------------------
#
# Save the words to:
#
# "words.json"
#
# When the program starts:
#
# - Try to load words.json.
# - If the file does not exist, start with
#   an empty list.
#
# Save the data whenever the word list changes.
#
# ============================================


import json
import os



# --------------------------------------------
# LOAD DATA
# --------------------------------------------

def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Coding Aubrey/Homework/Word Analyzer
    try:
        file_path = os.path.join(BASE_DIR, "words.json")
        with open(file_path, "r") as file:
            words = json.load(file)
            return words
    except FileNotFoundError:
        words = []
        return words


# --------------------------------------------
# SAVE DATA
# --------------------------------------------

def save_data(words):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "words.json")
    with open(file_path, "w") as file:
        json.dump(words, file)


# --------------------------------------------
# VIEW WORDS
# --------------------------------------------

def view_words():
    words = load_data()
    for word in words:
        print(word)


# --------------------------------------------
# ADD WORD
# --------------------------------------------

def add_word():
    word = input("Enter a word to add: ").strip().lower()
    if not word:
        print("Error: Word cannot be empty.")
        return

    words = load_data()
    words.append(word)
    save_data(words)
    print(f"Added word: {word}")


# --------------------------------------------
# REMOVE WORD
# --------------------------------------------

def remove_word():
    word = input("Enter a word to remove: ").strip().lower()
    words = load_data()

    if word in words:
        words.remove(word)
        save_data(words)
        print(f"Removed word: {word}")
    else:
        print(f"Error: Word '{word}' does not exist.")


# --------------------------------------------
# COUNT WORDS
# --------------------------------------------

def count_words():
    words = load_data()
    print(f"Total number of words: {len(words)}")


# --------------------------------------------
# MOST COMMON WORD
# --------------------------------------------

def most_common_word():
    words = load_data()
    if not words:
        print("No words available.")
        return
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    most_common = max(word_counts, key=word_counts.get)
    print(f"Most common word: {most_common} (appears {word_counts[most_common]} times)")

# --------------------------------------------
# LEAST COMMON WORD
# --------------------------------------------

def least_common_word():
    words = load_data()
    if not words:
        print("No words available.")
        return
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    least_common = min(word_counts, key=word_counts.get)
    print(f"Least common word: {least_common} (appears {word_counts[least_common]} times)") 


# --------------------------------------------
# SEARCH WORDS
# --------------------------------------------

def search_words():
    words = load_data()
    if not words:
        print("No words available.")
        return
    search_term = input("Enter a word to search for: ").strip().lower()
    found_words = [word for word in words if search_term in word]
    # found_words = []
    # for word in words:
    #     if search_term in word:
    #         found_words.append(word)
    # going through each word and if the search is in it then they put it. in found words
    if found_words:
        print(f"Words containing '{search_term}':") 
        for word in found_words: 
            print(word) 
    else: 
        print(f"No words containing '{search_term}' found.") 


# --------------------------------------------
# LONGEST WORD
# --------------------------------------------

def longest_word(): 
    words = load_data() 
    if not words: 
        print("No words available.") 
        return 
    longest = max(words, key=len)
    print(f"Longest word: {longest} (length {len(longest)})")


# --------------------------------------------
# SHORTEST WORD
# --------------------------------------------

def shortest_word():
    words = load_data()
    if not words:
        print("No words available.")
        return
    shortest = min(words, key=len)
    print(f"Shortest word: {shortest} (length {len(shortest)})")


# --------------------------------------------
# WORD STATISTICS
# --------------------------------------------

def word_statistics():
    words = load_data()
    if not words:
        print("No words available.")
        return
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    total_words = len(words)
    unique_words = len(word_counts)
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")


# --------------------------------------------
# MAIN MENU
# --------------------------------------------

while True:

    print("\n===== WORD ANALYZER =====")
    print("1. View Words")
    print("2. Add Word")
    print("3. Remove Word")
    print("4. Count Words")
    print("5. Most Common Word")
    print("6. Least Common Word")
    print("7. Search Words")
    print("8. Longest Word")
    print("9. Shortest Word")
    print("10. Word Statistics")
    print("11. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_words()

    elif choice == "2":
        add_word()

    elif choice == "3":
        remove_word()

    elif choice == "4":
        count_words()

    elif choice == "5":
        most_common_word()

    elif choice == "6":
        least_common_word()

    elif choice == "7":
        search_words()

    elif choice == "8":
        longest_word()

    elif choice == "9":
        shortest_word()

    elif choice == "10":
        word_statistics()

    elif choice == "11":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-11.")