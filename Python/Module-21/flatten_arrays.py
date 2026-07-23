import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

flat = numbers.flatten()

flatt = numbers.ravel()

print(flat)
print(flat.shape)
print(flatt)
print(flatt.shape)

number1 = np.array([
    [10, 20],
    [30, 40]
])

flat_numbers = numbers.flatten()

print(flat_numbers)
print(flat_numbers.shape)