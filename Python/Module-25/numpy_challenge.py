import numpy as np

grades = np.array([
    85, 90, 75, 90, 60,
    95, 80, 90, 70, 85
])

unique_numbers, counts = np.unique(grades , return_counts = True)

print(unique_numbers)
print(counts)

max_index = np.argmax(grades)
min_index = np.argmin(grades)

print(max_index)
print(min_index)
print(grades[max_index])
print(grades[min_index])

print(np.any(grades >= 95))
print(np.all(grades >= 50))
print(np.all(grades >= 70))