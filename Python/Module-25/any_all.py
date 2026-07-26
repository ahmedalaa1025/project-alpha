import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(np.any(numbers > 40))
print(np.all(numbers > 0))
print(np.all(numbers > 20))

print(np.any(numbers < 10))
print(np.any(numbers == 30))
print(np.all(numbers >= 10))
print(np.all(numbers < 100))