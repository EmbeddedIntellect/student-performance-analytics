from pathlib import Path
import numpy as np
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "students.csv"
SUBJECTS = [
    "Python", "Mathematics", "AI",
    "Statistics", "Communication"
]


def calculate_grade(average):
    """Return a grade based on the student's average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


def calculate_student_performance(marks):
    """Calculate total and average marks."""
    marks = np.asarray(marks, dtype=float)
    return int(np.sum(marks)), round(float(np.mean(marks)), 2)


def analyze_students(df):
    """Calculate student results and create analysis reports."""
    df = df.copy()

    df["Total_Marks"] = df[SUBJECTS].sum(axis=1)
    df["Average_Marks"] = df[SUBJECTS].mean(axis=1).round(2)
    df["Grade"] = df["Average_Marks"].apply(calculate_grade)

    df["Result"] = np.where(
        df[SUBJECTS].ge(40).all(axis=1),
        "Pass",
        "Fail"
    )

    df["Rank"] = df["Average_Marks"].rank(
        method="first", ascending=False
    ).astype(int)

    return df


def main():
    if not DATA_FILE.exists():
        print("Error: students.csv was not found.")
        return

    df = pd.read_csv(DATA_FILE)

    missing_columns = [
        column for column in
        ["Student_ID", "Name", "Department", "Attendance"] + SUBJECTS
        if column not in df.columns
    ]

    if missing_columns:
        print("Missing required columns:", missing_columns)
        return

    df = analyze_students(df)

    output_file = PROJECT_DIR / "student_performance_report.csv"
    df.to_csv(output_file, index=False)

    subject_report = pd.DataFrame({
        "Average_Marks": df[SUBJECTS].mean().round(2),
        "Highest_Marks": df[SUBJECTS].max(),
        "Lowest_Marks": df[SUBJECTS].min()
    })
    subject_report.to_csv(
        PROJECT_DIR / "subject_performance_report.csv",
        index_label="Subject"
    )

    grade_counts = df["Grade"].value_counts().reindex(
        ["A+", "A", "B", "C", "D", "F"],
        fill_value=0
    )
    grade_counts.to_frame(
        name="Number_of_Students"
    ).to_csv(
        PROJECT_DIR / "grade_distribution_report.csv",
        index_label="Grade"
    )

    print("STUDENT PERFORMANCE ANALYTICS")
    print("-----------------------------")
    print("Total students:", len(df))
    print("Class average:", round(df["Average_Marks"].mean(), 2))
    print("Passed:", int((df["Result"] == "Pass").sum()))
    print("Failed:", int((df["Result"] == "Fail").sum()))

    print("\\nTop 10 students:")
    print(
        df.sort_values("Rank")[
            ["Rank", "Student_ID", "Name", "Average_Marks", "Grade", "Result"]
        ].head(10).to_string(index=False)
    )

    print("\\nSubject-wise analysis:")
    print(subject_report)

    print("\\nReports saved successfully.")


if __name__ == "__main__":
    main()
