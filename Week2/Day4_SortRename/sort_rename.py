import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Score": [88, 76, 95, 84],
    "Department": ["IT", "HR", "IT", "Finance"]
})

renamed_df = df.rename(columns={
    "Name": "Student_Name",
    "Score": "Marks"
})

print("Renamed columns:")
print(renamed_df)

print("\nSorted by Marks descending:")
print(renamed_df.sort_values(by="Marks", ascending=False))

print("\nSorted by Department and Marks:")
print(renamed_df.sort_values(by=["Department", "Marks"]))
