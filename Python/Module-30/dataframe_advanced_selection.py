import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef"],
    "Math": [85, 70, 95, 80, 60],
    "Physics": [90, 65, 98, 84, 58],
    "AI": [88, 68, 94, 82, 62]
}

df = pd.DataFrame(students)

print(df[df["Name"].isin(["Ahmed", "Mariam"])])

print(df[df["Math"].between(70, 90)])

print(df[df["Physics"].between(60, 90)])

print(df[df["Name"].isin(["Youssef", "Omar"])])

print(df[df["AI"].between(80, 90)])

print(df[(df["Name"].isin(["Ahmed", "Sara"])) & df["Math"].between(80, 100)])
