import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

numbers[0] = 100
numbers[-1] = 500

print(numbers)

print(numbers[0])
print(numbers[2])
print(numbers[-1])