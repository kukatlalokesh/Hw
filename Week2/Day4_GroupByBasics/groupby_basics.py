import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Frank"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Score": [88, 76, 95, 84, 91, 79]
})

count_by_department = df.groupby("Department")["Name"].count()
average_by_department = df.groupby("Department")["Score"].mean()

print("Student count by department:")
print(count_by_department)

print("\nAverage score by department:")
print(average_by_department)
