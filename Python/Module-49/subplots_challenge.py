import matplotlib.pyplot as plt

months = [
    "Jan", "Feb", "Mar",
    "Apr", "May", "Jun"
]

revenue = [
    100, 120, 115,
    145, 160, 180
]

departments = [
    "HR",
    "Marketing",
    "IT",
    "Operations"
]

expenses = [
    80, 120, 150, 100
]

salaries = [
    5000, 5500, 6000, 6200,
    6500, 6800, 7000, 7200,
    7500, 7800, 8000, 8500,
    9000, 9500, 10000
]

experience = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15
]

salary = [
    3500, 3800, 4200, 4500, 5000,
    5400, 5700, 6200, 6600, 7000,
    7500, 8000, 8500, 9000, 9500
]

fig, axes = plt.subplots(2, 2)

axes[0, 0].plot(
    months,
    revenue,
    marker="o"
)

axes[0, 0].set_title("Monthly Revenue")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue")

axes[0, 1].bar(
    departments,
    expenses
)

axes[0, 1].set_title("Departmenta Expenses")
axes[0, 1].set_xlabel("Department")
axes[0, 1].set_ylabel("Expenses")

axes[1, 0].hist(
    salaries,
    bins=6
)

axes[1, 0].set_title("Employee Salary Distribution")
axes[1, 0].set_xlabel("Salary")
axes[1, 0].set_ylabel("Frequency")

axes[1, 1].scatter(
    experience,
    salary
)
axes[1, 1].set_title("Experience vs Salary")
axes[1, 1].set_xlabel("Experience")
axes[1, 1].set_ylabel("Salary")

fig.suptitle("Company Dashboard")

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.show()
