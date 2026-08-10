# import pandas as pd

# students = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Math": [85, 70, 95, 80]
# }

# df = pd.DataFrame(students)

# print("===== Original Data =====")
# print(df)

# print()

# df["Math"] = df["Math"].apply(lambda x: x + 5)

# df["Math"] = df["Math"].apply(
#     lambda x: x + 10 if x >= 80 else x + 5
# )

# print("===== Updated Data =====")
# print(df)

import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Math": [85, 70, 95, 80],
    "Physics": [90, 65, 98, 84]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

df["Total"] = df.apply(
    lambda row: row["Math"] + row["Physics"],
    axis=1
)

print("===== Data with Total =====")
print(df)

df["Average"] = df.apply(
    lambda row: (row["Math"] + row["Physics"]) / 2,
    axis=1
)

df["Status"] = df.apply(
    lambda row: "Pass" if row["Average"] >= 85 else "Fail",
    axis=1
)

print("===== Final Data =====")
print(df)
