import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": [
        "Jan", "Feb", "Mar",
        "Apr", "May", "Jun"
    ],

    "Sales": [
        120, 150, 140,
        180, 200, 230
    ],

    "Profit": [
        20, 30, 25,
        40, 50, 60
    ]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()

sns.barplot(
    data=df,
    x="Month",
    y="Profit",
)

plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()

plt.show()

experience_data = {
    "Experience": [
        1, 2, 3, 4,
        5, 6, 7, 8
    ],

    "Salary": [
        3500, 4000, 4500, 5000,
        5500, 6200, 7000, 8000
    ]
}

experience_df = pd.DataFrame(experience_data)

sns.scatterplot(
    data=experience_df,
    x="Experience",
    y="Salary"
)

plt.title("Experience vs Salary")

plt.grid()

plt.show()

sns.histplot(
    data=experience_df,
    x="Salary",
    bins=5
)

plt.title("Salary Distribution")

plt.grid()

plt.show()
