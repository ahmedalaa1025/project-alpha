import pandas as pd
import numpy as np

students = {
    "Name": ["Ahmed", "Omar", "Sara", "Mariam", "Ali", "Youssef"],
    "Math": [85, np.nan, 95, 80, 88, 75],
    "Physics": [90, 65, np.nan, 84, 91, np.nan],
    "AI": [88, 68, 94, np.nan, 90, 85]
}

df = pd.DataFrame(students) 

print(df)

print(df.isna())

print(df.isna().sum())

clean_df = df.copy()

clean_df["Math"] = clean_df["Math"].fillna(clean_df["Math"].mean())
clean_df["Physics"] = clean_df["Physics"].fillna(clean_df["Physics"].mean())
clean_df["AI"] = clean_df["AI"].fillna(clean_df["AI"].mean())

clean_df["Total"] = clean_df["Math"] + clean_df["Physics"] + clean_df["AI"]
clean_df["Average"] = clean_df["Total"] / 3

clean_df["Status"] = np.where(clean_df["Average"] >= 85, "Excellent", "Good")

clean_df = clean_df.sort_values(by="Average", ascending=False)

clean_df = clean_df.set_index("Name")

print(clean_df.loc["Ali"])

clean_df = clean_df.reset_index(drop=False)

print(clean_df)
