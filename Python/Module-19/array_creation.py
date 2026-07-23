import numpy as np

zeros = np.zeros(5)
ones = np.ones(5)
numbers = np.arange(1, 6)

print(zeros)
print(ones)
print(numbers)

numbers = np.array([10, 20, 30, 40, 50])

print(numbers.ndim)
print(numbers.shape)
print(numbers.size)
print(numbers.dtype)

number1 = np.array([1, 2, 3, 4, 5])

print(number1 + 10)

print(number1 * 2)

print(number1 ** 2)

print(number1 - 1)