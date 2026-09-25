import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "StudyHours": [2, 4, 5, 3, 6, 7, 8, 5],
    "Score": [55, 65, 72, 68, 82, 88, 94, 78]
})

print("Dataset:")
print(df)

print("\nSummary statistics:")
print(df.describe())

average_score = df["Score"].mean()
median_score = df["Score"].median()
average_study = df["StudyHours"].mean()
top_department = df.groupby("Department")["Score"].mean().idxmax()
top_department_score = df.groupby("Department")["Score"].mean().max()

print("\nKey observations:")
print(f"1. Average score is {average_score:.2f}.")
print(f"2. Median score is {median_score:.2f}.")
print(f"3. Average study time is {average_study:.2f} hours.")
print(f"4. {top_department} has the highest average score at {top_department_score:.2f}.")
print("5. The scatter plot below shows the relationship between study hours and score.")

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="StudyHours", y="Score", hue="Department")
plt.title("Study Hours vs Score")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Department", y="Score")
plt.title("Average Score by Department")
plt.tight_layout()
plt.show()
