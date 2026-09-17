import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [22, 24, 21, 23],
    "Score": [88, 76, 95, 84]
}

df_from_dict = pd.DataFrame(data)

data_list = [
    ["Ethan", 25, 91],
    ["Frank", 22, 79],
    ["Grace", 24, 87]
]

df_from_list = pd.DataFrame(data_list, columns=["Name", "Age", "Score"])

print("DataFrame from dictionary:")
print(df_from_dict)

print("\nFirst two rows:")
print(df_from_dict.head(2))

print("\nName and Score columns:")
print(df_from_dict[["Name", "Score"]])

print("\nDataFrame from list:")
print(df_from_list)

print("\nRows:")
print(df_from_list.iloc[0])
