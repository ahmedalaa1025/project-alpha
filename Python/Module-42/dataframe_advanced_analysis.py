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


high_salary_df = df[df["Salary"] >= 15000].copy()


high_salary_df["Bonus"] = high_salary_df["Salary"] * 0.10


high_salary_df["Total Income"] = (
    high_salary_df["Salary"] + high_salary_df["Bonus"]
)


print("===== High Salary Employees =====")
print(high_salary_df)

print()


department_analysis = df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Employee_Count=("Name", "count")
)


print("===== Department Analysis =====")
print(department_analysis)

print()


advanced_analysis = df.groupby("Department").agg(
    Salary_Mean=("Salary", "mean"),
    Salary_Max=("Salary", "max"),
    Salary_Min=("Salary", "min"),
    Salary_Sum=("Salary", "sum"),
    Salary_Count=("Salary", "count")
)


print("===== Advanced Salary Analysis =====")
print(advanced_analysis)

print()


df["Department Average Salary"] = (
    df.groupby("Department")["Salary"]
      .transform("mean")
)


df["Salary Difference"] = (
    df["Salary"] - df["Department Average Salary"]
)


print("===== Transform Analysis =====")
print(df)

print()


df["Salary Rank"] = df["Salary"].rank(
    ascending=False,
    method="dense"
)


print("===== Salary Ranking =====")
print(df)

print()


df["Department Rank"] = (
    df.groupby("Department")["Salary"]
      .rank(
          ascending=False,
          method="dense"
      )
)


print("===== Department Salary Ranking =====")
print(df)

print()


employees_with_duplicates = pd.DataFrame({
    "Name": [
        "Ahmed",
        "Omar",
        "Sara",
        "Ahmed",
        "Mariam",
        "Omar"
    ],
    "Department": [
        "IT",
        "HR",
        "AI",
        "IT",
        "Sales",
        "HR"
    ],
    "Salary": [
        15000,
        12000,
        18000,
        15000,
        11000,
        12000
    ]
})


print("===== Data with Possible Duplicates =====")
print(employees_with_duplicates)

print()


duplicate_mask = employees_with_duplicates.duplicated()


print("===== Duplicate Mask =====")
print(duplicate_mask)

print()


duplicate_rows = employees_with_duplicates[
    employees_with_duplicates.duplicated()
]


print("===== Duplicate Rows =====")
print(duplicate_rows)

print()


print("===== Number of Duplicate Rows =====")
print(
    employees_with_duplicates.duplicated().sum()
)

print()


advanced_df = df.copy()


advanced_df["Bonus"] = advanced_df["Salary"] * 0.10


advanced_df["Total Income"] = (
    advanced_df["Salary"] + advanced_df["Bonus"]
)


advanced_df = advanced_df[
    advanced_df["Total Income"] >= 15000
].copy()


advanced_df = advanced_df.sort_values(
    by="Total Income",
    ascending=False
)


advanced_df = advanced_df.reset_index(drop=True)


print("===== Advanced DataFrame Manipulation =====")
print(advanced_df)
