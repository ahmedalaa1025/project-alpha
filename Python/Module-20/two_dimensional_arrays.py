import numpy as np

numbers = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(numbers)
print(numbers.ndim)
print(numbers.shape)

number1 = np.array([
  [10, 20],
  [30, 40],
  [50, 60]
])

number1[0 , 1] = 200
number1[2 , 0] = 500

print(number1)

print(number1)
print(number1.ndim)
print(number1.shape)

number1[0 , 1]
number1[1 , 1]
number1[2 , 0]