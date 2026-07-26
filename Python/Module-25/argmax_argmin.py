import numpy as np

numbers = np.array([45, 10, 80, 25, 60, 5])

max_index = np.argmax(numbers)
min_index = np.argmin(numbers)

print(max_index)
print(min_index)

print(numbers[max_index])
print(numbers[min_index])