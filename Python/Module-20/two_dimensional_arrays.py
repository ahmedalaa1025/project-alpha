# import numpy as np

# numbers = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# print(numbers)
# print(numbers.ndim)
# print(numbers.shape)

import numpy as np

numbers = np.array([
  [10, 20],
  [30, 40],
  [50, 60]
])

numbers[0 , 1] = 200
numbers[2 , 0] = 500

print(numbers)

# print(numbers)
# print(numbers.ndim)
# print(numbers.shape)

# numbers[0 , 1]
# numbers[1 , 1]
# numbers[2 , 0]