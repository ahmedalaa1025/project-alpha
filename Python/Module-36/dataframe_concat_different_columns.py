import pandas as pd

students_math = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95]
}

students_physics = {
    "Name": ["Mariam", "Ali", "Youssef"],
    "Physics": [84, 91, 78]
}

df1 = pd.DataFrame(students_math)
df2 = pd.DataFrame(students_physics)

print("===== Math Data =====")
print(df1)

print()

print("===== Physics Data =====")
print(df2)

print()

combined_df = pd.concat(
    [df1, df2],
    ignore_index=True
)

print("===== Combined Data =====")
print(combined_df)
