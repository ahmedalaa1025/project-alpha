import pandas as pd

print("Pandas Imported Successfully!")

print(pd.__version__)

import pandas as pd
import numpy as np

grades = pd.Series([85, 90, 78, 95])

print(grades)

numbers = [10, 20, 30, 40]

series = pd.Series(numbers)

print(series)

array = np.array([100, 200, 300])

series_1 = pd.Series(array)

print(series_1)

student = {
    "Math":85,
    "Physics":90,
    "AI":95
}

series_2 = pd.Series(student)

print(series_2)

grades_1 = pd.Series(
    [85,90,78],
    index=["Ahmed","Omar","Sara"]
)

print(grades_1)

# print(grades_1[0])

print(grades_1["Ahmed"])

series_3 = pd.Series([1.5,2.8,3.9])

print(series_3)

series_4 = pd.Series([True, False, True])

print(series_4)

series_5 = pd.Series([
    "Python",
    "NumPy",
    "Pandas"
])

print(series_5)
