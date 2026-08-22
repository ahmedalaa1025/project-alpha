import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales = [120, 150, 140, 180, 200, 230]

plt.plot(months, sales, label="Sales")

plt.title("Store Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid()

plt.legend()

plt.show()
