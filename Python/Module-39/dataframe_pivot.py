import pandas as pd


students = {
    "Name": ["Ahmed", "Ahmed", "Omar", "Omar", "Sara", "Sara"],
    "Subject": ["Math", "Physics", "Math", "Physics", "Math", "Physics"],
    "Score": [85, 90, 70, 65, 95, 98]
}


df = pd.DataFrame(students)


print("===== Long Format =====")
print(df)


pivoted_df = df.pivot(
    index="Name",
    columns="Subject",
    values="Score"
)


print()
print("===== Wide Format =====")
print(pivoted_df)
