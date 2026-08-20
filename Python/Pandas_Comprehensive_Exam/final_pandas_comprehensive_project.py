# Final Pandas Project

import pandas as pd
import numpy as np

employees = {
    "Employee ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112
    ],

    "Name": [
        " Ahmed ",
        "OMAR",
        " Sara ",
        "Mariam",
        " ALI ",
        "Youssef",
        "Khaled",
        "Nour",
        " Hany ",
        "Mona",
        "Ahmed",
        " Salma "
    ],

    "Department": [
        " IT ",
        "Human Resources",
        "AI Research",
        "IT",
        " sales ",
        "Artificial Intelligence",
        "IT Support",
        "Human Resources",
        "Sales",
        "AI",
        " IT ",
        "HR"
    ],

    "Join Date": [
        "2024-01-15",
        "2023-06-20",
        "2024-03-10",
        "2022-11-05",
        "2024-02-25",
        "2023-09-12",
        "2024-04-18",
        "2022-08-10",
        "2024-01-30",
        "2023-12-05",
        "2024-01-15",
        "2024-05-20"
    ],

    "Salary": [
        15000,
        12000,
        18000,
        14000,
        11000,
        16000,
        13000,
        12500,
        11500,
        17000,
        15000,
        13500
    ]
}

df = pd.DataFrame(employees)

print("===== Original Data =====")

print(df)

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

clean_df["Join Date"] = pd.to_datetime(clean_df["Join Date"])

clean_df["Year"] = clean_df["Join Date"].dt.year

clean_df["Month"] = clean_df["Join Date"].dt.month

clean_df["Day"] = clean_df["Join Date"].dt.day

print(df.duplicated())

clean_df = clean_df.drop_duplicates()

print(clean_df)

clean_df["Day of Week"] = clean_df["Join Date"].dt.dayofweek

employees_2024 = clean_df[clean_df["Year"] == 2024]

print(employees_2024)

year_analysis = clean_df.groupby("Year")['Name'].count().reset_index()

print(year_analysis)

oldest_employee = clean_df.sort_values('Join Date').iloc[0]

print(oldest_employee)

latest_employee = clean_df.sort_values('Join Date').iloc[-1]

print(latest_employee)

clean_df["Annual Salary"] = clean_df["Salary"] * 12

clean_df["Bonus"] = clean_df["Salary"] * 0.10

clean_df["Total Income"] = (
    clean_df["Salary"] + clean_df["Bonus"]
)

clean_df["Salary Category"] = np.where(
    clean_df['Salary'] >= 17000,
    'High',
    np.where(
        clean_df['Salary'] >= 13000,
        'Medium',
        'Low'
    )
)

highest_salary_employee = clean_df.sort_values("Salary", ascending=False).iloc[0]

print(highest_salary_employee)

lowest_salary_employee = clean_df.sort_values("Salary", ascending=True).iloc[0]

print(lowest_salary_employee)

company_average_salary = clean_df["Salary"].mean()

clean_df["Company Average Salary"] = company_average_salary

above_average_df = clean_df[
    clean_df["Salary"] > company_average_salary
]

clean_df = clean_df.sort_values(
    by="Total Income",
    ascending=False
)

clean_df = clean_df.reset_index(drop=True)

print(clean_df)

department_analysis = clean_df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Minimum_Salary=("Salary", "min"),
    Employee_Count=("Name", "count"),
    Total_Salary=("Salary", "sum")
)

print(department_analysis)

clean_df["Department Average Salary"] = (
    clean_df.groupby("Department")["Salary"]
      .transform("mean")
)

clean_df["Salary Difference"] = (
    clean_df["Salary"] - clean_df["Department Average Salary"]
)

clean_df["Salary Rank"] = clean_df["Salary"].rank(ascending=False, method="dense")

clean_df["Department Rank"] = (
    clean_df.groupby("Department")["Salary"]
      .rank(
          ascending=False,
          method="dense"
      )
)

print(clean_df[clean_df["Department Rank"] == 1])

print(clean_df)

high_income_df = clean_df[
    (clean_df["Total Income"] >= 15000) &
    (clean_df["Department"].isin(["it", "ai"]))
]

print(high_income_df)

clean_df["Performance"] = np.where(
    clean_df["Salary Difference"] > 0,
    "Above Department Average",
    np.where(
        clean_df["Salary Difference"] == 0,
        "At Department Average",
        "Below Department Average"
    )
)

top_performers_df = clean_df[(clean_df["Performance"] == "Above Department Average") & (clean_df["Department Rank"] == 1)]

print(top_performers_df)

department_summary = clean_df.groupby("Department").agg(
    Average_Salary=("Salary", "mean"),
    Maximum_Salary=("Salary", "max"),
    Average_Total_Income=("Total Income", "mean"),
    Employee_Count=("Name", "count"),
)

print(department_summary)

highest_paid_department = department_summary["Average_Salary"].idxmax()

top_performers_df = top_performers_df.sort_values(
    by="Total Income",
    ascending=False
)

top_performers_df = top_performers_df.reset_index(drop=True)

print(top_performers_df)

department_report = clean_df.pivot_table(
    index='Department',
    values=['Salary', 'Total Income', 'Employee ID'],
    aggfunc={
        'Salary': ['mean', 'max', 'min'],
        'Total Income': 'mean',
        'Employee ID': 'count'
    }
)

department_report.columns = [
    'Average Salary',
    'Maximum Salary', 
    'Minimum Salary',
    'Average Total Income',
    'Employee Count'
]

department_report = department_report[[
    'Average Salary',
    'Maximum Salary',
    'Minimum Salary', 
    'Average Total Income',
    'Employee Count'
]]

print(department_report)

salary_category_report = clean_df.pivot_table(
    index='Salary Category',
    values=['Salary', 'Total Income', 'Employee ID'],
    aggfunc={
        'Salary': 'mean',
        'Total Income': 'mean',
        'Employee ID': 'count'
    }
)

print(salary_category_report)

department_category_report = clean_df.pivot_table(
    index="Department",
    columns="Salary Category",
    values="Salary",
    aggfunc="mean"
)

print(department_category_report)

wide_df = clean_df.pivot_table(
    index="Department",
    columns="Salary Category",
    values="Salary",
    aggfunc="mean"
)

print(wide_df)

long_df = wide_df.reset_index().melt(
    id_vars="Department",
    var_name="Salary Category",
    value_name="Salary"
)

print(long_df)

final_report = clean_df[[
    'Employee ID',
    'Name',
    'Department',
    'Salary',
    'Annual Salary',
    'Bonus',
    'Total Income',
    'Salary Category',
    'Company Average Salary',
    'Department Average Salary',
    'Salary Difference',
    'Department Rank',
    'Performance'
]]

final_report = final_report.sort_values("Total Income", ascending=False)

final_report = final_report.reset_index(drop=True)

department_top_employees = final_report[final_report["Department Rank"] == 1]

final_report = department_top_employees.sort_values("Total Income", ascending=False)

final_Department_salary = final_report.pivot_table(
    index='Department',
    values=['Salary', 'Total Income', 'Employee ID'],
    aggfunc={
        'Salary': ['mean', 'max', 'sum'],
        'Total Income': 'mean',
        'Employee ID': 'count'
    }
)

final_report["Salary Difference From Company Average"] = final_report["Company Average Salary"] - final_report["Department Average Salary"]

print(final_report)
