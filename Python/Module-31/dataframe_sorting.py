import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali"],
    "Math": [85, 70, 95, 80, 88],
    "Physics": [90, 65, 98, 84, 91],
    "AI": [88, 68, 94, 82, 90]
}

df = pd.DataFrame(students)

print("===== Original =====")
print(df)

print()

# ترتيب حسب Math تصاعديًا
print("===== Sort by Math (Ascending) =====")
print(df.sort_values(by="Math"))

print()

# ترتيب حسب Math تنازليًا
print("===== Sort by Math (Descending) =====")
print(df.sort_values(by="Math", ascending=False))

print()

# ترتيب حسب أكثر من عمود
print("===== Sort by AI ثم Math =====")
print(
    df.sort_values(
        by=["AI", "Math"],
        ascending=[False, True]
    )
)
