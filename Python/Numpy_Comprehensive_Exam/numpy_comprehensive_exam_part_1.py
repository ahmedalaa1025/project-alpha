# Question (1)

import numpy as np

sales = np.array([
    [1200, 1500, 1800],
    [2000, 2200, 2500],
    [2700, 3000, 3200],
    [3500, 3800, 4000]
])

print("===== Sales Report =====")

print()

print("Shape:" , sales.shape)

print("Size:" , sales.size)

print("Dimensions:" , sales.ndim)

print()

total_monthly_sales = np.sum(sales , axis = 0)

total_branch_sales = np.sum(sales , axis = 1)

print("Monthly Sales:" , total_monthly_sales)

print("Branch Sales:" , total_branch_sales)

print()

average_branch_sales = np.mean(sales , axis = 1)

print("Branch Average:" , average_branch_sales)

print()

maximum_sale_number = np.max(sales)

print("Maximum Sale:" , maximum_sale_number)

print()

max_sale_index = np.argmax(sales)

print("Max Index:" , max_sale_index)

print()

print("Sales > 2500:" , sales[sales > 2500])

print()

print("Updated Sales:" , sales + 500)

print()

reshaped = np.reshape(sales , (3 , 4))

print("Reshaped:" , reshaped)
 