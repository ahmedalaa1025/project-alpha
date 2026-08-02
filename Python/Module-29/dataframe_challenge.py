import pandas as pd
import numpy as np

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef"],
    "Math": [85, 70, 95, 80, 60],
    "Physics": [90, 65, 98, 84, 58],
    "AI": [88, 68, 94, 82, 62]
}

df = pd.DataFrame(students)

print("===== Student Data =====")

print()

print(df.shape)

print(df.size)

print(df.ndim)

print(df.columns)

print(df.dtypes)

print()

print(df.head(3))

print(df.tail(2))

print()

print(df["Name"])

print(df["Math"])

df["Total"] = df["Math"] + df["Physics"] + df["AI"]

df["Average"] = df["Total"] / 3

df["Status"] = np.where(df["Average"] >= 70 , "Pass" , "Fail")

df["AI"] = df["AI"] + 5

df.loc[4, "Math"] = 75

df = df.drop(columns=["Total"])

print(df)
