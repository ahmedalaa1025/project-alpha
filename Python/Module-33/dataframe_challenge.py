import pandas as pd
import numpy as np

df = pd.read_csv("students.csv")

print("===== Students Data =====")
print(df)

print()

print(df.shape)

print()

print(df.columns)

df["Total"] = df["Math"] + df["Physics"] + df["AI"]

df["Average"] = (df["Total"] / 3).round(2)

df["Status"] = np.where(df["Average"] >= 85 , "Excellent" , "Good")

df = df.sort_values(by="Average", ascending=False)

df.to_csv("students_report.csv", index=False)

df.to_excel("students_report.xlsx", index=False)

df1 = pd.read_csv("students_report.csv")

print(df1)
