# Question (1)

import pandas as pd
import numpy as np

students = {
    "Name": [
        "Ahmed",
        "Omar",
        "Sara",
        "Mariam",
        "Ali",
        "Youssef",
        "Ahmed"
    ],
    "Department": [
        "IT",
        "HR",
        "AI",
        "IT",
        "Sales",
        "AI",
        "IT"
    ],
    "Math": [
        85,
        70,
        95,
        80,
        np.nan,
        75,
        85
    ],
    "Physics": [
        90,
        65,
        np.nan,
        84,
        88,
        78,
        90
    ],
    "AI": [
        88,
        68,
        94,
        np.nan,
        90,
        82,
        88
    ]
}

df = pd.DataFrame(students)

print(df.duplicated())

clean_df = df.drop_duplicates()

print()

clean_df = df.copy()

clean_df["Math"] = clean_df["Math"].fillna(clean_df["Math"].mean())

clean_df["Physics"] = clean_df["Physics"].fillna(clean_df["Physics"].mean())

clean_df["AI"] = clean_df["AI"].fillna(clean_df["AI"].mean())

clean_df["Total"] = clean_df["Math"] + clean_df["Physics"] + clean_df["AI"]

clean_df["Average"] = clean_df["Total"] / 3

clean_df["Status"] = np.where(clean_df["Average"] >= 80 , "Pass" , "Fail")

clean_df = clean_df[clean_df["Average"] >= 80]

clean_df = clean_df.sort_values(by="Average", ascending=False)

clean_df = clean_df.reset_index(drop=True)

print(clean_df)
