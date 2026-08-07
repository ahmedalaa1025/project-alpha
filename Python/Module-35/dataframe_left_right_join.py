import pandas as pd

students = {
    "StudentID": [1, 2, 3, 4, 5],
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali"]
}

grades = {
    "StudentID": [1, 2, 3, 4],
    "Math": [85, 70, 95, 80]
}

students_df = pd.DataFrame(students)
grades_df = pd.DataFrame(grades)

print("===== Left Join =====")

left_join = pd.merge(
    students_df,
    grades_df,
    on="StudentID",
    how="left"
)

print(left_join)

print()

print("===== Right Join =====")

right_join = pd.merge(
    students_df,
    grades_df,
    on="StudentID",
    how="right"
)

print(right_join)
