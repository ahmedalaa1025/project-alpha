import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(numbers)
print(numbers.ndim)
print(numbers.shape)
print(numbers.size)

zeros = np.zeros(5)
ones = np.ones(5)

range_numbers = np.arange(1, 11, 2)

line_numbers = np.linspace(0, 1, 5)

random_numbers = np.random.randint(1, 51, 5)

print(zeros)
print(ones)
print(range_numbers)
print(line_numbers)
print(random_numbers)

numbers1 = np.array([10, 20, 30, 40, 50, 60])

print(numbers1[0])
print(numbers1[3])
print(numbers1[-1])

print(numbers1[1:4])
print(numbers1[:3])
print(numbers1[3:])

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(matrix[0, 1])
print(matrix[2, 0])

print(matrix[0, :])
print(matrix[:, 1])

print(matrix[0:2, 1:3])