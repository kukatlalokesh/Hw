import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "StudyHours": [2, 4, 5, 3, 6, 7, 8, 5],
    "Score": [55, 65, 72, 68, 82, 88, 94, 78]
})

print("Dataset:")
print(df)

print("\nBasic information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

print("\nAverage score by department:")
print(df.groupby("Department")["Score"].mean())

plt.figure(figsize=(8, 5))
plt.scatter(df["StudyHours"], df["Score"])
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
df.groupby("Department")["Score"].mean().plot(kind="bar")
plt.title("Average Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

print("\nFindings:")
print("1. Scores generally increase as study hours increase.")
print("2. Department average scores are different.")
print("3. The dataset contains both numerical and categorical columns.")
