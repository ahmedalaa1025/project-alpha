# Question (4)

products = [
    ["Laptop", 25000, 5],
    ["Mouse", 500, 20],
    ["Keyboard", 1200, 10],
    ["Monitor", 7000, 3]
]

print("===== Product Inventory Report =====")

print()

for i in range(len(products)):
  print("Product:" , products[i][0])
  print("Price:" , products[i][1])
  print("Quantity:" , products[i][2])
  print("Inventory Value:" , products[i][1] * products[i][2])
  print()

print()

print("===== Inventory Statistics =====")

print()

total = 0

for i in range(len(products)):
  total += products[i][1] * products[i][2]

print("Total Inventory Value:" , total)

print()

maximum_inventory_value = products[0][1] * products[0][2]
maximum_inventory_product_value = products[0][0]

for product in products:
  value = product[1] * product[2]

  if (value > maximum_inventory_value):
    maximum_inventory_value = value
    maximum_inventory_product_value = product[0]

print("Product With Highest Inventory Value:" , maximum_inventory_product_value)

print()

minimum_stock_value = products[0][2]
minimum_stock_product_value = products[0][0]

for i in range(1 , len(products)):
  if (products[i][2] < minimum_stock_value):
    minimum_stock_value = products[i][2]
    minimum_stock_product_value = products[i][0]

print("Product With Low Stock:" , minimum_stock_product_value)

print()

product_name = input("Enter a product:")

print("Enter product name:" , product_name)

quantity_to_add = int(input("Enter a quantity:"))

print("Enter quantity to add" , quantity_to_add)

for product in products:
  if (product[0] == product_name):
    product[2] += quantity_to_add
    print()
    print("Quantity Updated Successfully.")
    break

print()

print("===== Updated Inventory =====")

print()

for product in products:
  print(product[0] , "Price:" , product[1]    , "Quantity:" , product[2])
      