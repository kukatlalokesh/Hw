import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT", "Finance", "HR"],
    "Experience": [2, 4, 5, 3, 6, 7, 4, 5],
    "Salary": [55000, 62000, 78000, 60000, 72000, 90000, 68000, 75000],
    "Score": [72, 78, 88, 75, 84, 94, 80, 86]
})

sns.countplot(data=df, x="Department")
plt.title("Employee Count by Department")
plt.tight_layout()
plt.show()

sns.boxplot(data=df, x="Department", y="Salary")
plt.title("Salary Distribution by Department")
plt.tight_layout()
plt.show()

sns.pairplot(df[["Experience", "Salary", "Score"]])
plt.show()
