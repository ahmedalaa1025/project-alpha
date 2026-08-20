# Question (5)

import pandas as pd

employees = {
    "Name": [
        " Ahmed ",
        "OMAR",
        " Sara ",
        "Mariam",
        " ALI ",
        "Youssef",
        "Ahmed"
    ],

    "Department": [
        " IT ",
        "Human Resources",
        "AI Research",
        " sales ",
        "IT Support",
        "Artificial Intelligence",
        " IT "
    ],

    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05",
        "2024-02-25",
        "2023-09-12",
        "2024-01-15"
    ],

    "Salary": [
        15000,
        12000,
        18000,
        11000,
        14000,
        16000,
        15000
    ]
}

df = pd.DataFrame(employees)

clean_df = df.copy()

clean_df["Name"] = clean_df["Name"].str.lower()

clean_df["Name"] = clean_df["Name"].str.strip()

clean_df["Department"] = clean_df["Department"].str.lower()

clean_df["Department"] = clean_df["Department"].str.strip()

clean_df["Department"] = clean_df["Department"].str.replace(
    "human resources",
    "hr"
)

clean_df["Department"] = clean_df["Department"].str.replace(
    "artificial intelligence",
    "ai"
)

clean_df["Department"] = clean_df["Department"].str.replace(
    "it support",
    "it"
)

clean_df["Department"] = clean_df["Department"].str.replace(
    "sales",
    "sales department"
)

clean_df["Department"] = clean_df["Department"].str.replace(
    "ai research",
    "ai"
)

clean_df = clean_df.drop_duplicates()

clean_df["Join Date"] = pd.to_datetime(clean_df["Join Date"])

clean_df["Year"] = clean_df["Join Date"].dt.year

clean_df["Month"] = clean_df["Join Date"].dt.month

clean_df["Day"] = clean_df["Join Date"].dt.day

clean_df = clean_df[clean_df["Year"] == 2024]

clean_df = clean_df[clean_df["Department"].isin(["it", "ai"])]

clean_df["Annual Salary"] = clean_df["Salary"] * 12

clean_df["Department Average Salary"] = (
    clean_df.groupby("Department")["Salary"]
      .transform("mean")
)

clean_df["Salary Difference"] = (
    clean_df["Salary"] - clean_df["Department Average Salary"]
)

clean_df["Department Rank"] = (
    clean_df.groupby("Department")["Salary"]
      .rank(
          ascending=False,
          method="dense"
      )
)

clean_df["Bonus"] = clean_df["Salary"] * 0.10

clean_df["Total Income"] = (
    clean_df["Salary"] + clean_df["Bonus"]
)

clean_df = clean_df[
    clean_df["Total Income"] >= 15000
]

clean_df = clean_df.sort_values(
    by="Total Income",
    ascending=False
)

clean_df = clean_df.reset_index(drop=True)

print(clean_df)
