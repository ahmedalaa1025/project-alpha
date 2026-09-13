import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Jan", "Feb", "Mar"],
    "Sales": [100, 120, 140, 80, 110, 130],
    "Product": [
        "Laptop", "Laptop", "Laptop",
        "Phone", "Phone", "Phone"
    ]
}

df = pd.DataFrame(data)

# sns.lineplot(
#     data=df,
#     x="Month",
#     y="Sales",
#     hue="Product",
#     marker="o",
#     palette="Set2",
#     # order=["Jan", "Feb", "Mar"],
#     hue_order=["Laptop", "Phone"],
#     estimator="median",
#     errorbar="sd"
# )

# plt.title("Sales by Product")

# plt.show()

# sns.barplot(
#     data=df,
#     x="Department",
#     y="Salary",
#     hue="Gender",
#     estimator="median"
# )

# plt.title("Average Salary by Department and Gender")

# plt.xlabel("Department")

# plt.ylabel("Average Salary")

# plt.show()

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Month",
    y="Sales",
    hue="Product"
)

plt.title("Sales Distribution")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()
