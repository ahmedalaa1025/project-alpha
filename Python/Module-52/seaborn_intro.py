# import seaborn as sns

# print(sns.__version__)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 130, 120, 160, 190]
}

df = pd.DataFrame(data)

sns.lineplot(
    data=df,
    x="Month",
    y="Sales"
)

plt.show()
