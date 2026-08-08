import pandas as pd

group_1 = {
    "Name": ["Ahmed", "Omar", "Sara"],
    "Math": [85, 70, 95],
    "Physics": [90, 65, 98]
}

group_2 = {
    "Name": ["Mariam", "Ali", "Youssef"],
    "Math": [80, 88, 75],
    "Physics": [84, 91, 78]
}

group_3 = {
    "Name": ["Hana", "Khaled", "Adam"],
    "Math": [92, 76, 89],
    "Physics": [95, 72, 91]
}

df1 = pd.DataFrame(group_1)
df2 = pd.DataFrame(group_2)
df3 = pd.DataFrame(group_3)

combined_df = pd.concat(
    [df1, df2, df3],
    keys=["group_1", "group_2", "group_3"]
)

print("===== Combined Data =====")
print(combined_df)

combined_df_1 = pd.concat(
    [df1, df2, df3],
    ignore_index=True
)

print("===== Combined Data =====")
print(combined_df_1)

combined_df_1["Total"] = combined_df_1["Math"] + combined_df_1["Physics"]

combined_df_1["Average"] = combined_df_1["Total"] / 2

combined_df_1 = combined_df_1.sort_values(by="Average", ascending=False)

combined_df_1.to_csv("students_concat_report.csv", index=False)

combined_df_1.to_excel("students_concat_report.xlsx", index=False)

combined_df_1 = pd.read_csv("students_concat_report.csv")

print(combined_df_1)
