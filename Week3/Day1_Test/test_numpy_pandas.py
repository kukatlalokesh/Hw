import numpy as np
import pandas as pd

# 1. Arrays: create an array and calculate basic statistics.
numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)
print("Mean:", np.mean(numbers))
print("Standard deviation:", np.std(numbers))

# 2. DataFrame: create a small dataset.
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": [88, 72, 95, 81],
    "Department": ["IT", "HR", "IT", "Finance"]
})

print("\nDataFrame:")
print(df)

# 3. Filtering: select students with scores of 85 or higher.
high_scores = df[df["Score"] >= 85]
print("\nScores >= 85:")
print(high_scores)

# 4. Basic statistics.
print("\nScore statistics:")
print("Mean:", df["Score"].mean())
print("Median:", df["Score"].median())
print("Standard deviation:", df["Score"].std())
