import pandas as pd


employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05"
    ]
}


df = pd.DataFrame(employees)


print("===== Original Data =====")
print(df)

print()

print("===== Data Types =====")
print(df.dtypes)

print()

df["Join Date"] = pd.to_datetime(df["Join Date"])


print("===== Converted Data =====")
print(df)

print()

print("===== Data Types After Conversion =====")
print(df.dtypes)

import pandas as pd


employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05"
    ]
}


df = pd.DataFrame(employees)


df["Join Date"] = pd.to_datetime(df["Join Date"])


df["Year"] = df["Join Date"].dt.year

df["Month"] = df["Join Date"].dt.month

df["Day"] = df["Join Date"].dt.day

df["Day of Week"] = df["Join Date"].dt.dayofweek


print("===== Data with Date Components =====")
print(df)
