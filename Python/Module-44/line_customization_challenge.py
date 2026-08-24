import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

online_sales = [100, 130, 125, 160, 190, 220]

physical_sales = [150, 160, 155, 170, 180, 200]

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    online_sales,
    marker="o",
    linestyle="--",
    markersize=8,
    linewidth=2,
    color="blue",
    label="Online Store"
)

plt.plot(
    months,
    physical_sales,
    marker="s",
    linestyle="-",
    markersize=8,
    linewidth=2,
    color="red",
    label="Physical Store"
)

plt.title("Store Sales Comparison")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.legend()

plt.grid()

plt.show()
