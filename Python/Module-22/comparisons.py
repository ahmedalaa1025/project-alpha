import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[numbers > 25])
print(numbers[numbers <= 40])
print(numbers[numbers == 30])
print(numbers[numbers != 20])
