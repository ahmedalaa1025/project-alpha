import matplotlib.pyplot as plt

labels = ["Laptop", "Phone", "Tablet"]

sales = [200, 500, 300]

explode = [0, 0.1, 0]

plt.pie(
    sales,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode
)

plt.title("Sales Distribution")

plt.show()
