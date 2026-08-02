import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef"],
    "Math": [85, 70, 95, 80, 60],
    "Physics": [90, 65, 98, 84, 58],
    "AI": [88, 68, 94, 82, 62]
}

df = pd.DataFrame(students)

print(df.iloc[0])

print(df.iloc[1, 2])

print(df.iloc[[2, 4]])

print(df.iloc[:, [2, 3]])

print(df.iloc[0:4])

print(df.iloc[2:5])

print(df.iloc[:, [1, 2]])

print(df.iloc[1:4, 1:3])
