import pandas as pd
import numpy as np

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali"],
    "Department": ["IT", "HR", "AI", "IT", "Sales"],
    "Salary": [15000, 12000, 18000, 14000, 11000]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")
print(df)

df["Bonus"] = df["Salary"].apply(
    lambda x: 3000 if x >= 15000 else 1500
)

print("===== Data with Bonus =====")
print(df)

df["Total Income"] = df["Salary"] + df["Bonus"]

print("===== Data with Total Income =====")
print(df)

df["Status"] = df["Total Income"].apply(
    lambda x: "High" if x >= 20000
    else "Medium" if x >= 15000
    else "Low"
)

print("===== Final Data =====")
print(df)

