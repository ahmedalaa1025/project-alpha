import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

branch_a = [120, 150, 140, 180, 200, 230]
branch_b = [100, 130, 160, 170, 190, 210]

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    branch_a,
    marker="o",
    linewidth=2,
    label="Branch A"
)

plt.plot(
    months,
    branch_b,
    marker="s",
    linewidth=2,
    label="Branch B"
)

plt.title("Branch Sales Comparison")

plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid()

plt.show()
