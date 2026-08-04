import pandas as pd
import numpy as np

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Math": [85, np.nan, 95, 80],
    "Physics": [90, 65, np.nan, 84],
    "AI": [88, 68, 94, np.nan]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

print("===== Missing Values =====")
print(df.isna())

print()

print("===== Non Missing Values =====")
print(df.notna())
