import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef"],
    "Math": [85, 70, 95, 80, 60],
    "Physics": [90, 65, 98, 84, 58],
    "AI": [88, 68, 94, 82, 62]
}

df = pd.DataFrame(students)

print(df)

print(df.loc[1])

print(df.loc[2, "AI"])

print(df.loc[[0, 4]])

print(df.loc[:, ["Math", "Physics"]])

print(df.loc[[2, 3], ["AI", "Physics"]])
