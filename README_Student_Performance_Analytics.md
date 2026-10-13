# Student Performance Analytics System

A beginner-friendly Python project that analyzes **500 synthetic student records** using Pandas, NumPy, and Matplotlib. It calculates totals and averages, assigns grades, determines pass/fail status, ranks students, compares subject performance, creates charts, and exports CSV reports.

> **Important:** The data is synthetic and is for educational demonstration only. This project does not use machine learning.

## Features

- Generates 500 synthetic student records.
- Stores the dataset in `students.csv`.
- Checks dataset dimensions, missing values, duplicate student IDs, and mark/attendance ranges.
- Calculates total marks and average marks across five subjects.
- Assigns grades using predefined grade boundaries.
- Marks a student as Pass only if every subject score is at least 40.
- Reports class pass/fail percentages and grade distribution.
- Finds highest- and lowest-performing students and ranks the top 10.
- Summarizes average, highest, and lowest marks by subject.
- Creates a subject-average bar chart, pass/fail pie chart, and average-mark histogram.
- Exports CSV analysis reports.

## Technologies

- Python
- NumPy
- Pandas
- Matplotlib
- Google Colab
- CSV

## Dataset Fields

The original dataset has 9 columns:

`Student_ID`, `Name`, `Department`, `Python`, `Mathematics`, `AI`, `Statistics`, `Communication`, `Attendance`

Each subject is scored out of 100. Attendance is stored as a percentage.

## Grading Rules

| Average marks | Grade |
|---|---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

**Pass/Fail rule:** A student passes only if all five subject marks are at least 40. If any subject mark is below 40, the student fails.

## Results Shown in the Exported Notebook

- Student records: 500
- Original dataset size: 500 rows × 9 columns
- Missing values: 0
- Duplicate student IDs: 0
- Passed: 375 (75%)
- Failed: 125 (25%)
- Highest average shown: 94.4
- Lowest average shown: 27.8

These are results from the generated sample data, not real student performance. Run the notebook to reproduce and verify the outputs.

## Output Files

- `students.csv` — generated student dataset
- `student_performance_report.csv` — student details, calculations, grades, result, and rank
- `subject_performance_report.csv` — subject-wise average, highest, and lowest marks
- `grade_distribution_report.csv` — count of students in each grade
- `docs/Student_Performance_Analytics_Project_Report.pdf` — formal project report (if added)

## How to Run

1. Open `Student_Performance_Analytics.ipynb` in Google Colab.
2. Select **Runtime → Run all** (or run the cells in order from top to bottom).
3. Check that the dataset contains 500 records and the data-quality checks pass.
4. Check the displayed analysis and charts.
5. Download the generated CSV reports if you want to keep them in the repository.

## Repository Note

Upload the **actual `.ipynb` notebook** downloaded from Colab. The PDF export is useful as a readable copy, but it is not the editable notebook source. The current notebook output indicates that `main.py` and `functions.py` may be empty placeholders, so do not include them unless you add real code to them.

## Limitations

- Synthetic records only; no real student information is used.
- Grade boundaries and pass/fail rules are predefined for this demonstration.
- Descriptive analysis only; no machine learning is included.

## Author

Add your name, department, college, and academic year here before submitting.
