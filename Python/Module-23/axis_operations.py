import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Sum axis 0:", np.sum(numbers, axis=0))
print("Sum axis 1:", np.sum(numbers, axis=1))

print("Mean axis 0:", np.mean(numbers, axis=0))
print("Mean axis 1:", np.mean(numbers, axis=1))

print("Max axis 0:", np.max(numbers, axis=0))
print("Max axis 1:", np.max(numbers, axis=1))

print("Min axis 0:", np.min(numbers, axis=0))
print("Min axis 1:", np.min(numbers, axis=1))