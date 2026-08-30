import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": [
        "Jan", "Feb", "Mar",
        "Jan", "Feb", "Mar"
    ],

    "Sales": [
        100, 120, 140,
        80, 110, 130
    ],

    "Product": [
        "Laptop",
        "Laptop",
        "Laptop",
        "Phone",
        "Phone",
        "Phone"
    ]
}

df = pd.DataFrame(data)

sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    hue="Product",
    marker="o"
)

plt.title("Sales by Product")

plt.show()
