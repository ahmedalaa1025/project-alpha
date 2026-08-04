import pandas as pd
import numpy as np

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Math": [85, np.nan, 95, 80],
    "Physics": [90, 65, np.nan, 84],
    "AI": [88, 68, 94, np.nan]
}

df = pd.DataFrame(students)

print("===== Original =====")
print(df)

print()

# التعويض بقيمة ثابتة
fixed_fill = df.fillna(0)

print("===== Fill with 0 =====")
print(fixed_fill)

print()

# التعويض بمتوسط كل عمود رقمي
mean_fill = df.copy()

mean_fill["Math"] = mean_fill["Math"].fillna(mean_fill["Math"].mean())
mean_fill["Physics"] = mean_fill["Physics"].fillna(mean_fill["Physics"].mean())
mean_fill["AI"] = mean_fill["AI"].fillna(mean_fill["AI"].mean())

print("===== Fill with Mean =====")
print(mean_fill)
