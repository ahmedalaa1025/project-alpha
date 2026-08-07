import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Department": ["AI", "AI", "Networks", "Networks", "AI", "Networks"],
    "Math": [85, 70, 95, 80, 88, 75],
    "Physics": [90, 65, 98, 84, 91, 78]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

report = df.groupby("Department").agg({
    "Math": ["mean", "max", "min"],
    "Physics": ["mean", "max", "min"]
})

print("===== Department Report =====")
print(report)
