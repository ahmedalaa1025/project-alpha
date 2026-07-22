import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

print(numbers[3])

numbers[1] = 200

print(numbers[2:5])

print(np.sum(numbers))

print(np.mean(numbers))

print(numbers[numbers > 40])

print(numbers)