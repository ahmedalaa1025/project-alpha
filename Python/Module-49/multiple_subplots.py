import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

monthly_sales = [120, 150, 140, 180, 200, 230]

products = ["Laptop", "Phone", "Tablet", "Monitor"]

product_sales = [120, 200, 80, 150]

scores = [
    45, 52, 55, 58, 60,
    62, 65, 67, 68, 70,
    71, 72, 73, 75, 76,
    78, 80, 81, 82, 83,
    84, 85, 86, 88, 90
]

study_hours = [1, 2, 3, 4, 5, 6]

exam_scores = [50, 55, 60, 68, 75, 82]

fig, axes = plt.subplots(2, 2)

# Line Plot
axes[0, 0].plot(
    months,
    monthly_sales,
    marker="o"
)

axes[0, 0].set_title("Monthly Sales")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Sales")

# Bar Chart
axes[0, 1].bar(
    products,
    product_sales
)

axes[0, 1].set_title("Product Sales")
axes[0, 1].set_xlabel("Product")
axes[0, 1].set_ylabel("Sales")

# Histogram
axes[1, 0].hist(
    scores,
    bins=6
)

axes[1, 0].set_title("Student Scores")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Frequency")

# Scatter Plot
axes[1, 1].scatter(
    study_hours,
    exam_scores
)

axes[1, 1].set_title("Study Hours vs Exam Score")
axes[1, 1].set_xlabel("Hours Studied")
axes[1, 1].set_ylabel("Exam Score")

fig.suptitle("Data Visualization Dashboard")

plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.show()
