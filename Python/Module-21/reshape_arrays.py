import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

reshaped = numbers.reshape(2, 3)

print(reshaped)
print(reshaped.shape)

number1 = np.array([10, 20, 30, 40, 50, 60, 70, 80])

reshaped = number1.reshape(4, 2)

print(reshaped)

print(reshaped.shape)