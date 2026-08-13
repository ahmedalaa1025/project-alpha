import pandas as pd

employees = {
    "Name": [
        " Ahmed ",
        "OMAR",
        " Sara ",
        "Mariam",
        " ALI ",
        "Youssef"
    ],
    "Department": [
        " IT ",
        "Human Resources",
        "AI Research",
        " sales ",
        "IT Support",
        "Artificial Intelligence"
    ]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")
print(df)

print()

df["Name"] = (
    df["Name"]
    .str.strip()
    .str.lower()
)

df["Department"] = (
    df["Department"]
    .str.strip()
    .str.lower()
)

df["Department"] = df["Department"].str.replace(
    "artificial intelligence",
    "ai"
)

df["Department"] = df["Department"].str.replace(
    "it",
    "information technology"
)

df["Department"] = df["Department"].str.replace(
    "human resources"
    "hr",
)

df["Department"] = df["Department"].str.replace(
    "sales",
    "sales department"
)

df["Department"] = df["Department"].str.replace(
    "ai research",
    "ai"
)

df["Department"] = df["Department"].str.replace(
    "it support",
    "information technology support"
)

print(
    df[
        df["Department"].str.contains("information")
    ]
)

print(
    df[
        df["Department"].str.startswith("ai")
    ]
)

print()

print(
    df[
        df["Department"].str.endswith("department")
    ]
)

print(df)
