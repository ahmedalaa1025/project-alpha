import matplotlib.pyplot as plt

scores = [
    45, 52, 55, 58, 60,
    62, 65, 67, 68, 70,
    71, 72, 73, 75, 76,
    78, 80, 81, 82, 83,
    84, 85, 86, 88, 90,
    91, 92, 94, 96, 98
]

plt.hist(
    scores,
    bins=6,
    color="green",
    edgecolor="black",
    alpha=0.8
)

plt.title("Student Scores Distribution")

plt.xlabel("Score")

plt.ylabel("Frequency")

plt.grid(axis="y")

plt.show()
  