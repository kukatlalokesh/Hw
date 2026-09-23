import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Score": [55, 60, 62, 65, 68, 70, 72, 74, 76, 78, 80, 82, 85, 90, 98]
})

mean_score = df["Score"].mean()
median_score = df["Score"].median()

print("Mean:", round(mean_score, 2))
print("Median:", median_score)

if mean_score > median_score:
    print("The mean is above the median, suggesting some higher values pull the average upward.")
elif mean_score < median_score:
    print("The mean is below the median, suggesting some lower values pull the average downward.")
else:
    print("The mean and median are equal, suggesting a balanced distribution.")

sns.histplot(data=df, x="Score", bins=8, kde=True)
plt.axvline(mean_score, linestyle="--", label="Mean")
plt.axvline(median_score, linestyle=":", label="Median")
plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.show()
