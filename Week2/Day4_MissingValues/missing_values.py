import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [22, np.nan, 21, 23, np.nan],
    "Score": [88, 76, np.nan, 84, 91]
})

print("Original data:")
print(df)

print("\nMissing values by column:")
print(df.isnull().sum())

filled_df = df.copy()
filled_df["Age"] = filled_df["Age"].fillna(filled_df["Age"].mean())
filled_df["Score"] = filled_df["Score"].fillna(filled_df["Score"].mean())

print("\nAfter filling missing numeric values:")
print(filled_df)

dropped_df = df.dropna()

print("\nRows after dropping missing values:")
print(dropped_df)
