"""Add cluster labels and summarize each group without external libraries."""
# Pure Python KMeans: no third-party packages needed.
def kmeans(points, k, iterations=50):
    centers = [list(points[i * len(points) // k]) for i in range(k)]
    for _ in range(iterations):
        labels = [
            min(range(k), key=lambda j: sum((a - b) ** 2 for a, b in zip(p, centers[j])))
            for p in points
        ]
        updated = []
        for j in range(k):
            members = [p for p, label in zip(points, labels) if label == j]
            updated.append(
                [sum(p[d] for p in members) / len(members) for d in range(len(points[0]))]
                if members else centers[j]
            )
        if updated == centers:
            break
        centers = updated
    labels = [
        min(range(k), key=lambda j: sum((a - b) ** 2 for a, b in zip(p, centers[j])))
        for p in points
    ]
    inertia = sum(
        sum((a - b) ** 2 for a, b in zip(p, centers[label]))
        for p, label in zip(points, labels)
    )
    return labels, centers, inertia

customers = [
    {"visits": 1, "spend": 10}, {"visits": 2, "spend": 12},
    {"visits": 3, "spend": 15}, {"visits": 2, "spend": 18},
    {"visits": 8, "spend": 75}, {"visits": 9, "spend": 80},
    {"visits": 10, "spend": 90}, {"visits": 9, "spend": 85},
]
points = [[c["visits"], c["spend"]] for c in customers]
labels, centers, _ = kmeans(points, 2)

for customer, label in zip(customers, labels):
    customer["cluster"] = label
    print(customer)

print("\nCluster summary:")
for group in range(2):
    members = [c for c in customers if c["cluster"] == group]
    avg_visits = sum(c["visits"] for c in members) / len(members)
    avg_spend = sum(c["spend"] for c in members) / len(members)
    print(f"Cluster {group}: count={len(members)}, "
          f"avg visits={avg_visits:.1f}, avg spend={avg_spend:.1f}")
print("Cluster numbers are arbitrary, not true class labels.")
