# Requirements

# Build a program that helps students track their grades. 
# Students can input the grades they achieve for each subject, 
# and the program will read their grades from a file and calculate 
# their average grade. The program should handle exceptions (e.g., 
# invalid input, file errors) and store the grades in a file for future reference.

import json

# File path for storing grades
grades_file_path = 'student_grades.json'

def input_and_store_grades():
    grades = {}
    while True:
        subject = input("Enter subject (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        while True:
            try:
                grade = input(f"Enter grade for {subject}: ")
                grade = float(grade)  # Convert input to float; this also handles validation
                grades[subject] = grade
                break
            except ValueError:
                print("Invalid input. Please enter a numeric grade.")
    return grades

def calculate_and_display_average(grades):
    if not grades:
        print("No grades to calculate.")
        return
    average = sum(grades.values()) / len(grades)
    print(f"Average grade: {average:.2f}")

def store_grades(grades):
    try:
        with open(grades_file_path, 'w') as file:
            json.dump(grades, file)
        print("Grades saved successfully.")
    except Exception as e:
        print(f"Failed to save grades: {e}")

def main():
    print("Welcome to the Student Grade Tracker")
    grades = input_and_store_grades()
    calculate_and_display_average(grades)
    store_grades(grades)

if __name__ == "__main__":
    main()