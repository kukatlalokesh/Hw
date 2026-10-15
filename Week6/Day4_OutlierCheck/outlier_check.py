"""Distance-based outlier check in a 2D dataset."""
from math import dist

points = [(1, 2), (2, 1), (2, 3), (3, 2), (2, 2), (30, 30)]
# Mean distance to the two nearest OTHER points.
distances = []
for i, point in enumerate(points):
    nearest = sorted(dist(point, other) for j, other in enumerate(points) if i != j)[:2]
    distances.append(sum(nearest)/len(nearest))
for point, score in zip(points, distances):
    print(point, "average distance to 2 nearest neighbors:", round(score, 2))
print("Largest-distance point:", points[distances.index(max(distances))])
