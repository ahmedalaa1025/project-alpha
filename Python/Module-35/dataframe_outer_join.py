import pandas as pd

students = {
    "StudentID": [1, 2, 3, 4, 5],
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali"]
}

grades = {
    "StudentID": [1, 2, 3, 4, 6],
    "Math": [85, 70, 95, 80, 90]
}

students_df = pd.DataFrame(students)
grades_df = pd.DataFrame(grades)

outer_join = pd.merge(
    students_df,
    grades_df,
    on="StudentID",
    how="outer"
)

print("===== Outer Join =====")
print(outer_join)
