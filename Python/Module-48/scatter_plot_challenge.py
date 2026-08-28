import matplotlib.pyplot as plt

hours = [
    1, 2, 2, 3, 3, 4, 4, 5, 5, 6,
    6, 7, 7, 8, 8, 9, 10
]

scores = [
    45, 50, 53, 58, 62, 65, 68, 72, 75, 78,
    80, 84, 86, 89, 91, 94, 96
]

plt.scatter(
    hours,
    scores,
    color="purple",
    s=100,
    alpha=0.7
)

plt.title("Study Hours vs Exam Score")

plt.xlabel("Hours Studied")

plt.ylabel("Exam Score")

plt.grid()

plt.show()
