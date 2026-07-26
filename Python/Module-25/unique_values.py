import numpy as np

numbers = np.array([10, 20, 10, 30, 20, 40, 10, 50])

unique_numbers, counts = np.unique(
    numbers,
    return_counts=True
)

print(unique_numbers)
print(counts)