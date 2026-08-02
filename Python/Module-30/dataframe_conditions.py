import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef"],
    "Math": [85, 70, 95, 80, 60],
    "Physics": [90, 65, 98, 84, 58],
    "AI": [88, 68, 94, 82, 62]
}

df = pd.DataFrame(students)

print(df[df["Math"] > 80])

print(df[df["Physics"] < 70])

print(df[df["AI"] == 82])

print(df[df["Physics"] != 84])

print(df[(df["Math"] > 80) & (df["Physics"] > 85)])

print(df[(df["Math"] < 70) | (df["AI"] > 90)])
