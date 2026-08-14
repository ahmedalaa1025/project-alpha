import pandas as pd

employees = {
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
    "Salary": [
        15000,
        12000,
        18000,
        14000,
        11000,
        16000,
        15000
    ]
}

df = pd.DataFrame(employees)

duplicate_rows = df[
    df.duplicated()
]

print("===== Duplicate Rows =====")

print(duplicate_rows)

print()

print("===== Number of Duplicate Rows =====")

print(df.duplicated().sum())

print()

clean_df = df.drop_duplicates()

print(clean_df)

print()

advanced_analysis = clean_df.groupby("Department").agg(
    Salary_Mean=("Salary", "mean"),
    Salary_Max=("Salary", "max"),
    Salary_Min=("Salary", "min"),
    Salary_Sum=("Salary", "sum"),
    Salary_Count=("Salary", "count")
)

print("===== Advanced Salary Analysis =====")

print(advanced_analysis)

print()

clean_df["Department Average Salary"] = (
    clean_df.groupby("Department")["Salary"]
      .transform("mean")
)

clean_df["Salary Difference"] = (
    clean_df["Salary"] - clean_df["Department Average Salary"]
)


print("===== Transform Analysis =====")
print(clean_df)

clean_df["Department Rank"] = (
    clean_df.groupby("Department")["Salary"]
      .rank(
          ascending=False,
          method="dense"
      )
)


print("===== Department Salary Ranking =====")
print(clean_df)

print()

clean_df["Bonus"] = clean_df["Salary"] * 0.10

clean_df["Total Income"] = (
    clean_df["Salary"] + clean_df["Bonus"]
)

clean_df = clean_df[clean_df["Total Income"] >= 15000]

clean_df = clean_df.sort_values(
    by="Total Income",
    ascending=False
)

clean_df = clean_df.reset_index(drop=True)

print("===== Final Advanced Data =====")

print(clean_df)
