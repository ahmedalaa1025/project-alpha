# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Ahmed", "Mariam"],
#     "Department": ["IT", "HR", "AI", "IT", "Sales"],
#     "Salary": [15000, 12000, 18000, 15000, 11000]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# print("===== Duplicated Rows =====")
# print(df.duplicated())

# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Ahmed", "Mariam"],
#     "Department": ["IT", "HR", "AI", "IT", "Sales"],
#     "Salary": [15000, 12000, 18000, 15000, 11000]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# df = df.drop_duplicates()

# print("===== After Removing Duplicates =====")
# print(df)

# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Ahmed", "Mariam"],
#     "Department": ["IT", "HR", "AI", "Networks", "Sales"],
#     "Salary": [15000, 12000, 18000, 16000, 11000]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# print("===== Duplicate Names =====")
# print(df.duplicated(subset=["Name"]))

import pandas as pd

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Ahmed", "Mariam"],
    "Department": ["IT", "HR", "AI", "Networks", "Sales"],
    "Salary": [15000, 12000, 18000, 16000, 11000]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")
print(df)

print()

df = df.drop_duplicates(subset=["Name"])

print("===== After Removing Duplicate Names =====")
print(df)
