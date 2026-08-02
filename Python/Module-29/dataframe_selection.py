import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [95, 80, 97]
}

df = pd.DataFrame(students)

print(df["Math"])

print()

print(df["Name"])

print()

print(df[["Math", "Physics"]])

print()

print(df[["Math", "Physics", "AI"]])

print()

print(type(df["Math"]))

print(type(df[["Math", "Physics"]]))
