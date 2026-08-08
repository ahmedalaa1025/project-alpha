import pandas as pd

semester_1 = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95]
}

semester_2 = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [88, 75, 98]
}

df1 = pd.DataFrame(semester_1)
df2 = pd.DataFrame(semester_2)

print("===== Semester 1 =====")
print(df1)

print()

print("===== Semester 2 =====")
print(df2)

print()

combined_df = pd.concat(
    [df1, df2],
    keys=["Semester 1", "Semester 2"]
)

print("===== Combined Data =====")
print(combined_df)
