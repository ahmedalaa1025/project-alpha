import numpy as np

numbers = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

parts = np.split(numbers, 2, axis=0)

print(parts)

print("Part 1:")
print(parts[0])

print("Part 2:")
print(parts[1])

column_parts = np.split(numbers, 2, axis=1)

print("Column Part 1:")
print(column_parts[0])

print("Column Part 2:")
print(column_parts[1])