import pandas as pd

grades = pd.Series([85, 90, 78, 95])

print(grades.shape)

print(grades.size)

print(grades.dtype)

print(grades.index)

# grades = pd.Series(
#     [85,90,78],
#     index=["Ahmed","Omar","Sara"]
# )

# print(grades.index)

print(grades.values)

print(grades.head())

print(grades.head(2))

print(grades.tail())

print(grades.tail(2))

print(grades.sum())

print(grades.mean())

print(grades.max())

print(grades.min())

print(grades.describe())
