# ============================================
# Homework Assignment: Movie Database
# ============================================
#
# Objective:
# Practice using dictionaries to store and
# manage information about movies.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# movies = {
#     "The Batman": 8.5,
#     "Inception": 9.2,
#     "Interstellar": 9.0
# }
#
# Keys are movie titles.
# Values are ratings out of 10.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Movies
# 2. Add Movie
# 3. Update Rating
# 4. Delete Movie
# 5. Search Movie
# 6. Highest Rated Movie
# 7. Average Rating
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW MOVIES
# ---------------
# Display all movies and ratings.
#
#
# 2. ADD MOVIE
# -------------
# Ask for:
# - movie title
# - rating
#
# Add the movie to the dictionary.
#
# If the movie already exists:
# - print an error message
#
#
# 3. UPDATE RATING
# -----------------
# Ask for:
# - movie title
# - new rating
#
# Update the movie's rating.
#
#
# 4. DELETE MOVIE
# ----------------
# Remove a movie from the dictionary.
#
#
# 5. SEARCH MOVIE
# ----------------
# Ask for a movie title.
#
# If found:
# - display its rating
#
# If not found:
# - print an error message
#
#
# 6. HIGHEST RATED MOVIE
# -----------------------
# Find and display:
# - movie title
# - rating
#
#
# 7. AVERAGE RATING
# ------------------
# Calculate and display the average rating
# of all movies.
#
#
# 8. EXIT
# --------
# End the program.
#
#
# --------------------------------------------
# PROGRAM REQUIREMENTS
# --------------------------------------------
#
# - Use functions
# - Use a while loop
# - Use a dictionary
# - Validate user input
# - Ratings must be between 0 and 10
#
# --------------------------------------------
# START CODING BELOW
# --------------------------------------------
movies = {}

def view_movies(movies):
    if not movies:
        print("No movies in the database.")
    else:
        for title, rating in movies.items():
            print(f"{title}: {rating}/10")

def add_movie(movies):
    title = input("Enter movie title: ")
    if title in movies:
        print("Movie already exists.")
        return
    try:
        rating = float(input("Enter movie rating (0-10): "))
        if 0 <= rating <= 10:
            movies[title] = rating
            print(f"{title} added with rating {rating}/10.")
        else:
            print("Rating must be between 0 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number for the rating.")

def update_rating(movies): 
    title = input("Enter movie title to update: ")
    if title not in movies:
        print("Movie not found.")
        return
    try:
        rating = float(input("Enter new rating (0-10): "))
        if 0 <= rating <= 10:
            movies[title] = rating
            print(f"{title} updated with new rating {rating}/10.")
        else:
            print("Rating must be between 0 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number for the rating.")

def delete_movie(movies):
    title = input("Enter movie title to delete: ")
    if title in movies:
        del movies[title]
        print(f"{title} has been deleted.")
    else:
        print("Movie not found.")

def search_movie(movies):
    title = input("Enter movie title to search: ")
    if title in movies:
        print(f"{title}: {movies[title]}/10")
    else:
        print("Movie not found.")

def highest_rated_movie(movies):
    if not movies:
        print("No movies in the database.")
        return
    highest_movie = max(movies, key=movies.get)
    print(f"Highest rated movie: {highest_movie} with rating {movies[highest_movie]}/10")

def average_rating(movies):
    if not movies:
        print("No movies in the database.")
        return
    average = sum(movies.values()) / len(movies)
    print(f"Average rating: {average:.2f}/10")
def main(): 
    movies = {}
    while True:
        print("\nMenu:")
        print("1. View Movies")
        print("2. Add Movie")
        print("3. Update Rating")
        print("4. Delete Movie")
        print("5. Search Movie")
        print("6. Highest Rated Movie")
        print("7. Average Rating")
        print("8. Exit")
        
        choice = input("Choose an option (1-8): ")
        
        if choice == '1':
            view_movies(movies)
        elif choice == '2':
            add_movie(movies)
        elif choice == '3':
            update_rating(movies)
        elif choice == '4':
            delete_movie(movies)
        elif choice == '5':
            search_movie(movies)
        elif choice == '6':
            highest_rated_movie(movies)
        elif choice == '7':
            average_rating(movies)
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")
if __name__ == "__main__":
    main()
