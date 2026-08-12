import pandas as pd


students = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98],
    "AI": [88, 68, 94]
}


df = pd.DataFrame(students)


print("===== Wide Format =====")
print(df)


melted_df = df.melt(
    id_vars="Name",
    var_name="Subject",
    value_name="Score"
)


print()
print("===== Long Format =====")
print(melted_df)
