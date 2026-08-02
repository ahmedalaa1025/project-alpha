import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [95, 80, 97]
}

df = pd.DataFrame(students)

print(df.shape)

print(df.size)

print(df.ndim)

print(df.columns)

print(df.index)

print(df.values)

print(df.dtypes)

print(df.head())

print(df.tail(2))

print(df.info())

print(df.describe())
