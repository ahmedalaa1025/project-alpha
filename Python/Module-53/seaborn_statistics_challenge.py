import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "IT", "IT", "IT",
        "HR", "HR", "HR",
        "Finance", "Finance", "Finance",
        "IT", "HR", "Finance"
    ],

    "Experience": [
        2, 4, 6,
        1, 3, 5,
        2, 4, 7,
        8, 6, 9
    ],

    "Salary": [
        4500, 5500, 7000,
        4000, 5000, 6200,
        4800, 6000, 7500,
        8500, 6800, 9000
    ]
}

df = pd.DataFrame(data)

sns.countplot(
    data=df,
    x="Department"
)

plt.title("Employees by Department")

plt.show()

sns.boxplot(
    data=df,
    x="Department",
    y="Salary"
)

plt.title("Salary Distribution by Department")

plt.show()

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department"
)

plt.title("Salary vs Experience by Department")

plt.show()

sns.regplot(
    data=df,
    x="Experience",
    y="Salary"
)

plt.title("Experience vs Salary Regression")

plt.show()

correlation = df[
    ["Experience", "Salary"]
].corr()

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()
