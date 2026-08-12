import pandas as pd


employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali"],
    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05",
        "2024-02-25"
    ]
}


df = pd.DataFrame(employees)


df["Join Date"] = pd.to_datetime(df["Join Date"])


print("===== Original Data =====")
print(df)

print()


filtered_df = df[df["Join Date"] >= "2024-01-01"]


print("===== Employees Joined in 2024 =====")
print(filtered_df)

print()


sorted_df = df.sort_values(
    by="Join Date",
    ascending=True
)


print("===== Sorted by Join Date =====")
print(sorted_df)
