import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60])

parts = np.split(numbers, 3)

print(parts)

for part in parts:
    print(part)

unequal_parts = np.array_split(numbers, 4)

print(unequal_parts)

for part in unequal_parts:
    print(part)    

matrix = np.array([
    [10, 20],
    [30, 40],
    [50, 60],
    [70, 80]
])

parts_axis_0 = np.split(matrix, 2, axis=0)
parts_axis_1 = np.split(matrix, 2, axis=1)

print("Axis 0:")
for part in parts_axis_0:
    print(part)
    print(part.shape)

print("Axis 1:")
for part in parts_axis_1:
    print(part)
    print(part.shape)    