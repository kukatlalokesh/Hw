import numpy as np

numbers = np.array([10, 20, 30, 40, 50, 60, 70])

mean_value = np.mean(numbers)
median_value = np.median(numbers)
std_value = np.std(numbers)

# Manual calculations for comparison
manual_mean = sum(numbers) / len(numbers)

sorted_numbers = sorted(numbers)
middle = len(sorted_numbers) // 2
if len(sorted_numbers) % 2 == 1:
    manual_median = sorted_numbers[middle]
else:
    manual_median = (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2

manual_variance = sum((number - manual_mean) ** 2 for number in numbers) / len(numbers)
manual_std = manual_variance ** 0.5

print("Numbers:")
print(numbers)

print("\nNumPy statistics:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard deviation:", std_value)

print("\nManual calculations:")
print("Mean:", manual_mean)
print("Median:", manual_median)
print("Standard deviation:", manual_std)
