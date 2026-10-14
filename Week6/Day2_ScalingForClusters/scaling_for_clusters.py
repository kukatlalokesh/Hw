"""Compare KMeans assignments before and after standardizing features."""
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

points = [
    [1, 100], [2, 110], [3, 105],
    [8, 108], [9, 115], [10, 112],
    [1, 400], [2, 410], [3, 405],
    [8, 408], [9, 415], [10, 412],
]

# Standardize each column: (value - mean) / population standard deviation.
means = [sum(p[d] for p in points) / len(points) for d in range(2)]
stds = [
    (sum((p[d] - means[d]) ** 2 for p in points) / len(points)) ** 0.5
    for d in range(2)
]
scaled = [
    [(p[d] - means[d]) / stds[d] if stds[d] else 0 for d in range(2)]
    for p in points
]

raw_labels, _, raw_inertia = kmeans(points, 2)
scaled_labels, _, scaled_inertia = kmeans(scaled, 2)
print("Index | Features | Raw cluster | Scaled cluster")
for i, point in enumerate(points):
    print(f"{i:>5} | {str(point):>10} | {raw_labels[i]:>11} | {scaled_labels[i]:>14}")
print(f"Raw inertia: {raw_inertia:.2f}")
print(f"Scaled inertia: {scaled_inertia:.2f}")
print("Inertia values are on different scales and should not be compared directly.")
print("Scaling gives both features comparable influence on distances.")
