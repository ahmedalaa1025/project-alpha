import pandas as pd

grades = pd.Series(
    [85, 90, 78],
    index=["Ahmed", "Omar", "Sara"]
)

print(grades["Ahmed"])

print(grades.iloc[0])

print(grades.loc["Sara"])

grades["Ahmed"] = 100

print(grades)

grades.loc["Sara"] = 95

grades.iloc[1] = 80

print(grades)

grades["Mariam"] = 92

grades = grades.drop("Omar")

print(grades)

print(grades + 5)

print(grades * 2)

print(grades / 10)

print(grades > 80)

print(grades[grades > 80])
