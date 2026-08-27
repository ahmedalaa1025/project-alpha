import matplotlib.pyplot as plt

categories = [
    "Salaries",
    "Marketing",
    "Operations",
    "Technology",
    "Other"
]

budget = [400, 150, 200, 180, 70]

explode = [0.1, 0, 0, 0, 0]

plt.pie(
    budget,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode
)

plt.title("Company Budget Distribution")

plt.show()
