import numpy as np

numbers = np.arange(1, 13)
print(numbers)

reshaped = numbers.reshape(3, 4)
print(reshaped)

print(reshaped[1, 2])

flat = reshaped.flatten()
print(flat)

number1 = np.linspace(0, 100, 5)
print(number1)

number2 = np.random.randint(1, 51, (4, 3))
print(number2)