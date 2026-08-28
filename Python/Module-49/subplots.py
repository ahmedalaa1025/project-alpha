import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(
    [1, 2, 3, 4],
    [10, 20, 15, 25]
)

axes[0, 0].set_title("Line Plot")

axes[0, 1].bar(
    ["A", "B", "C"],
    [10, 20, 15]
)

axes[0, 1].set_title("Bar Chart")

axes[1, 0].hist(
    [10, 12, 12, 15, 16, 18, 20],
    bins=4
)

axes[1, 0].set_title("Histogram")

axes[1, 1].scatter(
    [1, 2, 3, 4],
    [10, 15, 12, 20]
)

axes[1, 1].set_title("Scatter Plot")

fig.suptitle("Company Sales Dashboard")

plt.show()
