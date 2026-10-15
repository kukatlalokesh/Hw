"""Compare KMeans before and after PCA; cluster IDs may be permuted."""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

X = StandardScaler().fit_transform(load_iris().data)
projected = PCA(n_components=2).fit_transform(X)
original_labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X)
projected_labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(projected)
print("Original silhouette score:", round(silhouette_score(X, original_labels), 3))
print("PCA silhouette score:", round(silhouette_score(projected, projected_labels), 3))
print("Cluster assignment similarity (ARI):",
      round(adjusted_rand_score(original_labels, projected_labels), 3))
print("Silhouette scores use different feature spaces; interpret with care.")
