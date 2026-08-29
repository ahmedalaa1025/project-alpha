import pandas as pd
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

df.plot(
    x="Month",
    y="Sales",
    kind="line",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()

plt.show()

df.plot(
    x="Month",
    y="Profit",
    kind="bar"
)

plt.title("Monthly Profit")

plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()

plt.show()

df.plot(
    x="Month",
    y=["Sales", "Profit"],
    kind="line"
)

plt.title("Monthly Sales and Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid()
plt.legend()

plt.show()
