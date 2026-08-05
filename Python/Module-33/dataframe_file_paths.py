import os
import pandas as pd

print("===== Current Working Directory =====")
print(os.getcwd())

print()

df = pd.read_csv("students.csv")

print(df)
