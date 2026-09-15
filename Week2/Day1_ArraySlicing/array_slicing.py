import numpy as np

array = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print("Original Array:")
print(array)

# Access individual elements
print("\nElement at row 1, column 2:", array[0, 1])
print("Element at row 3, column 4:", array[2, 3])

# Access rows
print("\nFirst row:", array[0])
print("Second row:", array[1])

# Access columns
print("First column:", array[:, 0])
print("Third column:", array[:, 2])

# Slice rows and columns
print("\nFirst two rows:")
print(array[:2])

print("First two columns:")
print(array[:, :2])

print("Rows 1-2 and columns 2-4:")
print(array[:2, 1:])
