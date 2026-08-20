# Question (4)

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

wide_df = df.pivot(
    index="Name",
    columns="Subject",
    values="Score"
)

wide_df["Total"] = wide_df["Math"] + wide_df["Physics"] + wide_df["AI"]

wide_df["Average"] = wide_df["Total"] / 3

pivot_table_df = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Score",
    aggfunc="mean"
)

stats_df = df.pivot_table(
    index="Name",
    columns="Subject",
    values="Score",
    aggfunc=["mean", "max"]
)

long_df = wide_df.reset_index().melt(
    id_vars="Name",
    var_name="Subject",
    value_name="Score"
)

long_df = long_df.sort_values(by=["Name", "Subject"],ascending=[True, True])

long_df = long_df.reset_index(drop=True)

print(long_df)
