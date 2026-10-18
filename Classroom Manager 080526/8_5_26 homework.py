# ============================================
# Homework Assignment: Classroom Manager
# ============================================
#
# Objective:
# Practice using dictionaries and lists to
# manage students enrolled in different
# classrooms.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# classrooms = {
#     "Math": ["Alice", "Bob"],
#     "Science": ["Charlie"],
#     "History": []
# }
#
# Keys are classroom names.
# Values are lists of students.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View Classrooms
# 2. Add Classroom
# 3. Add Student
# 4. Move Student
# 5. Remove Student
# 6. Delete Classroom
# 7. Largest Classroom
# 8. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW CLASSROOMS
# -------------------
# Display every classroom and the students
# enrolled in it.
#
#
# 2. ADD CLASSROOM
# -----------------
# Ask for a classroom name.
#
# Create an empty classroom.
#
# If the classroom already exists:
# - print an error message
#
#
# 3. ADD STUDENT
# ---------------
# Ask for:
# - classroom name
# - student name
#
# Add the student to the classroom.
#
# Requirements:
# - classroom must exist
# - student cannot already be in that classroom
#
#
# 4. MOVE STUDENT
# ----------------
# Ask for:
# - student name
# - current classroom
# - new classroom
#
# Move the student from one classroom
# to another.
#
# Requirements:
# - both classrooms must exist
# - student must be in the current classroom
#
#
# 5. REMOVE STUDENT
# ------------------
# Ask for:
# - classroom name
# - student name
#
# Remove the student from the classroom.
#
#
# 6. DELETE CLASSROOM
# --------------------
# Ask for a classroom name.
#
# Delete the classroom.
#
# Requirements:
# - classroom must exist
# - classroom must be empty
#
#
# 7. LARGEST CLASSROOM
# ---------------------
# Find and display:
# - classroom name
# - number of students
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
# - Use functions for each menu option.
# - Use a while loop for the menu.
# - Use a dictionary with lists as values.
# - Validate user input.
#
# --------------------------------------------
# SAVE/LOAD CLASSROOM DATA
# --------------------------------------------
#
# When the program starts:
# - Try to load the classroom data from
#   "classrooms.json".
# - If the file does not exist, start with
#   an empty dictionary.
#
# Every time the user changes the data
# (adding/removing classrooms, adding/removing
# students, or moving students), save the
# updated dictionary back to the file.
#
# Hint:
# - import json
# - Use json.load() to load the data.
# - Use json.dump() to save the data.
#
# Example classrooms.json:
#
# {
#     "Math": [
#         "Alice",
#         "Bob"
#     ],
#     "Science": [
#         "Charlie"
#     ],
#     "History": []
# }
#
# ============================================ 
import json
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    file_path = os.path.join(BASE_DIR, "classrooms.json")
    with open(file_path, "r") as file:
        classrooms = json.load(file)
except FileNotFoundError:
    classrooms = {}


def save_data():
    file_path = os.path.join(BASE_DIR, "classrooms.json")
    
    with open(file_path, "w") as file:
        json.dump(classrooms, file, indent=4)
    
    


def view_classrooms():
    if not classrooms:
        print("No classrooms found.")
        return

    for classroom, students in classrooms.items():
        print(classroom + ":")
        
        if students:
            for student in students:
                print("  - " + student)
        else:
            print("  No students")



def add_classroom():
    classroom = input("Enter classroom name: ").strip()

    if not classroom:
        print("Classroom name cannot be empty.")
        return

    if classroom in classrooms:
        print("Error: Classroom already exists.")
        return

    classrooms[classroom] = []
    save_data()

    print("Classroom added successfully.")



def add_student():
    classroom = input("Enter classroom name: ").strip()
    student = input("Enter student name: ").strip()

    if classroom not in classrooms:
        print("Error: Classroom does not exist.")
        return

    if not student:
        print("Student name cannot be empty.")
        return

    if student in classrooms[classroom]:
        print("Error: Student is already in this classroom.")
        return

    classrooms[classroom].append(student)
    save_data()

    print("Student added successfully.")


def move_student():
    student = input("Enter student name: ").strip()
    current_classroom = input("Enter current classroom: ").strip()
    new_classroom = input("Enter new classroom: ").strip()

    if current_classroom not in classrooms:
        print("Error: Current classroom does not exist.")
        return

    if new_classroom not in classrooms:
        print("Error: New classroom does not exist.")
        return

    if student not in classrooms[current_classroom]:
        print("Error: Student is not in the current classroom.")
        return

    if student in classrooms[new_classroom]:
        print("Error: Student is already in the new classroom.")
        return

    classrooms[current_classroom].remove(student)
    classrooms[new_classroom].append(student)

    save_data()

    print("Student moved successfully.")


def remove_student():
    classroom = input("Enter classroom name: ").strip()
    student = input("Enter student name: ").strip()

    if classroom not in classrooms:
        print("Error: Classroom does not exist.")
        return

    if student not in classrooms[classroom]:
        print("Error: Student is not in this classroom.")
        return

    classrooms[classroom].remove(student)
    save_data()

    print("Student removed successfully.")


def delete_classroom():
    classroom = input("Enter classroom name: ").strip()

    if classroom not in classrooms:
        print("Error: Classroom does not exist.")
        return

    if classrooms[classroom]:
        print("Error: Classroom must be empty before it can be deleted.")
        return

    del classrooms[classroom]
    save_data()

    print("Classroom deleted successfully.")


def largest_classroom():
    if not classrooms:
        print("No classrooms found.")
        return

    largest = max(classrooms, key=lambda classroom: len(classrooms[classroom]))

    print("Largest classroom:", largest)
    print("Number of students:", len(classrooms[largest]))


while True:
    print("\n===== CLASSROOM MANAGER =====")
    print("1. View Classrooms")
    print("2. Add Classroom")
    print("3. Add Student")
    print("4. Move Student")
    print("5. Remove Student")
    print("6. Delete Classroom")
    print("7. Largest Classroom")
    print("8. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_classrooms()

    elif choice == "2":
        add_classroom()

    elif choice == "3":
        add_student()

    elif choice == "4":
        move_student()

    elif choice == "5":
        remove_student()

    elif choice == "6":
        delete_classroom()

    elif choice == "7":
        largest_classroom()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-8.")
