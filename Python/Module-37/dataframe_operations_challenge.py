import pandas as pd
import numpy as np

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Department": ["IT", "HR", "AI", "IT", "Sales", "AI"],
    "Salary": [15000, 12000, 18000, 14000, 11000, 16000]
}

df = pd.DataFrame(employees)

df["Bonus"] = df["Salary"].apply(
    lambda x: 3000 if x >= 15000 else 1500
)

df["Total Income"] = df["Salary"] + df["Bonus"]

df["Status"] = df["Total Income"].apply(
    lambda x: "High" if x >= 20000
    else "Medium" if x >= 15000
    else "Low"
)

df["Department"] = df["Department"].replace({
    "IT": "Information Technology",
    "HR": "Human Resources",
    "AI": "Artificial Intelligence"
})

df["Department Code"] = df["Department"].map({
    "Information Technology": "IT",
    "Human Resources": "HR",
    "Artificial Intelligence": "AI",
    "Sales": "SALES"
})

df = df.sort_values(by="Total Income", ascending=False)

df.to_csv("employees_operations_report.csv", index=False)

df.to_excel("employees_operations_report.xlsx", index=False)

df = pd.read_csv("employees_operations_report.csv")

print(df)
