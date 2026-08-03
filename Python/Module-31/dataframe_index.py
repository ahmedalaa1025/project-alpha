import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [88, 68, 94]
}

df = pd.DataFrame(students)

print("===== Original =====")
print(df)

print()

df = df.set_index("Name")

print("===== New Index =====")
print(df)

print(df.loc["Sara"])

print()

df = df.reset_index()

print("===== Reset Index =====")

print(df)

print()

df = df.reset_index(drop=True)

print(df)
