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
    ],

    "Age": [
        22, 25, 28, 31,
        21, 24, 27, 29,
        23, 26, 30, 32
    ]
}

df = pd.DataFrame(data)

g = sns.FacetGrid(
    df,
    col="Department",
    # row = "Gender"
    col_wrap=2
)

g.map_dataframe(
    sns.scatterplot,
    x="Experience",
    y="Salary"
)

plt.show()

sns.lmplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Gender"
)

plt.show()

sns.pairplot(
    df[["Experience", "Salary", "Age", "Gender"]],
    hue="Gender"
)

plt.show()

sns.jointplot(
    data=df,
    x="Experience",
    y="Salary",
    kind="reg"
)

plt.show()
