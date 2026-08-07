import pandas as pd

students = {
    "StudentID": [1, 2, 3],
    "Name": ["Ahmed", "Omar", "Sara"]
}

grades = {
    "StudentID": [1, 2, 3],
    "Math": [85, 70, 95]
}

departments = {
    "StudentID": [1, 2, 3],
    "Department": ["AI", "Networks", "Cybersecurity"]
}

students_df = pd.DataFrame(students)
grades_df = pd.DataFrame(grades)
departments_df = pd.DataFrame(departments)

merged_df = pd.merge(students_df, grades_df, on="StudentID")

merged_df = pd.merge(merged_df, departments_df, on="StudentID")

print("===== Final Data =====")
print(merged_df)
