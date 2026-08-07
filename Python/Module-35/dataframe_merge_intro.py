import pandas as pd

students = {
    "StudentID": [1, 2, 3, 4],
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"]
}

grades = {
    "StudentID": [1, 2, 3, 4],
    "Math": [85, 70, 95, 80],
    "Physics": [90, 65, 98, 84]
}

df_students = pd.DataFrame(students)
df_grades = pd.DataFrame(grades)

print("===== Students =====")
print(df_students)

print()

print("===== Grades =====")
print(df_grades)

print()

merged = pd.merge(df_students, df_grades, on="StudentID")

print("===== Merged Data =====")
print(merged)
