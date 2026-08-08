import pandas as pd

students_1 = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95]
}

students_2 = {
    "Name": ["Mariam", "Ali", "Youssef"],
    "Math": [80, 88, 75]
}

df1 = pd.DataFrame(students_1)
df2 = pd.DataFrame(students_2)

print("===== DataFrame 1 =====")
print(df1)

print()

print("===== DataFrame 2 =====")
print(df2)

combined_df = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("===== Combined Data =====")
print(combined_df)
