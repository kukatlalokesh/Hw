import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": ["22", "24", "21", "23"],
    "JoinDate": ["2026-01-15", "2026-02-20", "2026-03-10", "2026-04-05"],
    "Department": ["IT", "HR", "IT", "Finance"]
})

print("Original data types:")
print(df.dtypes)

df["Age"] = pd.to_numeric(df["Age"])
df["JoinDate"] = pd.to_datetime(df["JoinDate"])
df["Department"] = df["Department"].astype("category")

print("\nConverted data types:")
print(df.dtypes)

print("\nConverted DataFrame:")
print(df)
