"""Compare removing and capping a synthetic salary outlier."""
from statistics import mean, median

salaries = [42000, 45000, 47000, 49000, 52000, 54000, 56000, 58000, 60000, 450000]
sorted_values = sorted(salaries)
lower, upper = sorted_values[:5], sorted_values[5:]
q1, q3 = median(lower), median(upper)
iqr = q3-q1
low, high = q1-1.5*iqr, q3+1.5*iqr
removed = [x for x in salaries if low <= x <= high]
capped = [min(max(x, low), high) for x in salaries]
print("Original mean:", round(mean(salaries), 2))
print("Mean after removal:", round(mean(removed), 2))
print("Mean after capping:", round(mean(capped), 2))
print("Outliers removed:", len(salaries)-len(removed))
print("This is illustrative data; investigate unusual real values before changing them.")
