import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Score": [62, 65, 68, 70, 72, 74, 75, 78, 80, 82, 85, 88, 150]
})

q1 = df["Score"].quantile(0.25)
q3 = df["Score"].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[
    (df["Score"] < lower_bound) |
    (df["Score"] > upper_bound)
]

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print("\nOutliers:")
print(outliers)

plt.boxplot(df["Score"])
plt.title("Score Outlier Detection")
plt.ylabel("Score")
plt.tight_layout()
plt.show()
