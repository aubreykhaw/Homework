# ============================================
# Assignment: Grade Report Generator
# ============================================
#
# Objective:
# Practice using dictionaries, lists, loops,
# sorting, searching, and calculations to
# generate a report about student grades.
#
# --------------------------------------------
# DATA STRUCTURE
# --------------------------------------------
#
# Example:
#
# grades = {
#     "Alice": [85, 92, 78],
#     "Bob": [90, 88, 95],
#     "Charlie": [72, 80, 75],
#     "David": [100, 94, 98]
# }
#
# Each student has a list of grades.
#
# --------------------------------------------
# MENU OPTIONS
# --------------------------------------------
#
# 1. View All Grades
# 2. Add Student
# 3. Add Grade
# 4. Student Report
# 5. Class Average
# 6. Highest Average
# 7. Lowest Average
# 8. Students Passing
# 9. Students Failing
# 10. Sort By Average
# 11. Remove Student
# 12. Exit
#
# --------------------------------------------
# REQUIREMENTS
# --------------------------------------------
#
# 1. VIEW ALL GRADES
# ------------------
# Display every student and their grades.
#
# Example:
#
# Alice: [85, 92, 78]
# Bob: [90, 88, 95]
#
#
# 2. ADD STUDENT
# ---------------
# Ask for a student name.
#
# Add the student with an empty list.
#
# Requirements:
# - Name cannot be empty.
# - Student cannot already exist.
#
#
# 3. ADD GRADE
# ------------
# Ask for:
# - student name
# - grade
#
# Add the grade to the student's list.
#
# Requirements:
# - Student must exist.
# - Grade must be between 0 and 100.
#
#
# 4. STUDENT REPORT
# -----------------
# Ask for a student name.
#
# Display:
# - Their grades
# - Their average
# - Their highest grade
# - Their lowest grade
#
# Example:
#
# Alice
# Grades: [85, 92, 78]
# Average: 85.0
# Highest: 92
# Lowest: 78
#
#
# 5. CLASS AVERAGE
# ----------------
# Calculate the average of every grade
# from every student.
#
# Example:
#
# Alice: [80, 90]
# Bob: [70, 100]
#
# Class average: 85.0
#
#
# 6. HIGHEST AVERAGE
# ------------------
# Find the student with the highest
# average grade.
#
# Display:
#
# Highest average:
# Alice - 94.5
#
#
# 7. LOWEST AVERAGE
# -----------------
# Find the student with the lowest
# average grade.
#
#
# 8. STUDENTS PASSING
# -------------------
# Display every student whose average
# is 70 or higher.
#
# Example:
#
# Passing Students:
# Alice - 85.0
# Bob - 78.5
#
#
# 9. STUDENTS FAILING
# -------------------
# Display every student whose average
# is below 70.
#
#
# 10. SORT BY AVERAGE
# -------------------
# Display all students from highest
# average to lowest average.
#
# Example:
#
# 1. David - 97.3
# 2. Alice - 91.5
# 3. Bob - 84.2
# 4. Charlie - 68.5
#
# Hint:
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
try:
    file_path = os.path.join(BASE_DIR, "grades.json")
    with open(file_path, "r") as file:
        grades = json.load(file)
except FileNotFoundError:
    grades = {}


# --------------------------------------------
# SAVE DATA
# --------------------------------------------

def save_data():
    with open(file_path, "w") as file:
        json.dump(grades, file)


# --------------------------------------------
# VIEW ALL GRADES
# --------------------------------------------

def view_grades():
    if len(grades) == 0:
        print("There are no students yet.")
    else:
        for student in grades:
            print(student + ":", grades[student])


# --------------------------------------------
# ADD STUDENT
# --------------------------------------------

def add_student():
    student = input("Enter student name: ").strip()

    if student == "":
        print("Name cannot be empty.")

    elif student in grades:
        print("Student already exists.")

    else:
        grades[student] = []
        save_data()
        print("Student added.")


# --------------------------------------------
# ADD GRADE
# --------------------------------------------

def add_grade():
    student = input("Enter student name: ").strip()

    if student not in grades:
        print("Student does not exist.")

    else:
        grade = float(input("Enter grade: "))

        if grade < 0 or grade > 100:
            print("Grade must be between 0 and 100.")

        else:
            grades[student].append(grade)
            save_data()
            print("Grade added.")


# --------------------------------------------
# STUDENT REPORT
# --------------------------------------------

def student_report():
    student = input("Enter student name: ").strip()

    if student not in grades:
        print("Student does not exist.")

    elif len(grades[student]) == 0:
        print("This student has no grades yet.")

    else:
        total = 0

        for grade in grades[student]:
            total += grade

        average = total / len(grades[student])

        print(student)
        print("Grades:", grades[student])
        print("Average:", average)
        print("Highest:", max(grades[student]))
        print("Lowest:", min(grades[student]))


# --------------------------------------------
# CLASS AVERAGE
# --------------------------------------------

def class_average():
    total = 0
    count = 0

    for student in grades:
        for grade in grades[student]:
            total += grade
            count += 1

    if count == 0:
        print("There are no grades yet.")

    else:
        average = total / count
        print("Class average:", average)


# --------------------------------------------
# HIGHEST AVERAGE
# --------------------------------------------

def highest_average():
    if len(grades) == 0:
        print("There are no students yet.")

    else:
        highest = 0
        for student in grades:
            if len(grades[student]) == 0:
                continue

            total = sum(grades[student])
            average = total / len(grades[student])
            if average > highest:
                highest = average

            print("Highest average:", highest)


# --------------------------------------------
# LOWEST AVERAGE
# --------------------------------------------

def lowest_average():
    if len(grades) == 0:
        print("There are no students yet.")
    else:
        # float('inf') # sets to positive infinity
        lowest = 100  
        for student in grades:
            if len(grades[student]) == 0:
                continue
            total = sum(grades[student])
            average = total / len(grades[student])
            if average < lowest:
                lowest = average
            print("Lowest average:", lowest)


# --------------------------------------------
# STUDENTS PASSING
# --------------------------------------------

def students_passing():
    if len(grades) == 0:
        print("There are no students yet.")
    else:
        passing_students = []
        for student in grades:
            if len(grades[student]) == 0:
                continue
            total = sum(grades[student])
            average = total / len(grades[student])
            if average >= 70:
                passing_students.append((student, average)) # tuple 
                if len(passing_students) == 0:
                    print("There are no passing students.")
                else:
                    print("Passing Students:")
                    for student, average in passing_students:
                        print(f"{student} - {average}")


# --------------------------------------------
# STUDENTS FAILING
# --------------------------------------------

def students_failing():
    if len(grades) == 0:
        print("There are no students yet.")
    else:
        failing_students = []
        for student in grades:
            if len(grades[student]) == 0:
                continue
            total = sum(grades[student])
            average = total / len(grades[student])
            if average < 70:
                failing_students.append((student, average))
                if len(failing_students) == 0:
                    print("There are no failing students.")
                else:
                    print("Failing Students:")
                    for student, average in failing_students:
                        print(f"{student} - {average}")



# --------------------------------------------
# SORT BY AVERAGE
# --------------------------------------------

def sort_by_average():
    if len(grades) == 0:
        print("There are no students yet.")
    else:
        averages = []
        for student in grades:
            if len(grades[student]) == 0:
                continue
            total = sum(grades[student])
            average = total / len(grades[student])
            averages.append((student, average))
            
        # averages.sort(key=lambda x: x[1], reverse=True)
        sorted_average = []
        while len(averages)> 0:
            highest_average = 0
            highest_student = ""

            for student, average in averages:
                if average > highest_average:
                    highest_average = average
                    highest_student = student

            sorted_average.append((highest_student, highest_average))
            averages.remove((highest_student, highest_average))
        


        print("Students sorted by average:")
        for i, (student, average) in enumerate(sorted_average, start=1):
            print(f"{i}. {student} - {average}")


# --------------------------------------------
# REMOVE STUDENT
# --------------------------------------------

def remove_student():
    student = input("Enter student name: ").strip()

    if student not in grades:
        print("Student does not exist.")

    else:
        del grades[student]
        save_data()
        print("Student removed.")


# --------------------------------------------
# MAIN MENU
# --------------------------------------------

while True:

    print("\n===== GRADE REPORT GENERATOR =====")
    print("1. View All Grades")
    print("2. Add Student")
    print("3. Add Grade")
    print("4. Student Report")
    print("5. Class Average")
    print("6. Highest Average")
    print("7. Lowest Average")
    print("8. Students Passing")
    print("9. Students Failing")
    print("10. Sort By Average")
    print("11. Remove Student")
    print("12. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        view_grades()

    elif choice == "2":
        add_student()

    elif choice == "3":
        add_grade()

    elif choice == "4":
        student_report()

    elif choice == "5":
        class_average()
# -----------------------------------
    elif choice == "6":
        highest_average()

    elif choice == "7":
        lowest_average()

    elif choice == "8":
        students_passing()

    elif choice == "9":
        students_failing()

    elif choice == "10":
        sort_by_average()

    elif choice == "11":
        remove_student()

    elif choice == "12":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number from 1-12.")