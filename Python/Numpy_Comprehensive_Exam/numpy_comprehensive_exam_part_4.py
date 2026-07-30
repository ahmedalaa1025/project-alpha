# Question (4)

import numpy as np

sales = np.array([
    [1200, 1500, 1700],
    [1400, 1600, 1800],
    [1100, 1550, 1750],
    [1800, 1900, 2100],
    [2000, 2200, 2400]
])

print("===== Store Sales Report =====")

print()

print("Shape:" , sales.shape)

print("Size:" , sales.size)

print("Dimensions:" , sales.ndim)

print()

sales_per_day = np.sum(sales , axis = 1)

print("Total Sales Per Day:" , sales_per_day)

print()

sales_per_department = np.sum(sales , axis = 0)

print("Total Sales Per Department:" , sales_per_department)

print()

average_sales_per_department = np.mean(sales , axis = 0)

print("Department Average:" , average_sales_per_department)

print()

higher_sales = np.max(sales)

print("Maximum Sale:" , higher_sales)

print()

higher_index = np.argmax(sales)

print("Argmax:" , higher_index)

print()

sales_higher_1800 = sales[sales > 1800]

print("Sales > 1800:" , sales_higher_1800)

print()

new_day = np.array([[2100, 2300, 2500]])

updated_sales = np.vstack((sales , new_day))

print("Updated Sales:" , updated_sales)

print()

daily_average = np.mean(updated_sales , axis = 1)

print("Daily Average:" , daily_average)

print()

unique_numbers , counts = np.unique(updated_sales , return_counts = True)

print("Unique Values:" , unique_numbers)

print()

print("Counts:" , counts)

print()

print("Any == 2500:" , np.any(updated_sales == 2500))

print()

print("All >= 1000:" , np.all(updated_sales >= 1000))

print()

reshaped = np.reshape(updated_sales , (3 , 6))

print("Reshaped:" , reshaped)
