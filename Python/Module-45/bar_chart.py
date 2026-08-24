import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]

employees = [25, 15, 20, 30]

plt.bar(
    departments,
    employees,
    color="blue",
    width=0.6,
    edgecolor="black",
    alpha=0.8
)

plt.title("Employees by Department")

plt.xlabel("Department")

plt.ylabel("Employees")

plt.grid(axis="y")

plt.show()
