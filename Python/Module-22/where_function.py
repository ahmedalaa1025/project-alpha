import numpy as np

numbers = np.array([10, 25, 40, 55, 70])

result = np.where(numbers >= 50, "High", "Low")

result1 = np.where(numbers % 2 == 0, 1, 0)

print(result)
print(result1)