# Titles & Labels

# plt.title("Average Salary by Department")

# plt.xlabel("Department")
# plt.ylabel("Average Salary ($)")

# Legends & Annotations

# sns.scatterplot(
#     data=df,
#     x="Experience",
#     y="Salary",
#     hue="Department"
# )

# plt.legend(title="Department")

# plt.show()

# plt.annotate(
#     "Highest Salary",
#     xy=(9, 9000),
#     xytext=(6, 9500),
#     arrowprops={"arrowstyle": "->"}
# )

# plt.show()

# Color & Color Palettes

# sns.barplot(
#     data=df,
#     x="Department",
#     y="Salary",
#     hue="Gender",
#     palette="Set2"
# )

# plt.show()


# Sorting & Ordering Data
# department_order = (
#     df.groupby("Department")["Salary"]
#     .mean()
#     .sort_values(ascending=False)
#     .index
# )

# sns.barplot(
#     data=df,
#     x="Department",
#     y="Salary",
#     order=department_order
# )

# plt.show()

# Handling Outliers in visuallizations

# sns.boxplot(
#     data=df,
#     y="Salary"
# )

# plt.show()
