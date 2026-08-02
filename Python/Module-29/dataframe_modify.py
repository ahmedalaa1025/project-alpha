import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [95, 80, 97]
}

df = pd.DataFrame(students)

df["Total"] = df["Math"] + df["Physics"] + df["AI"]

print(df)

df["Average"] = df["Total"] / 3

print(df)

df["Physics"] = df["Physics"] + 2

print(df)

df.loc[2, "Math"] = 100

print(df)

df = df.drop(columns=["Total"])

print(df)
