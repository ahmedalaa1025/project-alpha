import pandas as pd
import numpy as np

employees = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali"]
}

departments = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Department": ["IT", "HR", "AI", "Finance", "Sales"]
}

salaries = {
    "EmployeeID": [1, 2, 3, 4, 5],
    "Salary": [15000, 12000, 18000, 14000, 11000]
}

employees_df = pd.DataFrame(employees)
departments_df = pd.DataFrame(departments)
salaries_df = pd.DataFrame(salaries)

merged_df = pd.merge(employees_df, departments_df, on="EmployeeID")
merged_df = pd.merge(merged_df, salaries_df, on="EmployeeID")

merged_df["Bonus"] = np.where(merged_df["Salary"] >= 15000 , 3000 , 1500)

merged_df["Total Income"] = merged_df["Salary"] + merged_df["Bonus"]

merged_df = merged_df.sort_values(by="Total Income", ascending=False)

merged_df.to_csv("employees_report.csv", index=False)

merged_df.to_excel("employees_report.xlsx", index=False)

merged_df = pd.read_csv("employees_report.csv")

print(merged_df)
