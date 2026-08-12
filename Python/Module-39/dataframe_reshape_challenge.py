import pandas as pd


students = {
    "Name": [
        "Ahmed", "Ahmed", "Ahmed",
        "Omar", "Omar", "Omar",
        "Sara", "Sara", "Sara",
        "Mariam", "Mariam", "Mariam"
    ],
    "Subject": [
        "Math", "Physics", "AI",
        "Math", "Physics", "AI",
        "Math", "Physics", "AI",
        "Math", "Physics", "AI"
    ],
    "Score": [
        85, 90, 88,
        70, 65, 68,
        95, 98, 94,
        80, 84, 82
    ]
}


df = pd.DataFrame(students)

print("===== Original Data =====")
print(df)

pivoted_df = df.pivot(
    index="Name",
    columns="Subject",
    values="Score"
)


print()
print("===== Wide Format =====")
print(pivoted_df)

pivoted_df["Total"] = pivoted_df["Math"] + pivoted_df["Physics"] + pivoted_df["AI"]

pivoted_df["Average"] = pivoted_df["Total"] / 3

pivot_table_df = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Score",
    aggfunc="mean"
)


print()
print("===== Pivot Table =====")
print(pivot_table_df)

melted_df = df.pivot(
    index="Name",
    columns="Subject",
    values="Score"
).reset_index().melt(
    id_vars="Name",
    var_name="Subject",
    value_name="Score"
)


print()
print("===== Long Format =====")
print(melted_df)

pivot_table_df_mean_max = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Score",
    aggfunc=["mean", "max"]
)


print()
print("===== Pivot Table =====")
print(pivot_table_df_mean_max)
