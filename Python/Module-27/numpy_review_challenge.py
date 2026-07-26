import numpy as np

grades = np.array([
    [80, 75, 90, 85],
    [60, 70, 65, 75],
    [95, 88, 92, 90]
])

print(np.sum(grades , axis = 1))

print(np.mean(grades , axis = 1))

print(np.max(grades , axis = 0))

new_student = np.array([
    [88, 92, 85, 90]
])

result = np.vstack((grades , new_student))

print(result)

result1 = np.mean(result , axis = 1)

print(result1)

result2 = np.where(result1 >= 70, "Pass", "Fail")

print(result2)

result3 = np.sum(result , axis = 1 , keepdims = True)

print(result3)

normalized = result / result3

print(normalized)

unique_grades, counts = np.unique(
    grades,
    return_counts=True
)

print("Unique Grades:")
print(unique_grades)

print("Counts:")
print(counts)

max_index = np.argmax(grades)
min_index = np.argmin(grades)

print("Max Flat Index:", max_index)
print("Min Flat Index:", min_index)

print("Any grade >= 95:", np.any(grades >= 95))
print("All grades >= 50:", np.all(grades >= 50))
print("All grades >= 70:", np.all(grades >= 70))