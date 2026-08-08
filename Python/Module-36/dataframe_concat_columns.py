import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95]
}

grades = {
    "Physics": [90, 65, 98],
    "AI": [88, 68, 94]
}

df1 = pd.DataFrame(students)
df2 = pd.DataFrame(grades)

print("===== DataFrame 1 =====")
print(df1)

print()

print("===== DataFrame 2 =====")
print(df2)

print()

combined_df = pd.concat([df1, df2], axis=1)

print("===== Combined Data =====")
print(combined_df)
