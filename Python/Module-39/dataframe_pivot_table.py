import pandas as pd


students = {
    "Name": ["Ahmed", "Ahmed", "Omar", "Omar", "Sara", "Sara"],
    "Subject": ["Math", "Math", "Physics", "Physics", "Math", "Physics"],
    "Score": [80, 90, 70, 60, 95, 98]
}


df = pd.DataFrame(students)


print("===== Original Data =====")
print(df)


pivot_table_df = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Score",
    aggfunc="mean"
)


print()
print("===== Pivot Table =====")
print(pivot_table_df)
