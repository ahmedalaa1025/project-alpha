import numpy as np

sales = np.array([
    1200, 1500, 1800,
    2000, 2200, 2500,
    2700, 3000, 3200,
    3500, 3800, 4000
])

result0 = np.split(sales, 4)
print(result0[0])
print(result0[1])
print(result0[2])
print(result0[3])

result1 = np.sum(result0, axis = 1)
print(result1)

result2 = np.mean(result0, axis = 1)
print(result2)

result3 = np.array_split(sales, 5)
print(result3)

for part in result3:
  print(part)
  print(part.shape)