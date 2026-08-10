# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Department": ["IT", "HR", "AI", "IT"]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# df["Department"] = df["Department"].replace(
#     "IT",
#     "Information Technology"
# )

# print("===== Updated Data =====")
# print(df)

# import pandas as pd

# employees = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Department": ["IT", "HR", "AI", "IT"]
# }

# df = pd.DataFrame(employees)

# print("===== Original Data =====")
# print(df)

# print()

# df["Department"] = df["Department"].replace({
#     "IT": "Information Technology",
#     "HR": "Human Resources",
#     "AI": "Artificial Intelligence"
# })

# print("===== Updated Data =====")
# print(df)

import pandas as pd

employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Department": ["IT", "HR", "AI", "IT"],
    "Status": ["Active", "Inactive", "Active", "Inactive"]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")
print(df)

print()

df = df.replace({
    "IT": "Information Technology",
    "HR": "Human Resources",
    "AI": "Artificial Intelligence",
    "Active": "Working",
    "Inactive": "Not Working"
})

print("===== Updated Data =====")
print(df)
