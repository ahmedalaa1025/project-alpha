import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5, 6]

scores = [50, 55, 60, 68, 75, 82]

plt.scatter(
    hours,
    scores,
    color="blue",
    s=100,
    alpha=0.7
)

plt.title("Study Hours vs Exam Score")

plt.xlabel("Hours Studied")

plt.ylabel("Exam Score")

plt.grid()

plt.show()
