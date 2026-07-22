import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers > 25)
# print(numbers[numbers > 25])

numbers = np.array([10, 25, 30, 45, 50, 65, 80])

print(numbers[numbers > 40])
print(numbers[numbers < 50])
print(numbers[numbers == 25])