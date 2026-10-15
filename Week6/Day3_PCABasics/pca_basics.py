"""PCA reduces feature count while preserving as much variance as possible."""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = load_iris().data
scaled = StandardScaler().fit_transform(X)
pca = PCA(n_components=2)
reduced = pca.fit_transform(scaled)
print("Original shape:", X.shape)
print("PCA shape:", reduced.shape)
print("First 5 transformed rows:\n", reduced[:5])
