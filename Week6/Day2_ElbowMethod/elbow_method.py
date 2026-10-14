"""Elbow method: compare K=1..6 and draw a text-based elbow chart."""
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
    [1, 2], [2, 1], [2, 3], [3, 2],
    [10, 10], [11, 10], [10, 11], [12, 10],
    [21, 2], [22, 3], [23, 2], [22, 1],
]
results = []
for k in range(1, 7):
    _, _, inertia = kmeans(points, k)
    results.append((k, inertia))
    print(f"K={k}: inertia={inertia:.2f}")

print("\nElbow chart (shorter bars mean lower within-cluster error):")
largest = max(value for _, value in results)
for k, value in results:
    bar = "#" * max(1, round(value / largest * 45))
    print(f"K={k} | {bar} ({value:.1f})")
print("\nLook for where improvement begins to slow down; the elbow is a heuristic.")
