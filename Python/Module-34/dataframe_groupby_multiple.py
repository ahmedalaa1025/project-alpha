import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Department": ["AI", "AI", "Networks", "Networks", "AI", "Networks"],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Male"],
    "Math": [85, 70, 95, 80, 88, 75]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

report = df.groupby(["Department", "Gender"])["Math"].mean()

print("===== GroupBy Department & Gender =====")
print(report)
