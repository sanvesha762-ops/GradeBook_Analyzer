"""
Project: GradeBook Analyzer
Course: Programming for Problem Solving using Python
Author: [Your Name Here]
Date: Oct 2024
Description: A CLI tool to analyze student marks, calculate statistics, 
             and generate formatted reports.
"""

import csv
import os
import statistics

# --- Task 3: Statistical Analysis Functions [cite: 36] ---

def calculate_average(marks_dict):
    """Calculates the mean of the marks."""
    if not marks_dict:
        return 0.0
    scores = list(marks_dict.values())
    return sum(scores) / len(scores)

def calculate_median(marks_dict):
    """Calculates the median of the marks."""
    if not marks_dict:
        return 0.0
    scores = list(marks_dict.values())
    return statistics.median(scores)

def find_max_score(marks_dict):
    """Finds the highest score."""
    if not marks_dict:
        return 0
    return max(marks_dict.values())

def find_min_score(marks_dict):
    """Finds the lowest score."""
    if not marks_dict:
        return 0
    return min(marks_dict.values())

# --- Task 4: Grade Assignment [cite: 47] ---

def assign_grade(score):
    """Returns a letter grade based on the score."""
    # Grading scale: A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60 [cite: 50]
    if score >= 90:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    else:
        return 'F'

def generate_grade_distribution(marks_dict):
    """Creates a dictionary of grades and counts distribution."""
    grades_dict = {}
    distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

    for name, score in marks_dict.items():
        grade = assign_grade(score)
        grades_dict[name] = grade
        distribution[grade] += 1
        
    return grades_dict, distribution

# --- Task 2: Data Input Functions [cite: 28] ---

def get_manual_input():
    """Gets student names and marks from user input."""
    marks = {}
    print("\n--- Manual Entry Mode ---")
    print("Type 'done' as the name to finish.")
    
    while True:
        name = input("Enter student name: ").strip()
        if name.lower() == 'done':
            break
        try:
            score = float(input(f"Enter marks for {name}: "))
            marks[name] = score
        except ValueError:
            print("Invalid input. Please enter a numeric value for marks.")
    return marks

def load_from_csv(filename):
    """Loads student data from a CSV file."""
    marks = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row if present
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    try:
                        score = float(row[1].strip())
                        marks[name] = score
                    except ValueError:
                        print(f"Skipping invalid score for {name}")
        print(f"Successfully loaded {len(marks)} records from {filename}.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return marks

# --- Main Application Logic ---

def main():
    print("========================================")
    print("Welcome to GradeBook Analyzer CLI")
    print("========================================")

    while True:
        marks_data = {}
        
        # Menu for Input Method
        print("\nSelect Input Method:")
        print("1. Manual Entry")
        print("2. Load from CSV")
        print("3. Exit")
        
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1':
            marks_data = get_manual_input()
        elif choice == '2':
            fname = input("Enter CSV filename (e.g., students.csv): ").strip()
            marks_data = load_from_csv(fname)
        elif choice == '3':
            print("Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        if not marks_data:
            print("No data loaded. returning to menu...")
            continue

        # Perform Analysis
        print("\n--- Statistical Analysis ---")
        avg = calculate_average(marks_data)
        med = calculate_median(marks_data)
        max_s = find_max_score(marks_data)
        min_s = find_min_score(marks_data)
        
        print(f"Average Score : {avg:.2f}")
        print(f"Median Score  : {med:.2f}")
        print(f"Highest Score : {max_s}")
        print(f"Lowest Score  : {min_s}")

        # Task 5: Pass/Fail Logic [cite: 54]
        # Passed: Score >= 40, Failed: Score < 40
        passed_students = [name for name, score in marks_data.items() if score >= 40]
        failed_students = [name for name, score in marks_data.items() if score < 40]

        print(f"\nTotal Passed: {len(passed_students)} {passed_students}")
        print(f"Total Failed: {len(failed_students)} {failed_students}")

        # Task 4 & 6: Grade Assignment & Output Table [cite: 62]
        student_grades, dist = generate_grade_distribution(marks_data)

        print("\n--- Student Report Card ---")
        print(f"{'Name':<15} {'Marks':<10} {'Grade':<5}")
        print("-" * 35)
        
        for name, score in marks_data.items():
            grade = student_grades[name]
            print(f"{name:<15} {score:<10} {grade:<5}")

        print("\n--- Grade Distribution ---")
        for grade, count in dist.items():
            print(f"Grade {grade}: {count} students")
        
        # Loop Check
        cont = input("\nWould you like to analyze another set? (y/n): ").lower()
        if cont != 'y':
            print("Exiting. Good luck!")
            break

if __name__ == "__main__":
    main()
    