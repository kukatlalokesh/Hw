import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [65, 70, 72, 78, 82, 86, 91, 95],
    "Assignments": [60, 64, 70, 75, 80, 85, 90, 94],
    "Score": [55, 60, 65, 70, 74, 82, 88, 93]
})

correlation_matrix = df.corr(numeric_only=True)

print("Correlation Matrix:")
print(correlation_matrix)

sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
