import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Python/Data_Visualization_Comprehensive_Exam/Dataset/dataset.csv")

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print(df.describe())

print(df.isna().sum())

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df.shape)

avg_salary = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)

avg_performance = df.groupby("Department")["Performance"].mean().sort_values(ascending=False)

print(avg_salary)

print(avg_performance)

print(df.groupby("Gender")["Salary"].mean())

print(df.loc[df["Salary"].idxmax()])

print(df.loc[df["Performance"].idxmax()])

print(df[["Experience", "Salary", "Performance"]].corr())

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))

sorted_df = df.sort_values("Experience")

plt.plot(
    sorted_df["Experience"],
    sorted_df["Salary"],
    marker="o"
)

plt.title("Salary by Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.grid(True)

plt.show()

plt.figure(figsize=(8, 5))

plt.bar(
    avg_salary.index,
    avg_salary.values
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

plt.figure(figsize=(8, 5))

plt.hist(
    df["Salary"],
    bins=6
)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.show()

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Experience"],
    df["Salary"]
)

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="Department",
    y="Salary",
    order=avg_salary.index
)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Gender",
    y="Salary"
)

plt.title("Salary Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Salary")

plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Experience",
    y="Salary",
    hue="Department"
)

plt.title("Experience vs Salary by Department")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Department",
    y="Performance"
)

plt.title("Performance Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Performance")

plt.show()

correlation = df.corr(numeric_only=True)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

print("Insight 1: IT has a little higher average salry than Finance and HR Department.")
print("Insight 2: The higher distribution of salary is in the range between 6000 & 7000.")
print("Insight 3: The distribution of salary by gender for male is between 5000 & 7000 and for female is between 6000 & 8000.")
print("Insight 4: The performance distribution by department shows that the IT department has a little higher performance than Finance and HR Department.")
print("Insight 5: The distribution of IT apperas between 83 & 92 & Finance between 80 & 91 & HR between 76 & 86.")
