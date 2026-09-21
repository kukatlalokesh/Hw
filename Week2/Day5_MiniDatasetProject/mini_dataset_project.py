import pandas as pd
import numpy as np

data = {
    "Student": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Frank"],
    "Math": [85, 72, np.nan, 91, 68, 79],
    "Science": [90, 68, 92, 88, np.nan, 81],
    "English": [88, 75, 96, 84, 71, np.nan]
}

df = pd.DataFrame(data)

print("Original dataset:")
print(df)

# Clean missing marks using the column mean.
for column in ["Math", "Science", "English"]:
    df[column] = df[column].fillna(df[column].mean())

# Analyze the cleaned dataset.
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3
df["Grade"] = pd.cut(
    df["Average"],
    bins=[-float("inf"), 59, 69, 79, 89, float("inf")],
    labels=["F", "D", "C", "B", "A"]
)

print("\nCleaned and analyzed dataset:")
print(df)

print("\nSummary:")
print("Average class score:", round(df["Average"].mean(), 2))
print("Highest average:", round(df["Average"].max(), 2))
print("Lowest average:", round(df["Average"].min(), 2))
print("\nGrade counts:")
print(df["Grade"].value_counts().sort_index())
