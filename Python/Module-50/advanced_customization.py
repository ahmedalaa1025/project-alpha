import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [120, 150, 140, 180, 200, 230]

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    sales,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.ylim(100, 250)

plt.xticks(rotation=45)

plt.grid()

plt.annotate(
    "Peak Sales",
    xy=("Jun", 230),
    xytext=("Apr", 240),
    arrowprops=dict(
        arrowstyle="->"
    )
)

plt.show()
