import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

result1 = np.sum(numbers, axis=1)
result2 = np.sum(numbers, axis=1, keepdims=True)

result3 = np.mean(numbers, axis=0, keepdims=True)

print(result1)
print(result1.shape)

print(result2)
print(result2.shape)

print(result3)
print(result3.shape)