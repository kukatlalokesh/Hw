"""Project four Iris features into two PCA dimensions and save a plot."""
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X = StandardScaler().fit_transform(iris.data)
points = PCA(n_components=2).fit_transform(X)
plt.figure(figsize=(8, 6))
scatter = plt.scatter(points[:, 0], points[:, 1], c=iris.target, cmap="viridis")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("Iris Dataset — 2D PCA Projection")
plt.colorbar(scatter, label="Species class")
plt.tight_layout()
path = Path(__file__).with_name("pca_projection.png")
plt.savefig(path, dpi=150)
print("Saved:", path)
plt.show()
