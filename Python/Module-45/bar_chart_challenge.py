import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]

sales = [120, 200, 80, 150, 100]

plt.bar(
    products,
    sales,
    color="green",
    width=0.6,
    edgecolor="black",
    alpha=0.8
)

plt.title("Product Sales")

plt.xlabel("Product")

plt.ylabel("Sales")

plt.grid(axis="y")

plt.show()
