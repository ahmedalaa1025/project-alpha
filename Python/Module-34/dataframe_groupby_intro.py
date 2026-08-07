import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Department": ["AI", "AI", "Networks", "Networks", "AI", "Networks"],
    "Math": [85, 70, 95, 80, 88, 75]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

group = df.groupby("Department")["Math"].mean()

print("===== Average Math Grade =====")
print(group)
