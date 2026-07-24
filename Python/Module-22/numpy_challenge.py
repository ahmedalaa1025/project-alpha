import numpy as np

numbers = np.array([15, 40, 25, 60, 10, 75, 30])

increased = numbers + 5

filter = increased[increased > 40]

result = np.where(numbers >= 50, "Pass", "Fail")

result1 = np.sort(numbers)

print(numbers)
print(increased)
print(filter)
print(result)
print(result1)