import matplotlib.pyplot as plt

ages = [18, 19, 20, 21, 22, 22, 23, 24, 25, 25, 26, 27, 28]

plt.hist(
    ages,
    bins=5,
    color="blue",
    edgecolor="black",
    alpha=0.8
)

plt.title("Age Distribution")

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.grid(axis="y")

plt.show()
