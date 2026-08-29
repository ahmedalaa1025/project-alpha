import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar",
    "Apr", "May", "Jun",
    "Jul", "Aug"
]

revenue = [
    100, 120, 115, 145,
    160, 180, 170, 220
]

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    revenue,
    marker="o",
    linewidth=2
)

plt.title("Monthly Revenue")

plt.xlabel("Month")

plt.ylabel("Revenue")

plt.ylim(90, 230)

plt.xticks(rotation=45)

plt.grid()

plt.annotate(
    "Peak Revenue",
    xy=("Aug", 220),
    xytext=("Jun", 240),
    arrowprops=dict(
        arrowstyle="->"
    )
)

plt.show()
