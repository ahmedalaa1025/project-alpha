import numpy as np
import pandas as pd

grades = pd.Series(
  [85, 90, 78, 95, 88, 92, 70, 65],
  index = ["Ahmed", "Omar", "Sara", "Mariam", "Youssef", "Ali", "Nour", "Mona"]
)

print("===== Student Grades =====")

print()

print(grades)

print()

print(grades.shape)

print(grades.size)

print(grades.dtype)

print(grades.index)

print(grades.values)

print()

print(grades.head())

print(grades.tail(2))

print()

print(grades.sum())

print(grades.mean())

print(grades.max())

print(grades.min())

print()

print(grades.describe())

print()

print(grades.loc["Sara"])

print(grades.iloc[0])

grades["Ahmed"] = 100

grades["Nour"] = 80

grades["Khaled"] = 91

grades = grades.drop("Omar")

print()

print(grades + 5)

print()

print(grades[grades > 90])

status = np.where(grades >= 60 , "Pass" , "Fail")

print(status)

print()

print("===== Final Report =====")

print(status.size)

print()

high_60 = grades[grades >= 60]

print(high_60.size)

low_60 = grades[grades < 60]

print(low_60.size)

maximum = np.max(grades)

print(maximum)

top_student = grades.idxmax()

print(top_student)

