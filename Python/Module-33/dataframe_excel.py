import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [88, 68, 94]
}

df = pd.DataFrame(students)

df["Total"] = df["Math"] + df["Physics"] + df["AI"]
df["Average"] = (df["Total"] / 3).round(2)

# حفظ الملف كـ Excel
df.to_excel("students_report.xlsx", index=False)

print("Excel File Saved Successfully!")

print()

# قراءة الملف مرة أخرى
new_df = pd.read_excel("students_report.xlsx")

print("===== Excel Data =====")
print(new_df)
