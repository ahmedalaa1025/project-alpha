import numpy as np

numbers2 = np.array([10, 20, 30, 40, 50])

print(numbers2 + 5)
print(numbers2 * 2)

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