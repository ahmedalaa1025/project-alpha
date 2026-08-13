import pandas as pd


employees = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Department": ["IT", "HR", "AI", "Sales"]
}


df = pd.DataFrame(employees)


print("===== Original Data =====")
print(df)

print()


df["Name Lower"] = df["Name"].str.lower()

df["Name Upper"] = df["Name"].str.upper()


print("===== String Operations =====")
print(df)

print()

employees["Department"] = [
    " IT ",
    " HR",
    "AI ",
    " Sales "
]


df_clean = pd.DataFrame(employees)


print("===== Data with Extra Spaces =====")
print(df_clean)

print()


df_clean["Department"] = df_clean["Department"].str.strip()


print("===== After strip() =====")
print(df_clean)

print()


employees_replace = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam"],
    "Department": [
        "Information Technology",
        "Human Resources",
        "Artificial Intelligence",
        "Sales"
    ]
}


df_replace = pd.DataFrame(employees_replace)


print("===== Original Department Names =====")
print(df_replace)

print()


df_replace["Department"] = df_replace["Department"].str.replace(
    "Information Technology",
    "IT"
)


df_replace["Department"] = df_replace["Department"].str.replace(
    "Human Resources",
    "HR"
)


df_replace["Department"] = df_replace["Department"].str.replace(
    "Artificial Intelligence",
    "AI"
)


print("===== After String Replacement =====")
print(df_replace)

print()


employees_contains = {
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
        "IT Support",
        "AI Research"
    ]
}


df_contains = pd.DataFrame(employees_contains)


print("===== Employees =====")
print(df_contains)

print()


print("===== Departments Containing 'IT' =====")
print(
    df_contains[
        df_contains["Department"].str.contains("IT")
    ]
)

print()


print("===== Departments Containing 'AI' =====")
print(
    df_contains[
        df_contains["Department"].str.contains("AI")
    ]
)

print()


print("===== Departments Starting with 'IT' =====")

print(
    df_contains[
        df_contains["Department"].str.startswith("IT")
    ]
)

print()


print("===== Departments Ending with 'Research' =====")

print(
    df_contains[
        df_contains["Department"].str.endswith("Research")
    ]
)

print()


dirty_employees = {
    "Name": [
        " ahmed ",
        "OMAR",
        " Sara ",
        "mariam",
        " ALI "
    ],
    "Department": [
        " it ",
        "HR",
        " artificial intelligence ",
        " IT ",
        "sales"
    ]
}


dirty_df = pd.DataFrame(dirty_employees)


print("===== Dirty Data =====")
print(dirty_df)

print()


dirty_df["Name"] = (
    dirty_df["Name"]
    .str.strip()
    .str.lower()
)


dirty_df["Department"] = (
    dirty_df["Department"]
    .str.strip()
    .str.lower()
)


dirty_df["Department"] = dirty_df["Department"].str.replace(
    "artificial intelligence",
    "ai"
)


dirty_df["Department"] = dirty_df["Department"].str.replace(
    "it",
    "information technology"
)


dirty_df["Department"] = dirty_df["Department"].str.replace(
    "hr",
    "human resources"
)


dirty_df["Department"] = dirty_df["Department"].str.replace(
    "sales",
    "sales department"
)


print("===== Cleaned Data =====")
print(dirty_df)
