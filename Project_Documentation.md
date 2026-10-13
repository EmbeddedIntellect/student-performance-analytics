# Student Performance Analytics System

## 1. Project Overview
The Student Performance Analytics System is a Python-based project
that analyzes student academic performance using Pandas and NumPy.

## 2. Project Objectives
- Organize student records using a Pandas DataFrame.
- Calculate total and average marks for each student.
- Assign grades using defined grading rules.
- Identify pass and fail students.
- Analyze overall class performance.
- Perform subject-wise performance analysis.
- Identify top-performing students.

## 3. Technologies Used
- Python
- NumPy
- Pandas

## 4. Dataset Description
The dataset contains 500 student records with the following fields:
- Student ID
- Name
- Department
- Python marks
- Mathematics marks
- AI marks
- Statistics marks
- Communication marks
- Attendance percentage

## 5. Implementation
The project reads student records from a CSV file and organizes
them using a Pandas DataFrame. NumPy is used for numerical
calculations, while reusable functions and loops support processing.

## 6. Grading Rules
- A+: Average marks >= 90
- A: Average marks >= 80 and < 90
- B: Average marks >= 70 and < 80
- C: Average marks >= 60 and < 70
- D: Average marks >= 50 and < 60
- F: Average marks < 50

## 7. Pass/Fail Rule
A student passes if they obtain at least 40 marks in every subject.
Otherwise, the student is classified as Fail.

## 8. Analysis and Outputs
- Total and average marks for each student
- Overall class average
- Highest and lowest student averages
- Pass/fail statistics
- Grade distribution
- Subject-wise performance
- Top-performing students
- CSV reports containing analysis results

## 9. Project Files
- main.py: Main executable program
- students.csv: Original student dataset
- functions.py: Reusable functions (optional)
- Project_Documentation.md: Project documentation

## 10. Conclusion
The project demonstrates basic Python programming and data analysis
by processing student records and generating meaningful performance
summaries without using machine learning.
