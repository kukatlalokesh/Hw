"""Plot KMeans clusters on a two-feature sample dataset."""
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(
    n_samples=120, centers=3, cluster_std=0.85, random_state=42
)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X)
centers = model.cluster_centers_

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", alpha=0.8)
plt.scatter(
    centers[:, 0], centers[:, 1],
    marker="X", s=220, c="red", edgecolors="black", label="Centroids"
)
plt.title("KMeans Clustering (3 clusters)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.colorbar(scatter, label="Cluster")
plt.tight_layout()
output = Path(__file__).with_name("clusters.png")
plt.savefig(output, dpi=150)
print("Saved visualization to:", output)
plt.show()
