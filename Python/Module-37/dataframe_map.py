import pandas as pd

# students = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Grade": ["A", "B", "A", "C"]
# }

# df = pd.DataFrame(students)

# print("===== Original Data =====")
# print(df)

# print()

# df["Grade"] = df["Grade"].map(
#     {"A": "Excellent", "B": "Good", "C": "Pass"}
# )

# print("===== Updated Data =====")
# print(df)

# students = {
#     "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
#     "Math": [85, 70, 95, 80]
# }

# df = pd.DataFrame(students)

# df["Status"] = df["Math"].map(
#     lambda x: "Pass" if x >= 80 else "Fail"
# )

# print("===== Data with Status =====")
# print(df)

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Level": [3, 1, 3, 2]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

df["Level"] = df["Level"].map({
    1: "Beginner",
    2: "Intermediate",
    3: "Advanced"
})

print("===== Updated Data =====")
print(df)
