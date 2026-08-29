# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#     "Sales": [120, 150, 140, 180, 200, 230]
# }

# df = pd.DataFrame(data)

# sns.lineplot(
#     data=df,
#     x="Month",
#     y="Sales",
#     marker="o"
# )

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.grid()

# plt.show()

# import pandas as pd
# import seaborn as sns
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

# sns.barplot(
#     data=df,
#     x="Product",
#     y="Sales"
# )

# plt.title("Product Sales")
# plt.xlabel("Product")
# plt.ylabel("Sales")

# plt.show()

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Experience": [1, 2, 3, 4, 5, 6, 7, 8],
#     "Salary": [3500, 4000, 4500, 5000, 5500, 6200, 7000, 8000]
# }

# df = pd.DataFrame(data)

# sns.scatterplot(
#     data=df,
#     x="Experience",
#     y="Salary"
# )

# plt.title("Experience vs Salary")
# plt.xlabel("Experience")
# plt.ylabel("Salary")

# plt.show()

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Salary": [
#         3500, 4000, 4500,
#         5000, 5500, 6200,
#         7000, 8000, 8500,
#         9000
#     ]
# }

# df = pd.DataFrame(data)

# sns.histplot(
#     data=df,
#     x="Salary",
#     bins=5
# )

# plt.title("Salary Distribution")
# plt.xlabel("Salary")

# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.set_theme(style="whitegrid")

# sns.lineplot(
#     x=["Jan", "Feb", "Mar", "Apr"],
#     y=[100, 150, 130, 180],
#     marker="o"
# )

# plt.title("Monthly Sales")

# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 140, 180, 200, 230]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.lineplot(
    data=df,
    x="Month",
    y="Sales",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()

plt.show()
