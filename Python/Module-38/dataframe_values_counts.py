import pandas as pd

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Department": ["IT", "HR", "AI", "IT", "Sales", "AI"],
    "Salary": [15000, 12000, 18000, 14000, 11000, 16000]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")
print(df)

print()

print("===== Unique Departments =====")
print(df["Department"].unique())

print()

print("===== Number of Unique Departments =====")
print(df["Department"].nunique())


print()

print("===== Department Counts =====")
print(df["Department"].value_counts())

print()

print("===== Department Percentages =====")
print(df["Department"].value_counts(normalize=True))
