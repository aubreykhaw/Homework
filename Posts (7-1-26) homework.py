# ============================================
# Homework Assignment: Social Media Simulator
# ============================================
#
# Objective:
# Practice using lists and dictionaries to
# create a simple social media system.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# posts = [
#     {
#         "username": "alice",
#         "post": "Hello everyone!",
#         "likes": 3
#     },
#     {
#         "username": "bob",
#         "post": "Having a great day!",
#         "likes": 5
#     }
# ]
#
# Each post is stored as a dictionary inside
# a list.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Posts
# 2. Create Post
# 3. Like Post
# 4. Delete Post
# 5. View User Posts
# 6. Most Liked Post
# 7. Total Likes
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW POSTS
# --------------
# Display all posts.
#
# Example:
# Post ID: 0
# User: alice
# Post: Hello everyone!
# Likes: 3
#
#
# 2. CREATE POST
# ---------------
# Ask for:
# - username
# - post content
#
# Create a new post and add it to the list.
#
#
# 3. LIKE POST
# -------------
# Ask for:
# - post ID
#
# Increase the likes for that post by 1.
#
# Requirements:
# - post ID must be valid
#
#
# 4. DELETE POST
# ---------------
# Ask for:
# - post ID
#
# Remove the post from the list.
#
# Requirements:
# - post ID must be valid
#
#
# 5. VIEW USER POSTS
# -------------------
# Ask for:
# - username
#
# Display all posts made by that user.
#
#
# 6. MOST LIKED POST
# -------------------
# Find and display:
# - username
# - post content
# - likes
#
# for the post with the most likes.
#
#
# 7. TOTAL LIKES
# ---------------
# Calculate and display the total number
# of likes across all posts.
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
# - Use a list of dictionaries
# - Validate user input
# - Handle invalid post IDs
#
posts = []


def view_posts():
    if len(posts) == 0:
        print("No posts available.")
    else:
        for index, post in enumerate(posts):
            print("\nPost ID:", index)
            print("User:", post["username"])
            print("Post:", post["post"])
            print("Likes:", post["likes"])


def create_post():
    username = input("Enter username: ")
    content = input("Enter post: ")

    new_post = {
        "username": username,
        "post": content,
        "likes": 0
    }

    posts.append(new_post)
    print("Post created!")


def like_post():
    if len(posts) == 0:
        print("No posts available.")
        return

    post_id = int(input("Enter post ID: "))

    if 0 <= post_id < len(posts):
        posts[post_id]["likes"] += 1
        print("Post liked!")
    else:
        print("Invalid post ID.")


def delete_post():
    if len(posts) == 0:
        print("No posts available.")
        return

    post_id = int(input("Enter post ID: "))

    if 0 <= post_id < len(posts):
        posts.pop(post_id)
        print("Post deleted!")
    else:
        print("Invalid post ID.")


def view_user_posts():
    username = input("Enter username: ")
    found = False

    for index, post in enumerate(posts):
        if post["username"] == username:
            print("\nPost ID:", index)
            print("Post:", post["post"])
            print("Likes:", post["likes"])
            found = True

    if not found:
        print("No posts found for that user.")


def most_liked_post():
    if len(posts) == 0:
        print("No posts available.")
        return

    most_liked = posts[0]

    for post in posts:
        if post["likes"] > most_liked["likes"]:
            most_liked = post

    print("\nMost Liked Post")
    print("User:", most_liked["username"])
    print("Post:", most_liked["post"])
    print("Likes:", most_liked["likes"])


def total_likes():
    total = 0

    for post in posts:
        total += post["likes"]

    print("Total Likes:", total)



while True:
    print("\n===== Social Media Simulator =====")
    print("1. View Posts")
    print("2. Create Post")
    print("3. Like Post")
    print("4. Delete Post")
    print("5. View User Posts")
    print("6. Most Liked Post")
    print("7. Total Likes")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        view_posts()

    elif choice == "2":
        create_post()

    elif choice == "3":
        like_post()

    elif choice == "4":
        delete_post()

    elif choice == "5":
        view_user_posts()

    elif choice == "6":
        most_liked_post()

    elif choice == "7":
        total_likes()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")