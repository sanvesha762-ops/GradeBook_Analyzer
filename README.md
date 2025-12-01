# GradeBook Analyzer

**Course:** Programming for Problem Solving using Python  
**Student Name:** Anvesha Saxena  
**Semester:** 1st Semester, 2025  
**Assignment:** Lab Assignment 2 (Mini Project)

## 📌 Project Overview
The **GradeBook Analyzer** is a Python-based Command Line Interface (CLI) tool designed to automate the process of analyzing student marks. It allows users to input data manually or via CSV, performs statistical analysis, assigns letter grades, and generates formatted reports.

This project was submitted by **Anvesha Saxena** as part of the 1st Semester coursework to demonstrate modular programming, file handling, and data analysis skills in Python.

## 🚀 Features
- **Data Input:**
  - **Manual Entry:** Interactive loop to enter names and marks.
  - **CSV Import:** Load student data automatically from a `.csv` file.
- **Statistical Analysis:** Calculates **Average**, **Median**, **Highest**, and **Lowest** scores.
- **Grading System:** Auto-assigns grades (A, B, C, D, F) based on score ranges.
- **Pass/Fail Logic:** Filters and lists students who passed (>= 40) or failed (< 40).
- **Reporting:** Displays a clean, formatted table of results.
- **Interactive Loop:** Allows multiple analyses without restarting the program.

## 📂 Project Structure
```text
gradebook_analyzer/
│
├── gradebook.py          # Main application script
├── students.csv          # Sample dataset for testing
└── README.md             # Project documentation
