import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [120, 150, 140, 180, 200, 230]

plt.plot(
    months,
    sales,
    marker="o",
    linestyle="--",
    markersize=8,
    linewidth=3,
    color="blue",
    markerfacecolor="white",
    markeredgecolor="blue"
)

plt.title("Store Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.show()
