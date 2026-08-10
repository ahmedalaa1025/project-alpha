# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Department": ["IT", "HR", "AI", "Sales"],
#     "Salary": [15000, 12000, 18000, 11000],
#     "Bonus": [3000, 1500, 3000, 1500]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# df = df.drop("Bonus", axis=1)

# print("===== After Dropping Bonus =====")
# print(df)

# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Department": ["IT", "HR", "AI", "Sales"],
#     "Salary": [15000, 12000, 18000, 11000],
#     "Bonus": [3000, 1500, 3000, 1500]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# df = df.drop(["Salary", "Bonus"], axis=1)

# print("===== After Dropping Salary & Bonus =====")
# print(df)

# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Department": ["IT", "HR", "AI", "Sales"],
#     "Salary": [15000, 12000, 18000, 11000]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# df = df.drop(2, axis=0)

# print("===== After Dropping Row 2 =====")
# print(df)

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

df = df.drop([1, 3], axis=0)

print("===== After Dropping Rows 1 & 3 =====")
print(df)
