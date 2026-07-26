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

numbers2 = np.array([10, 20, 30, 40, 50])

print(numbers + 5)
print(numbers * 2)

print(np.sum(numbers2))
print(np.mean(numbers2))
print(np.max(numbers2))
print(np.min(numbers2))

print(numbers2[numbers2 > 25])
print(np.where(numbers2 >= 30, "Pass", "Fail"))

numbers3 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([1, 2, 3])

print(numbers3 + 10)
print(numbers3 + values)

numbers4 = np.arange(1, 13)

print(numbers4)

reshaped = numbers4.reshape(3, 4)

print(reshaped)
print(reshaped.shape)

flat = reshaped.flatten()
raveled = reshaped.ravel()

print(flat)
print(raveled)