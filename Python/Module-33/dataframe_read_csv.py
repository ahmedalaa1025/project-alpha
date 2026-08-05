import pandas as pd

df = pd.read_csv("students.csv")

print("===== Students Data =====")
print(df)

print()

print(df.shape)

print()

print(df.columns)

print()

print(df.dtypes)
