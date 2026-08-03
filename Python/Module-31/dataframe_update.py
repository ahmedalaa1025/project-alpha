import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Math": [85, 70, 95, 80],
    "Physics": [90, 65, 98, 84],
    "AI": [88, 68, 94, 82]
}

df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

print()

# تعديل قيمة واحدة
df.loc[1, "Math"] = 75

# تعديل عمود بالكامل
df["AI"] = df["AI"] + 5

print("===== Updated Data =====")
print(df)
