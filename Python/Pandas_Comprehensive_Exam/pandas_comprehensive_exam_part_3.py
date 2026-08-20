# Question (3)

import pandas as pd
import numpy as np

employees = {
    "Name": [
        "Ahmed",
        "Omar",
        "Sara",
        "Mariam",
        "Ali",
        "Youssef",
        "Khaled",
        "Nour"
    ],
    "Department": [
        "IT",
        "HR",
        "AI",
        "IT",
        "Sales",
        "AI",
        "IT",
        "HR"
    ],
    "Salary": [
        15000,
        12000,
        18000,
        14000,
        11000,
        16000,
        13000,
        13500
    ]
}

df = pd.DataFrame(employees)

department_analysis = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Employee_Count=("Name", "count")
)

df["Department Average Salary"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)

df["Salary Difference"] = (
    df["Salary"] - df["Department Average Salary"]
)

df["Salary Rank"] = df["Salary"].rank(
    ascending=False,
    method="dense"
)

df["Department Rank"] = (
    df.groupby("Department")["Salary"]
      .rank(
          ascending=False,
          method="dense"
      )
)

df["Bonus"] = df["Salary"] * 0.10

df["Total Income"] = (
    df["Salary"] + df["Bonus"]
)

df = df[
    df["Total Income"] >= 15000
]

df = df.sort_values(
    by="Total Income",
    ascending=False
)

df = df.reset_index(drop=True)

print(df)
