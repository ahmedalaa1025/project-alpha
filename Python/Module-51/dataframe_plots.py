# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
#     "Sales": [100, 130, 120, 160, 190]
# }

# df = pd.DataFrame(data)

# df.plot(
#     x="Month",
#     y="Sales"
#     kind="line",
#     marker="o",
#     linewidth=2
# )

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.grid()

# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Product": [
#         "Laptop",
#         "Phone",
#         "Tablet",
#         "Monitor"
#     ],

#     "Sales": [
#         120,
#         200,
#         80,
#         150
#     ]
# }

# df = pd.DataFrame(data)

# df.plot(
#     x="Product",
#     y="Sales",
#     kind="bar"
# )

# plt.title("Product Sales")

# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# data = {
#     "Salary": [
#         5000, 5500, 6000,
#         6200, 6500, 7000,
#         7200, 7500, 8000,
#         8500, 9000, 9500
#     ]
# }

# df = pd.DataFrame(data)

# df["Salary"].plot(
#     kind="hist",
#     bins=5
# )

# plt.title("Salary Distribution")
# plt.xlabel("Salary")

# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Experience": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10
    ],

    "Salary": [
        3500, 4000, 4500, 5000, 5500,
        6000, 6500, 7000, 7500, 8000
    ]
}

df = pd.DataFrame(data)

df.plot(
    x="Experience",
    y="Salary",
    kind="scatter"
)

plt.title("Experience vs Salary")

plt.show()
