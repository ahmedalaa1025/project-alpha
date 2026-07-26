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

concatenate_axis_0 = np.concatenate((array1, array2), axis=0)
concatenate_axis_1 = np.concatenate((array1, array2), axis=1)

print("Concatenate axis 0:")
print(concatenate_axis_0)

print("Concatenate axis 1:")
print(concatenate_axis_1)