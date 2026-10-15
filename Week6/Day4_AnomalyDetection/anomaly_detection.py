"""Find unusual values with a z-score and IQR. Standard library only."""
from statistics import mean, pstdev

values = [10, 11, 12, 12, 13, 14, 15, 12, 11, 100]
avg, std = mean(values), pstdev(values)
print("Mean:", avg, "Std:", round(std, 2))
for value in values:
    z = (value - avg) / std if std else 0
    print(value, "z-score:", round(z, 2), "outlier (|z| > 2):", abs(z) > 2)

sorted_values = sorted(values)
lower = sorted_values[:len(values)//2]
upper = sorted_values[len(values)//2:]
def median(items):
    n = len(items)
    return items[n//2] if n % 2 else (items[n//2-1]+items[n//2])/2
q1, q3 = median(lower), median(upper)
iqr = q3 - q1
low, high = q1 - 1.5*iqr, q3 + 1.5*iqr
print("IQR limits:", low, high)
print("IQR outliers:", [x for x in values if x < low or x > high])
