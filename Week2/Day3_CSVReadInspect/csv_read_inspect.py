import pandas as pd

csv_file = "students.csv"

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Age": [22, 24, 21, 23, 25],
    "Score": [88, 76, 95, 84, 91]
}

pd.DataFrame(data).to_csv(csv_file, index=False)

df = pd.read_csv(csv_file)

print("First rows:")
print(df.head())

print("\nLast rows:")
print(df.tail())

print("\nDataFrame information:")
df.info()

print("\nDescriptive statistics:")
print(df.describe())
