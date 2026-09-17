import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Score": [88, 76, 95, 84, 91]
})

print("Single column:")
print(df["Name"])

print("\nMultiple columns:")
print(df[["Name", "Score"]])

print("\nStudents with Score >= 85:")
print(df[df["Score"] >= 85])

print("\nIT department students:")
print(df[df["Department"] == "IT"])
