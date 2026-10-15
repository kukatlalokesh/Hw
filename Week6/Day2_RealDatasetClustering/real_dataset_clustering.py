"""Cluster a small illustrative customer dataset. No external packages."""
import csv
from pathlib import Path

path = Path(__file__).with_name("customers.csv")
with path.open(newline="") as file:
    customers = list(csv.DictReader(file))
points = [(float(c["visits"]), float(c["spending"])) for c in customers]
# Two fixed starting centers; update until assignments stop changing.
centers = [list(points[0]), list(points[-1])]
for _ in range(30):
    labels = [min(range(2), key=lambda j: sum((a-b)**2 for a,b in zip(p, centers[j]))) for p in points]
    new_centers = []
    for j in range(2):
        group = [p for p,label in zip(points,labels) if label == j]
        new_centers.append([sum(p[d] for p in group)/len(group) for d in range(2)] if group else centers[j])
    if new_centers == centers:
        break
    centers = new_centers
for c, label in zip(customers, labels):
    print(c["customer_id"], "cluster", label)
print("Centers:", centers)
print("Note: CSV contains illustrative customer records, not verified real-world data.")
