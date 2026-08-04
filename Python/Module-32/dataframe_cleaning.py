import pandas as pd
import numpy as np

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Youssef"],
    "Math": [85, np.nan, 95, 80, 75],
    "Physics": [90, 65, np.nan, 84, 88],
    "AI": [88, 68, 94, np.nan, 90]
}

df = pd.DataFrame(students)

print("===== Original =====")
print(df)

print()

# تعويض القيم المفقودة بمتوسط كل عمود
df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Physics"] = df["Physics"].fillna(df["Physics"].mean())
df["AI"] = df["AI"].fillna(df["AI"].mean())

# إنشاء أعمدة جديدة
df["Total"] = df["Math"] + df["Physics"] + df["AI"]
df["Average"] = df["Total"] / 3

# تحديد الحالة
df["Status"] = np.where(df["Average"] >= 80, "Pass", "Fail")

# ترتيب حسب المتوسط
df = df.sort_values(by="Average", ascending=False)

# إعادة ترقيم الـ Index
df = df.reset_index(drop=True)

print("===== Cleaned Data =====")
print(df)
