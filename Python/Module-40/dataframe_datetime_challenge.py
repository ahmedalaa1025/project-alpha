import pandas as pd


employees = {
    "Name": [
        "Ahmed",
        "Omar",
        "Sara",
        "Mariam",
        "Ali",
        "Youssef"
    ],
    "Department": [
        "IT",
        "HR",
        "AI",
        "Sales",
        "IT",
        "AI"
    ],
    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05",
        "2024-02-25",
        "2023-09-12"
    ]
}


df = pd.DataFrame(employees)

df["Join Date"] = pd.to_datetime(df["Join Date"])

df["Year"] = df["Join Date"].dt.year

df["Month"] = df["Join Date"].dt.month

df["Day"] = df["Join Date"].dt.day

df["Day of Week"] = df["Join Date"].dt.dayofweek

filtered_df = df[df["Join Date"] >= "2024-01-01"]


print("===== Employees Joined in 2024 =====")
print(filtered_df)

print()


sorted_df = df.sort_values(
    by="Join Date",
    ascending=False
)


print("===== Sorted by Join Date =====")
print(sorted_df)

reference_date = pd.Timestamp("2026-01-01")


df["Days Since Joining"] = (
    reference_date - df["Join Date"]
).dt.days


print("===== Employees Data =====")
print(df)

oldest_employee = df.sort_values('Join Date').iloc[0]

print(oldest_employee)
