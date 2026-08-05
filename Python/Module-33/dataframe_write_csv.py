import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [88, 68, 94]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

df["Total"] = df["Math"] + df["Physics"] + df["AI"]

df["Average"] = df["Total"] / 3

df.to_csv("students_report.csv", index=False)

print("File Saved Successfully!")
