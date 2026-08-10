import pandas as pd

employees = {
    "Name": ["Ahmed", "Omar", "Sara","Ahmed", "Mariam", "Ali", "Youssef", "Omar"],
    "Department": ["IT", "HR", "AI", "IT", "Sales","IT", "AI", "HR"],
    "Salary": [15000, 12000, 18000, 15000, 11000, 14000, 16000, 12000]
}

df = pd.DataFrame(employees)

df = df.rename(columns={
    "Name": "Employee Name",
    "Department": "Department Name",
    "Salary": "Monthly Salary"
})

print("===== Duplicated Rows =====")
print(df.duplicated())

df = df.drop_duplicates()

print("===== After Removing Duplicates =====")
print(df)

print("===== Unique Departments =====")
print(df["Department Name"].unique())

print()

print("===== Number of Unique Departments =====")
print(df["Department Name"].nunique())

print()

print("===== Department Counts =====")
print(df["Department Name"].value_counts())

print()

print("===== Department Percentages =====")
print(df["Department Name"].value_counts(normalize=True))

df = df.drop(["Monthly Salary"], axis=1)

df = df.sort_values(by="Employee Name", ascending=True)

df.to_csv("employees_transform_report.csv", index=False)

df.to_excel("employees_transform_report.xlsx", index=False)

df = pd.read_csv("employees_transform_report.csv")

print(df)
