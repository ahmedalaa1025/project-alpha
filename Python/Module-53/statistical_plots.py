# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Department": [
#         "IT", "IT", "IT",
#         "HR", "HR", "HR"
#     ],

#     "Salary": [
#         7000, 8000, 9000,
#         5000, 6000, 6500
#     ]
# }

# df = pd.DataFrame(data)

# sns.boxplot(
#     data=df,
#     x="Department",
#     y="Salary"
# )

# plt.title("Salary Distribution by Department")

# plt.show()

# import pandas as pd 
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Department": [
#         "IT",
#         "HR",
#         "IT",
#         "Finance",
#         "IT",
#         "HR"
#     ]
# }

# df = pd.DataFrame(data)

# sns.countplot(
#     data=df,
#     x="Department"
# )

# plt.title("Employees by Department")

# plt.show()

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = {
#     "Experience": [
#         1, 2, 3, 4,
#         5, 6, 7, 8
#     ],

#     "Salary": [
#         3500, 4000, 4500, 5000,
#         5500, 6200, 7000, 8000
#     ]
# }

# df = pd.DataFrame(data)

# sns.regplot(
#     data=df,
#     x="Experience",
#     y="Salary"
# )

# plt.title("Experience vs Salary")

# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
     "Experience": [
         1, 2, 3, 4,
         5, 6, 7, 8
     ],

     "Salary": [
         3500, 4000, 4500, 5000,
         5500, 6200, 7000, 8000
     ]
 }

df = pd.DataFrame(data)


correlation = df[
    ["Experience", "Salary"]
].corr()

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()
