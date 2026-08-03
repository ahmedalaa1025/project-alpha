import pandas as pd
import numpy as np

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef", "Ali"],
    "Math": [85, 70, 95, 80, 60, 88],
    "Physics": [90, 65, 98, 84, 58, 91],
    "AI": [88, 68, 94, 82, 62, 90]
}

df = pd.DataFrame(students)

print(df)

print()

df["Total"] = df["Math"] + df["Physics"] + df["AI"]

df["Average"] = df["Total"] / 3

df["Status"] = np.where(df["Average"] >= 80 , "Excellent" , "Good")

df.loc[4, "Math"] = 75

df["AI"] = df["AI"] + 3

df = df.rename(
    columns={
        "Math": "Mathematics",
        "Physics": "Physics Score",
        "AI": "Artificial Intelligence"
    }
)

df = df.sort_values(by="Average", ascending=False)

df = df.set_index("Name")

print(df.loc["Ahmed"])

df = df.reset_index()

print(df)
