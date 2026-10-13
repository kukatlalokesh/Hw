"""Practice KMeans fit_predict and inspect cluster centers."""
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(
    n_samples=60, centers=3, cluster_std=0.8, random_state=42
)
model = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = model.fit_predict(X)
print("First 15 cluster assignments:", labels[:15])
print("Number of clusters:", model.n_clusters)
print("Cluster centers:\n", model.cluster_centers_)
for cluster in range(model.n_clusters):
    print(f"Cluster {cluster}: {(labels == cluster).sum()} points")
