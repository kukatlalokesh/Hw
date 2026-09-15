import numpy as np

# Create a 1D array
original_array = np.arange(1, 13)

# Reshape the 1D array into a 3x4 matrix
reshaped_array = original_array.reshape(3, 4)

# Flatten the reshaped array back into 1D
flattened_array = reshaped_array.flatten()

print("Original 1D array:")
print(original_array)
print("Shape:", original_array.shape)

print("\nReshaped 3x4 array:")
print(reshaped_array)
print("Shape:", reshaped_array.shape)

print("\nFlattened array:")
print(flattened_array)
print("Shape:", flattened_array.shape)

print("\nSame values after reshape and flatten:", np.array_equal(original_array, flattened_array))
