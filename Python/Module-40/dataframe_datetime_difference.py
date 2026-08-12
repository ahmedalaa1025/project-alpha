import pandas as pd


employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05"
    ]
}


df = pd.DataFrame(employees)


df["Join Date"] = pd.to_datetime(df["Join Date"])


reference_date = pd.Timestamp("2026-01-01")


df["Days Since Joining"] = (
    reference_date - df["Join Date"]
).dt.days


print("===== Employees Data =====")
print(df)
