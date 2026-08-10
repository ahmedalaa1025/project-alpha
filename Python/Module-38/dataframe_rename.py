import pandas as pd

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Department": ["IT", "HR", "AI", "Sales"],
    "Salary": [15000, 12000, 18000, 11000]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")
print(df)

print()

df = df.rename(columns={
    "Name": "Employee Name",
    "Department": "Department Name",
    "Salary": "Monthly Salary"
})

print("===== Renamed Data =====")
print(df)
