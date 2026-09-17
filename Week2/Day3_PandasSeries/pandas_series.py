import pandas as pd

series = pd.Series([85, 92, 78, 90, 88], index=["Alice", "Bob", "Charlie", "Diana", "Ethan"])

print("Pandas Series:")
print(series)

print("\nValue for Bob:", series["Bob"])
print("\nFirst three values:")
print(series[:3])

print("\nStudents with marks >= 85:")
print(series[series >= 85])

print("\nValues:")
print(series.values)

print("\nIndex:")
print(series.index)
