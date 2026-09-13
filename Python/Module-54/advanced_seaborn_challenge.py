import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "IT", "IT", "IT", "IT",
        "HR", "HR", "HR", "HR",
        "Finance", "Finance", "Finance", "Finance"
    ],

    "Gender": [
        "Male", "Female", "Male", "Female",
        "Female", "Male", "Female", "Male",
        "Male", "Female", "Male", "Female"
    ],

    "Experience": [
        2, 4, 6, 8,
        1, 3, 5, 6,
        2, 4, 7, 9
    ],

    "Salary": [
        4500, 5500, 7000, 8500,
        4000, 5000, 6200, 6800,
        4800, 6000, 7500, 9000
    ]
}

df = pd.DataFrame(data)

sns.barplot(
    data=df,
    x="Department",
    y="Salary",
    hue="Gender",
    hue_order=["Male", "Female"],
)

plt.title("Sales Distribution")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()

sns.barplot(
    data=df,
    x="Department",
    y="Salary",
    hue="Gender",
    palette="Set1"
)

plt.title("Average Salary by Department and Gender")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.show()

sns.boxplot(
    data=df,
    x="Department",
    y="Salary"
)

plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.show()

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department"
)

plt.title("Salary vs Experience by Department")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

plt.show()

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Gender"
)

plt.title("Salary vs Experience by Gender")
plt.xlabel("Experience (Years)")
plt.ylabel("Salary")

plt.show()
