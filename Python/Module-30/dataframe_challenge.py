import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef", "Ali"],
    "Math": [85, 70, 95, 80, 60, 88],
    "Physics": [90, 65, 98, 84, 58, 91],
    "AI": [88, 68, 94, 82, 62, 90]
}

df = pd.DataFrame(students)

print(df)

print(df.loc[2])

print(df.iloc[0])

print(df.loc[:, ["Name", "AI"]])

print(df.iloc[0:3])

print(df[df["Math"] > 80])

print(df[df["Physics"] < 70])

print(df[df["AI"].between(80, 90)])

print(df[df["Name"].isin(["Ahmed", "Ali", "Sara"])])

print(df[(df["Math"] > 80) & (df["Physics"] > 85)])

print(df[(df["Math"] < 70) | (df["AI"] > 90)])

print(df[(df["Name"].isin(["Ahmed", "Sara"])) & df["Math"].between(80, 100)])
