import numpy as np

array1 = np.array([
    [10, 20],
    [30, 40]
])

array2 = np.array([
    [50, 60],
    [70, 80]
])

result_axis0 = np.concatenate((array1, array2), axis=0)
result_axis1 = np.concatenate((array1, array2), axis=1)

print("Axis 0:")
print(result_axis0)
print(result_axis0.shape)

print("Axis 1:")
print(result_axis1)
print(result_axis1.shape)