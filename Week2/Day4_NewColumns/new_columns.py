import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Math": [85, 72, 95, 81],
    "Science": [90, 68, 92, 79],
    "English": [88, 75, 96, 84]
})

df["Total_Marks"] = df[["Math", "Science", "English"]].sum(axis=1)
df["Percentage"] = df["Total_Marks"] / 3

print("Data with new columns:")
print(df)
