import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug"
    ],

    "Sales": [
        120, 150, 140, 180,
        200, 230, 210, 260
    ],

    "Profit": [
        20, 30, 25, 40,
        50, 60, 55, 70
    ],

    "Department": [
        "IT", "HR", "Finance", "IT",
        "HR", "Finance", "IT", "HR"
    ],

    "Experience": [
        2, 3, 4, 5,
        6, 7, 8, 9
    ],

    "Salary": [
        4500, 5000, 5500, 6500,
        7000, 7500, 8500, 9000
    ]
}

df = pd.DataFrame(data)

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

department_order = (
    df.groupby("Department")["Salary"]
    .mean()
    .sort_values(ascending=False)
    .index
)

sns.barplot(
    data=df,
    x="Department",
    y="Salary",
    order=department_order
)

plt.show()

plt.hist(
    df["Salary"],
    bins=5
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department"
)

plt.annotate(
    "Highest Salary",
    xy=(9, 9000),
    xytext=(6, 9500),
    arrowprops={"arrowstyle": "->"}
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

sns.boxplot(
    data=df,
    x="Department",
    y="Salary"
)

plt.title("Salary Distribution by Department")

plt.show()
