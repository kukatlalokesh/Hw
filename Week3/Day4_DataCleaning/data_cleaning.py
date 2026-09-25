import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Bob", "Charlie", "Diana"],
    "Department": ["it", "HR", "HR", "finance", "IT"],
    "Score": [88, 76, 76, 91, 84]
})

print("Original data:")
print(df)

print("\nDuplicate rows:")
print(df[df.duplicated()])

df = df.drop_duplicates().copy()

# Standardize column names and text values.
df.columns = [column.strip().lower() for column in df.columns]
df["department"] = df["department"].str.strip().str.upper()

print("\nCleaned data:")
print(df)
