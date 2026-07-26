import numpy as np

sales = np.array([
    [120, 150, 180, 200],
    [90, 110, 130, 160],
    [200, 220, 250, 300]
])

print(sales.shape)
print(sales.ndim)
print(sales.size)

print(np.sum(sales, axis = 1))

print(np.mean(sales, axis = 1))

print(np.max(sales))

print(np.argmax(sales))

print(sales[sales > 150])

print(np.where(sales >= 150, "High", "Low"))

last_array = sales + 10

print(last_array)

print(last_array.reshape(4,3))