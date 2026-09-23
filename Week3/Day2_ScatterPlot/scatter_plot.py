import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "StudyHours": [2, 3, 4, 5, 6, 7, 8, 9],
    "Score": [55, 60, 65, 70, 74, 82, 88, 93]
})

plt.scatter(df["StudyHours"], df["Score"])
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
