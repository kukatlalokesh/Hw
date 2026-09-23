import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR", "Finance"],
    "Score": [88, 76, 95, 84, 91, 79, 87, 82, 90]
})

counts = df["Department"].value_counts()
averages = df.groupby("Department")["Score"].mean()

print("Count by department:")
print(counts)

print("\nAverage score by department:")
print(averages)

summary = averages.reset_index()

sns.barplot(data=summary, x="Department", y="Score")
plt.title("Average Score by Department")
plt.xlabel("Department")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()
