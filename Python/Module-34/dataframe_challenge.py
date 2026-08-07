import pandas as pd

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Male"],
    "Salary": [15000, 12000, 14000, 13500, 11000, 12500],
    "Bonus": [2000, 1500, 2500, 2200, 1200, 1800]
}

df = pd.DataFrame(employees)

print(df)

df["Total Income"] = df["Salary"] + df["Bonus"]

group_by_department = df.groupby("Department")["Total Income"].mean()

print(group_by_department)

report_for_salary = df.groupby("Department")["Salary"].agg(
    ["count", "sum", "mean", "max", "min"]
)

print()

print(report_for_salary)

group_by_department_gender = df.groupby(["Department", "Gender"])["Salary"].mean()

print()

print(group_by_department_gender)

df = df.sort_values(by="Total Income", ascending=False)

df.to_csv("employees_report.csv", index=False)

df.to_excel("employees_report.xlsx", index=False)

df = pd.read_csv("employees_report.csv")

print(df)
