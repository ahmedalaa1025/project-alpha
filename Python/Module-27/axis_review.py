import numpy as np

numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Sum axis 0:", np.sum(numbers, axis=0))
print("Sum axis 1:", np.sum(numbers, axis=1))

print("Mean axis 0:", np.mean(numbers, axis=0))
print("Mean axis 1:", np.mean(numbers, axis=1))

print("Max axis 0:", np.max(numbers, axis=0))
print("Max axis 1:", np.max(numbers, axis=1))

print(np.sum(numbers, axis=1))
print(np.sum(numbers, axis=1, keepdims=True))

print(np.mean(numbers, axis=1))
print(np.mean(numbers, axis=1, keepdims=True))

sum_result = np.sum(numbers, axis=1)
sum_keepdims = np.sum(numbers, axis=1, keepdims=True)

print(sum_result)
print(sum_result.shape)

print(sum_keepdims)
print(sum_keepdims.shape)

row_sums = np.sum(numbers, axis=1, keepdims=True)

print(row_sums)

normalized = numbers / row_sums

print(normalized)