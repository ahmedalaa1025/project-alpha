import matplotlib.pyplot as plt

departments = ["Information Technology", "Human Resources", "Finance", "Sales"]

employees = [25, 15, 20, 30]

plt.barh(
    departments,
    employees,
    color="blue",
    edgecolor="black",
    alpha=0.8
)

plt.title("Employees by Department")

plt.xlabel("Employees")

plt.ylabel("Department")

plt.grid(axis="x")

plt.show()
