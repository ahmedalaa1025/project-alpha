import numpy as np

array1 = np.array([
    [1, 2],
    [3, 4]
])

array2 = np.array([
    [5, 6],
    [7, 8]
])

vertical = np.vstack((array1, array2))
horizontal = np.hstack((array1, array2))

print("Vertical Stack:")
print(vertical)
print(vertical.shape)

print("Horizontal Stack:")
print(horizontal)
print(horizontal.shape)