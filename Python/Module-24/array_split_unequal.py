import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

parts = np.array_split(numbers, 3)

print(parts)

print(parts[0])
print(parts[1])
print(parts[2])