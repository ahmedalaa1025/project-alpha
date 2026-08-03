import pandas as pd

students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [88, 68, 94]
}

df = pd.DataFrame(students)

print("===== Original =====")
print(df)

print()

# تغيير أسماء الأعمدة
df = df.rename(
    columns={
        "Math": "Mathematics",
        "Physics": "Physics Score",
        "AI": "Artificial Intelligence"
    }
)

print("===== Renamed Columns =====")
print(df)

print()

# تغيير أسماء الـ Index
df = df.rename(
    index={
        0: "Student A",
        1: "Student B",
        2: "Student C"
    }
)

print("===== Renamed Index =====")
print(df)
